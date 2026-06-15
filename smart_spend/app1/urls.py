from django.urls import path
from . import views

urlpatterns = [
    path("", views.landing_page, name="landing"),

    path("login/", views.login_view, name="login"),
    path("register/", views.register_view, name="register"),
    path("forgot-password/", views.forgot_password_view, name="forgot_password"),
    path("reset-password/", views.reset_password_view, name="reset_password"),
    path("verify-email/", views.verify_email_view, name="verify_email"),
    path("success/", views.success_view, name="success"),

    path("dashboard/", views.dashboard, name="dashboard"),

    path("expenses/", views.expenses_view, name="expenses"),
    path("expenses/delete/<int:expense_id>/", views.delete_expense, name="delete_expense"),
    path("expenses/all/", views.all_expenses_view, name="all_expenses"),
    path("expenses/edit/<int:expense_id>/", views.edit_expense_view, name="edit_expense"),

    path("bill-reminder/", views.bill_reminder_view, name="bill_reminder"),
    path("monthly-report/", views.monthly_report_view, name="monthly_report"),
    path("budget-planning/", views.budget_planning_view, name="budget_planning"),
    path("ai-analysis/", views.ai_analysis_view, name="ai_analysis"),
    path("profile/", views.profile_view, name="profile"),
    path("settings/", views.settings_view, name="settings"),
    path("about-us/", views.about_us_view, name="about_us"),
    path('budget/update/', views.update_budget, name='update_budget'),
]