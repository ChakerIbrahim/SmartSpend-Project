from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, logout, authenticate, update_session_auth_hash
from django.contrib.auth.models import User
from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404
from django.db.models import Sum
from django.core.mail import EmailMultiAlternatives
from django.conf import settings
from .models import Expense, BillReminder, Budget, UserProfile, SupportMessage

from django.http import JsonResponse
import json

import os
import random
import datetime
from dotenv import load_dotenv
import google.generativeai as genai

load_dotenv()
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

def get_currency_symbol(user):
    try:
        profile = user.userprofile
        symbols = {'USD': '$', 'ILS': '₪', 'EUR': '€'}
        return symbols.get(profile.currency, '$')
    except Exception:
        return '$'


# ---------------------------------------------------------------------------
# Public views
# ---------------------------------------------------------------------------

def landing_page(request):
    return render(request, "landingPage.html")


def login_view(request):
    if request.method == "POST":
        email    = request.POST.get("email")
        password = request.POST.get("password")

        user_obj = User.objects.filter(email=email).first()

        if user_obj:
            user = authenticate(
                request,
                username=user_obj.username,
                password=password,
            )
            if user:
                login(request, user, backend="django.contrib.auth.backends.ModelBackend")
                return redirect("dashboard")

    return render(request, "login.html")


def register_view(request):
    """
    Registration with email-verification flow (Doc 3).
    A 6-digit code is sent via SendGrid; the user is created only after
    the code is confirmed in verify_email_view.
    """
    if request.method == "POST":
        fullname         = request.POST.get("fullname")
        username         = request.POST.get("username")
        email            = request.POST.get("email")
        password         = request.POST.get("password")
        confirm_password = request.POST.get("confirm_password")

        if password != confirm_password:
            messages.error(request, "Passwords do not match.")
            return redirect("register")

        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already exists.")
            return redirect("register")

        if User.objects.filter(email=email).exists():
            messages.error(request, "Email already exists.")
            return redirect("register")

        code = str(random.randint(100000, 999999))

        request.session["verification_code"] = code
        request.session["temp_user"] = {
            "fullname": fullname,
            "username": username,
            "email":    email,
            "password": password,
        }

        # ── DEBUG: print code to terminal so you can test without SendGrid ──
        print(f"============ VERIFICATION CODE: {code} ============")

        try:
            mail = EmailMultiAlternatives(
                subject="Email Verification - SmartSpend X",
                body=" ",
                from_email=settings.DEFAULT_FROM_EMAIL,
                to=[email],
            )
            mail.content_subtype        = "html"
            mail.template_id            = "d-88d3829c61fe4d0f9a37ee5e658da67d"
            mail.dynamic_template_data  = {
                "verification_code": code,
                "first_name":        fullname,
                "current_year":      datetime.datetime.now().year,
            }
            mail.send(fail_silently=False)

        except Exception as e:
            print("================ SENDGRID ERROR ================")
            print(str(e))
            print("================================================")
            # Don't redirect back to register — still go to verify page
            # so the user can enter the code printed in the terminal above.
            messages.warning(request, "Email sending failed — use the code printed in the server terminal.")

        return redirect("verify_email")

    return render(request, "register.html")


def forgot_password_view(request):
    if request.method == "POST":
        email = request.POST.get("email")
        user = User.objects.filter(email=email).first()

        if user:
            request.session["reset_user_id"] = user.id
            return redirect("reset_password")
        else:
            messages.error(request, "No account found with that email.")
            return redirect("forgot_password")

    return render(request, "forgot-password.html")


def reset_password_view(request):
    user_id = request.session.get("reset_user_id")

    if not user_id:
        messages.error(request, "Please verify your email first.")
        return redirect("forgot_password")

    user = User.objects.filter(id=user_id).first()
    if not user:
        messages.error(request, "Something went wrong. Please try again.")
        return redirect("forgot_password")

    if request.method == "POST":
        password = request.POST.get("password")
        confirm_password = request.POST.get("confirm_password")

        if password != confirm_password:
            messages.error(request, "Passwords do not match.")
            return render(request, "reset-password.html")

        user.set_password(password)
        user.save()

        del request.session["reset_user_id"]

        messages.success(request, "Your password has been reset successfully. Please log in.")
        return redirect("login")

    return render(request, "reset-password.html")


def verify_email_view(request):
    if request.method == "POST":
        entered_code = request.POST.get("code")
        session_code = request.session.get("verification_code")
        user_data    = request.session.get("temp_user")

        print("=== VERIFICATION PROCESS STARTED ===")
        print(f"Entered Code  : {entered_code}")
        print(f"Session Code  : {session_code}")
        print(f"User Payload  : {user_data}")
        print("=====================================")

        if entered_code == session_code and user_data:
            try:
                user = User.objects.create_user(
                    username=user_data["username"],
                    email=user_data["email"],
                    password=user_data["password"],
                )

                fullname = user_data.get("fullname", "")
                if fullname:
                    names = fullname.split(" ", 1)
                    user.first_name = names[0]
                    if len(names) > 1:
                        user.last_name = names[1]
                    user.save()

                del request.session["verification_code"]
                del request.session["temp_user"]

                messages.success(request, "Account created successfully. Please log in.")
                return redirect("login")

            except Exception as sql_error:
                print("================ DATABASE ERROR ================")
                print(str(sql_error))
                print("================================================")
                messages.error(request, "A database error occurred. Please try again.")
                return redirect("verify_email")
        else:
            messages.error(request, "Invalid verification code.")
            return redirect("verify_email")

    return render(request, "verify-email.html")

def success_view(request):
    return render(request, "success.html")

# ---------------------------------------------------------------------------
# Dashboard
# ---------------------------------------------------------------------------

@login_required
def dashboard(request):
    expenses       = Expense.objects.filter(user=request.user).order_by("-date")[:5]
    bills          = BillReminder.objects.filter(user=request.user, is_paid=False).order_by("due_date")[:3]
    total_expenses = Expense.objects.filter(user=request.user).aggregate(total=Sum("amount"))["total"] or 0
    total_budget   = Budget.objects.filter(user=request.user).aggregate(total=Sum("budget_amount"))["total"] or 0

    category_data = (
        Expense.objects.filter(user=request.user)
        .values("category")
        .annotate(total=Sum("amount"))
        .order_by("category")
    )
    chart_labels = [item["category"].capitalize() for item in category_data]
    chart_values = [float(item["total"])           for item in category_data]

    return render(request, "dashboard.html", {
        "expenses":       expenses,
        "bills":          bills,
        "total_budget":   total_budget,
        "total_expenses": total_expenses,
        "currency":       get_currency_symbol(request.user),
        "chart_labels":   chart_labels,
        "chart_values":   chart_values,
    })


# ---------------------------------------------------------------------------
# Expenses
# ---------------------------------------------------------------------------

# @login_required
# def expenses_view(request):
#     if request.method == "POST":
#         Expense.objects.create(
#             user=request.user,
#             title=request.POST.get("title"),
#             amount=request.POST.get("amount"),
#             category=request.POST.get("category"),
#             date=request.POST.get("date"),
#         )
#         return redirect("expenses")

#     expenses = Expense.objects.filter(user=request.user).order_by("-date")
#     return render(request, "expenses.html", {
#         "expenses": expenses,
#         "currency": get_currency_symbol(request.user),
#     })

@login_required
def expenses_view(request):
    if request.method == "POST":
        # AJAX request
        if request.content_type == 'application/json':
            data = json.loads(request.body)
            expense = Expense.objects.create(
                user=request.user,
                title=data.get("title"),
                amount=data.get("amount"),
                category=data.get("category"),
                date=data.get("date"),
            )
            return JsonResponse({
                'success': True,
                'expense': {
                    'id': expense.id,
                    'title': expense.title,
                    'amount': str(expense.amount),
                    'category': expense.category,
                    'date': str(expense.date),
                }
            })
        # Normal form submit fallback
        Expense.objects.create(
            user=request.user,
            title=request.POST.get("title"),
            amount=request.POST.get("amount"),
            category=request.POST.get("category"),
            date=request.POST.get("date"),
        )
        return redirect("expenses")

    expenses = Expense.objects.filter(user=request.user).order_by("-date")
    return render(request, "expenses.html", {
        "expenses": expenses,
        "currency": get_currency_symbol(request.user),
    })


@login_required
def all_expenses_view(request):
    expenses        = Expense.objects.filter(user=request.user).order_by("-date", "-id")
    total_expenses  = expenses.aggregate(total=Sum("amount"))["total"] or 0
    category_totals = expenses.values("category").annotate(total=Sum("amount")).order_by("-total")

    return render(request, "allExpenses.html", {
        "expenses":        expenses,
        "total_expenses":  total_expenses,
        "category_totals": category_totals,
        "currency":        get_currency_symbol(request.user),
    })


@login_required
def edit_expense_view(request, expense_id):
    expense = get_object_or_404(Expense, id=expense_id, user=request.user)

    if request.method == "POST":
        expense.title    = request.POST.get("title")
        expense.amount   = request.POST.get("amount")
        expense.category = request.POST.get("category")
        expense.date     = request.POST.get("date")
        expense.save()
        messages.success(request, "Expense updated successfully.")
        return redirect("all_expenses")

    return render(request, "editExpense.html", {
        "expense":    expense,
        "categories": Expense.CATEGORY_CHOICES,
        "currency":   get_currency_symbol(request.user),
    })


@login_required
def delete_expense(request, expense_id):
    expense = get_object_or_404(Expense, id=expense_id, user=request.user)
    expense.delete()
    # AJAX request
    if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
        return JsonResponse({'success': True})
    return redirect("expenses")

# ---------------------------------------------------------------------------
# Bill Reminders
# ---------------------------------------------------------------------------

@login_required
def bill_reminder_view(request):
    if request.method == "POST":
        try:
            BillReminder.objects.create(
                name=request.POST.get("name"),
                amount=request.POST.get("amount"),
                due_date=request.POST.get("due_date"),
                user=request.user,
            )
            return redirect("bill_reminder")

        except Exception:
            # Keep error handling from Doc 3
            bills        = BillReminder.objects.filter(user=request.user).order_by("due_date")
            unpaid_bills = bills.filter(is_paid=False)
            return render(request, "billReminder.html", {
                "bills":          bills,
                "upcoming_count": unpaid_bills.count(),
                "total_needed":   unpaid_bills.aggregate(total=Sum("amount"))["total"] or 0,
                "next_bill":      unpaid_bills.first(),
                "currency":       get_currency_symbol(request.user),
                "error":          "Invalid date. Please use the date picker or format YYYY-MM-DD.",
            })

    bills        = BillReminder.objects.filter(user=request.user).order_by("due_date")
    unpaid_bills = bills.filter(is_paid=False)
    return render(request, "billReminder.html", {
        "bills":          bills,
        "upcoming_count": unpaid_bills.count(),
        "total_needed":   unpaid_bills.aggregate(total=Sum("amount"))["total"] or 0,
        "next_bill":      unpaid_bills.first(),
        "currency":       get_currency_symbol(request.user),
    })


# ---------------------------------------------------------------------------
# Monthly Report
# ---------------------------------------------------------------------------

@login_required
def monthly_report_view(request):
    expenses    = Expense.objects.filter(user=request.user)
    total_spent = expenses.aggregate(total=Sum("amount"))["total"] or 0
    biggest_category = (
        expenses.values("category")
        .annotate(total=Sum("amount"))
        .order_by("-total")
        .first()
    )
    return render(request, "monthlyReport.html", {
        "expenses":         expenses,
        "total_spent":      total_spent,
        "biggest_category": biggest_category,
        "currency":         get_currency_symbol(request.user),
    })


# ---------------------------------------------------------------------------
# Budget Planning
# ---------------------------------------------------------------------------

@login_required
def budget_planning_view(request):
    if request.method == "POST":
        Budget.objects.create(
            income=request.POST.get("income"),
            category=request.POST.get("category"),
            budget_amount=request.POST.get("budget"),
            user=request.user,
        )
        return redirect("budget_planning")

    budgets = Budget.objects.filter(user=request.user)
    return render(request, "budgetPlanning.html", {
        "budgets":  budgets,
        "currency": get_currency_symbol(request.user),
    })

@login_required
def update_budget(request):
    if request.method == 'POST':
        # Grab income and budget limits from the form submission
        income = request.POST.get('income', 0)
        budget_amount = request.POST.get('budget_amount', 0)
        category = request.POST.get('category', 'General') # Default or selected category
       
        # Look for an existing budget for the current user, or create a new one
        budget, created = Budget.objects.get_or_create(
            user=request.user,
            category=category,
            defaults={'income': income, 'budget_amount': budget_amount}
        )
       
        # If it already existed, update the values
        if not created:
            budget.income = income
            budget.budget_amount = budget_amount
            budget.save()
           
        return redirect('dashboard')

# ---------------------------------------------------------------------------
# Profile
# ---------------------------------------------------------------------------

@login_required
def profile_view(request):
    expenses       = Expense.objects.filter(user=request.user).order_by("-date")[:4]
    total_expenses = Expense.objects.filter(user=request.user).aggregate(total=Sum("amount"))["total"] or 0
    return render(request, "profile.html", {
        "expenses":       expenses,
        "total_expenses": total_expenses,
        "currency":       get_currency_symbol(request.user),
    })


# ---------------------------------------------------------------------------
# Settings
# ---------------------------------------------------------------------------

@login_required
def settings_view(request):
    profile, _ = UserProfile.objects.get_or_create(user=request.user)

    if request.method == "POST":
        action = request.POST.get("action")

        if action == "update_info":
            request.user.username = request.POST.get("username")
            request.user.email    = request.POST.get("email")
            request.user.save()

            profile.currency = request.POST.get("currency")
            profile.language = request.POST.get("language")
            profile.save()

            messages.success(request, "Settings saved successfully.")
            return redirect("settings")

        if action == "change_password":
            current_password = request.POST.get("current_password")
            new_password     = request.POST.get("new_password")

            if not request.user.check_password(current_password):
                messages.error(request, "Current password is incorrect.")
                return redirect("settings")

            request.user.set_password(new_password)
            request.user.save()
            update_session_auth_hash(request, request.user)
            messages.success(request, "Password updated successfully.")
            return redirect("settings")

        if action == "delete_account":
            user = request.user
            logout(request)
            user.delete()
            return redirect("landing")

    return render(request, "settings.html", {"profile": profile})


# ---------------------------------------------------------------------------
# About Us  (with contact form — Doc 4)
# ---------------------------------------------------------------------------

def about_us_view(request):
    if request.method == "POST":
        name         = request.POST.get("name", "").strip()
        email        = request.POST.get("email", "").strip()
        message_text = request.POST.get("message", "").strip()

        if not name or not email or not message_text:
            messages.error(request, "Please fill in all fields.")
            return redirect("about_us")

        SupportMessage.objects.create(
            name=name,
            email=email,
            message=message_text,
            user=request.user if request.user.is_authenticated else None,
        )
        messages.success(request, "Your message has been sent successfully.")
        return redirect("about_us")

    return render(request, "about_us.html")


# ---------------------------------------------------------------------------
# AI Analysis  (Doc 4)
# ---------------------------------------------------------------------------

@login_required
def ai_analysis_view(request):

    expenses = Expense.objects.filter(user=request.user)

    total = expenses.aggregate(total=Sum("amount"))["total"] or 0

    expenses_text = "\n".join([
        f"{e.category} - {e.amount} - {e.date}"
        for e in expenses
    ])

    prompt = f"""
You are a professional AI financial advisor.

Analyze this user's expenses.

Total spending: {total}

Expenses:
{expenses_text}

Give:
1. Spending summary
2. Biggest financial problem
3. Saving advice
4. Budget recommendation
5. One motivational sentence

Keep the answer clean and professional.
"""

    ai_result = ""

    try:
        genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

        model = genai.GenerativeModel("gemini-2.5-flash")

        response = model.generate_content(prompt)

        ai_result = response.text

    except Exception as e:
        ai_result = str(e)

    return render(request, "aiAnalysis.html", {
        "ai_result": ai_result,
        "total": total,
    })