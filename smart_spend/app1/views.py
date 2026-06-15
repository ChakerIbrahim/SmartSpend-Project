from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, logout, authenticate, update_session_auth_hash
from django.contrib.auth.models import User
from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404
from django.db.models import Sum
from .models import Expense, BillReminder, Budget, UserProfile
import random
import datetime
from django.core.mail import EmailMultiAlternatives
from django.conf import settings

def get_currency_symbol(user):
    try:
        profile = user.userprofile
        symbols = {'USD': '$', 'ILS': '₪', 'EUR': '€'}
        return symbols.get(profile.currency, '$')
    except:
        return '$'

def landing_page(request):
    return render(request, "landingPage.html")

def login_view(request):
    if request.method == "POST":
        email = request.POST.get("email")
        password = request.POST.get("password")

        user_obj = User.objects.filter(email=email).first()

        if user_obj:
            user = authenticate(request, username=user_obj.username, password=password)
            if user:
                login(request, user)
                return redirect("dashboard")

    return render(request, "login.html")

def register_view(request):
    if request.method == "POST":
        fullname = request.POST.get("fullname")
        username = request.POST.get("username")
        email = request.POST.get("email")
        password = request.POST.get("password")
        confirm_password = request.POST.get("confirm_password")
 
        # Validate password match
        if password != confirm_password:
            messages.error(request, "Passwords do not match.")
            return redirect("register")
 
        # Check existing user
        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already exists.")
            return redirect("register")
 
        if User.objects.filter(email=email).exists():
            messages.error(request, "Email already exists.")
            return redirect("register")
 
        # Generate verification code
        code = str(random.randint(100000, 999999))
 
        # Save temporary user data in session
        request.session["verification_code"] = code
        request.session["temp_user"] = {
            "fullname": fullname,
            "username": username,
            "email": email,
            "password": password,
        }
 
        try:
            # SendGrid email setup
            mail = EmailMultiAlternatives(
                subject="Email Verification - SmartSpend X",
                body=" ",  # body can be blank, template handles content
                from_email=settings.DEFAULT_FROM_EMAIL,
                to=[email],
            )
 
            mail.content_subtype = "html"
 
            # Use your published SendGrid dynamic template ID
            mail.template_id = "d-88d3829c61fe4d0f9a37ee5e658da67d"
 
            # Pass dynamic data to template
            mail.dynamic_template_data = {
                "verification_code": code,
                "first_name": fullname,
                "current_year": datetime.datetime.now().year,
            }
 
            mail.send(fail_silently=False)
 
            return redirect("verify_email")
 
        except Exception as e:
            print("================ SENDGRID ERROR ================")
            print(str(e))
            print("================================================")
            messages.error(request, "An error occurred while sending the verification code. Please try again.")
            return redirect("register")
 
    return render(request, "register.html")

def verify_email_view(request):
    if request.method == "POST":
        entered_code = request.POST.get("code")
        session_code = request.session.get("verification_code")
        user_data = request.session.get("temp_user")
 
        # --- VERIFICATION DEBUG PRINTS ---
        print("=== VERIFICATION PROCESS STARTED ===")
        print(f"Entered Code from HTML: {entered_code}")
        print(f"Session Stored Code   : {session_code}")
        print(f"Session User Payload  : {user_data}")
        print("====================================")

        # Check if code matches and user data exists
        if entered_code == session_code and user_data:
            try:
                print("Success: Codes match! Committing user records to SQLite...")
                # Create the user account
                user = User.objects.create_user(
                    username=user_data["username"],
                    email=user_data["email"],
                    password=user_data["password"],
                )
 
                # Save first and last name if provided
                fullname = user_data.get("fullname", "")
                if fullname:
                    names = fullname.split(" ", 1)
                    user.first_name = names[0]
                    if len(names) > 1:
                        user.last_name = names[1]
                    user.save()
 
                # Clear session data now that commit is complete
                del request.session["verification_code"]
                del request.session["temp_user"]
 
                print("Database Success: User account successfully generated in SQL!")
                messages.success(request, "Account created successfully. Please log in.")
                return redirect("login")
                
            except Exception as sql_error:
                print("================ DATABASE CRITICAL ERROR ================")
                print(str(sql_error))
                print("=========================================================")
                messages.error(request, "Critical database writing error occurred.")
                return redirect("verify_email")
        else:
            print("Verification Failed: Mismatched code entries or session timed out.")
            messages.error(request, "Invalid verification code.")
            return redirect("verify_email")
 
    return render(request, "verify-email.html")

def forgot_password_view(request):
    return render(request, "forgot-password.html")

def reset_password_view(request):
    return render(request, "reset-password.html")

def success_view(request):
    return render(request, "success.html")

@login_required
def dashboard(request):
    expenses = Expense.objects.filter(user=request.user).order_by("-date")[:5]
    bills = BillReminder.objects.filter(user=request.user, is_paid=False).order_by("due_date")[:3]
    total_expenses = Expense.objects.filter(user=request.user).aggregate(total=Sum("amount"))["total"] or 0
    total_budget = Budget.objects.filter(user=request.user).aggregate(total=Sum("budget_amount"))["total"] or 0
    
    category_data = (
        Expense.objects.filter(user=request.user)
        .values('category')
        .annotate(total=Sum('amount'))
        .order_by('category')
    )
    chart_labels = [item['category'].capitalize() for item in category_data]
    chart_values = [float(item['total']) for item in category_data]
    
    return render(request, "dashboard.html", {
        "expenses": expenses,
        "bills": bills,
        "total_budget": total_budget,
        "total_expenses": total_expenses,
        "currency": get_currency_symbol(request.user),
        "chart_labels": chart_labels,
        "chart_values": chart_values,
    })

@login_required
def expenses_view(request):
    if request.method == "POST":
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
def delete_expense(request, expense_id):
    expense = get_object_or_404(Expense, id=expense_id, user=request.user)
    expense.delete()
    return redirect("expenses")

@login_required
def bill_reminder_view(request):
    if request.method == "POST":
        try:
            BillReminder.objects.create(
                name=request.POST.get("name"),
                amount=request.POST.get("amount"),
                due_date=request.POST.get("due_date"),
                user=request.user
            )
            return redirect("bill_reminder")
        except Exception as e:
            bills = BillReminder.objects.filter(user=request.user).order_by("due_date")
            unpaid_bills = bills.filter(is_paid=False)
            return render(request, "billReminder.html", {
                "bills": bills,
                "upcoming_count": unpaid_bills.count(),
                "total_needed": unpaid_bills.aggregate(total=Sum("amount"))["total"] or 0,
                "next_bill": unpaid_bills.first(),
                "currency": get_currency_symbol(request.user),
                "error": "Invalid date. Please use the date picker or format YYYY-MM-DD.",
            })

    bills = BillReminder.objects.filter(user=request.user).order_by("due_date")
    unpaid_bills = bills.filter(is_paid=False)
    return render(request, "billReminder.html", {
        "bills": bills,
        "upcoming_count": unpaid_bills.count(),
        "total_needed": unpaid_bills.aggregate(total=Sum("amount"))["total"] or 0,
        "next_bill": unpaid_bills.first(),
        "currency": get_currency_symbol(request.user),
    })

@login_required
def monthly_report_view(request):
    expenses = Expense.objects.filter(user=request.user)
    total_spent = expenses.aggregate(total=Sum("amount"))["total"] or 0
    biggest_category = (
        expenses.values("category")
        .annotate(total=Sum("amount"))
        .order_by("-total")
        .first()
    )
    return render(request, "monthlyReport.html", {
        "expenses": expenses,
        "total_spent": total_spent,
        "biggest_category": biggest_category,
        "currency": get_currency_symbol(request.user),
    })

@login_required
def budget_planning_view(request):
    if request.method == "POST":
        Budget.objects.create(
            income=request.POST.get("income"),
            category=request.POST.get("category"),
            budget_amount=request.POST.get("budget"),
            user=request.user
        )
        return redirect("budget_planning")

    budgets = Budget.objects.filter(user=request.user)
    return render(request, "budgetPlanning.html", {"budgets": budgets})

@login_required
def profile_view(request):
    expenses = Expense.objects.filter(user=request.user).order_by("-date")[:4]
    total_expenses = Expense.objects.filter(user=request.user).aggregate(total=Sum("amount"))["total"] or 0
    return render(request, "profile.html", {
        "expenses": expenses,
        "total_expenses": total_expenses,
        "currency": get_currency_symbol(request.user),
    })

@login_required
def settings_view(request):
    profile, _ = UserProfile.objects.get_or_create(user=request.user)

    if request.method == "POST":
        action = request.POST.get("action")

        if action == "update_info":
            username = request.POST.get("username")
            email = request.POST.get("email")
            currency = request.POST.get("currency")
            language = request.POST.get("language")

            request.user.username = username
            request.user.email = email
            request.user.save()

            profile.currency = currency
            profile.language = language
            profile.save()

            messages.success(request, "Settings saved successfully.")
            return redirect("settings")

        if action == "change_password":
            current_password = request.POST.get("current_password")
            new_password = request.POST.get("new_password")

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

def about_us_view(request):
    return render(request, "about_us.html")