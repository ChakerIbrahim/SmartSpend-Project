from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    CURRENCY_CHOICES = [
        ('USD', 'USD $'),
        ('ILS', 'ILS ₪'),
        ('EUR', 'Euro €'),
    ]
    LANGUAGE_CHOICES = [
        ('english', 'English'),
        ('arabic', 'Arabic'),
        ('spanish', 'Spanish'),
    ]

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    currency = models.CharField(max_length=10, choices=CURRENCY_CHOICES, default='USD')
    language = models.CharField(max_length=20, choices=LANGUAGE_CHOICES, default='english')

    def __str__(self):
        return f"{self.user.username}'s profile"

class Expense(models.Model):
    CATEGORY_CHOICES = [
        ("Food", "Food"),
        ("Transportation", "Transportation"),
        ("Entertainment", "Entertainment"),
        ("Bills", "Bills"),
        ("Other", "Other"),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    title = models.CharField(max_length=100)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES)
    date = models.DateField()

    def __str__(self):
        return self.title


class BillReminder(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=100)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    due_date = models.DateField()
    is_paid = models.BooleanField(default=False)

    def __str__(self):
        return self.name


class Budget(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    income = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.CharField(max_length=100)
    budget_amount = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.category