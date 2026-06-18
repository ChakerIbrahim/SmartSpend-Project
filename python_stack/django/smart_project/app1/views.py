from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, logout, authenticate,update_session_auth_hash
from django.contrib.auth.models import User
from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404
from django.db.models import Sum
from .models import *


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

        if password != confirm_password:
            messages.error(request, "Passwords do not match")
            return redirect("register")

        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already exists")
            return redirect("register")

        if User.objects.filter(email=email).exists():
            messages.error(request, "Email already exists")
            return redirect("register")

        user = User.objects.create_user(
            username=username,
            email=email,
            password=password
        )

        if fullname:
            names = fullname.split(" ", 1)
            user.first_name = names[0]
            if len(names) > 1:
                user.last_name = names[1]
            user.save()

        return redirect("success")

    return render(request, "register.html")


def forgot_password_view(request):
    return render(request, "forgot-password.html")


def reset_password_view(request):
    return render(request, "reset-password.html")


def verify_email_view(request):
    return render(request, "verify-email.html")


def success_view(request):
    return render(request, "success.html")


@login_required
def dashboard(request):
    expenses = Expense.objects.filter(user=request.user).order_by("-date")[:5]
    bills = BillReminder.objects.filter(user=request.user, is_paid=False).order_by("due_date")[:3]
    total_expenses = Expense.objects.filter(user=request.user).aggregate(total=Sum("amount"))["total"] or 0

    return render(request, "dashboard.html", {
        "expenses": expenses,
        "bills": bills,
        "total_expenses": total_expenses,
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
    return render(request, "expenses.html", {"expenses": expenses})
@login_required
def delete_expense(request, expense_id):
    expense = get_object_or_404(Expense, id=expense_id, user=request.user)
    expense.delete()
    return redirect("expenses")

def bill_reminder_view(request):
    if request.method == "POST":
        BillReminder.objects.create(
            name=request.POST.get("name"),
            amount=request.POST.get("amount"),
            due_date=request.POST.get("due_date"),
            user=request.user if request.user.is_authenticated else None
        )
        return redirect("bill_reminder")

    bills = BillReminder.objects.all().order_by("due_date")
    unpaid_bills = bills.filter(is_paid=False)

    return render(request, "billReminder.html", {
        "bills": bills,
        "upcoming_count": unpaid_bills.count(),
        "total_needed": unpaid_bills.aggregate(total=Sum("amount"))["total"] or 0,
        "next_bill": unpaid_bills.first(),
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
    })


def budget_planning_view(request):
    if request.method == "POST":
        Budget.objects.create(
            income=request.POST.get("income"),
            category=request.POST.get("category"),
            budget_amount=request.POST.get("budget"),
            user=request.user if request.user.is_authenticated else None
        )
        return redirect("budget_planning")

    budgets = Budget.objects.all()
    return render(request, "budgetPlanning.html", {"budgets": budgets})


def profile_view(request):
    return render(request, "profile.html")

@login_required
def settings_view(request):
    if request.method == "POST":
        action = request.POST.get("action")

        if action == "update_info":
            username = request.POST.get("username")
            email = request.POST.get("email")

            request.user.username = username
            request.user.email = email
            request.user.first_name = username
            request.user.save()

            messages.success(request, "Profile updated successfully.")
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

    return render(request, "settings.html")

def about_us_view(request):
    return render(request, "about_us.html")