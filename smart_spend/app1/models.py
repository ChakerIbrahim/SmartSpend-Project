from django.db import models
from django.contrib.auth.models import User , UserManager
import re

class CustomUserManager(UserManager):
    def register_validator(self, postData):
        errors = {}
 
        name_regex = re.compile(r'^[A-Za-z ]+$')
        username_regex = re.compile(r'^[A-Za-z0-9_]+$')
        email_regex = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
 
        fullname = postData.get('fullname', '').strip()
        username = postData.get('username', '').strip()
        email = postData.get('email', '').strip()
        password = postData.get('password', '')
        confirm_password = postData.get('confirm_password', '')
 
        # Fullname
        if len(fullname) < 2:
            errors['fullname'] = "Full name must be at least 2 characters."
        elif not name_regex.match(fullname):
            errors['fullname'] = "Full name must contain letters and spaces only."
 
        # Username
        if len(username) < 3:
            errors['username'] = "Username must be at least 3 characters."
        elif not username_regex.match(username):
            errors['username'] = "Username can only contain letters, numbers, and underscores."
        elif self.filter(username__iexact=username).exists():
            errors['username'] = "Username already exists."
 
        # Email
        if not email_regex.match(email):
            errors['email'] = "Invalid email address."
        elif self.filter(email__iexact=email).exists():
            errors['email'] = "Email already exists."
 
        # Password
        if len(password) < 8:
            errors['password'] = "Password must be at least 8 characters."
 
        if password != confirm_password:
            errors['confirm_password'] = "Passwords do not match."
 
        return errors
 
    def update_info_validator(self, postData, current_user):
        errors = {}
 
        email_regex = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
 
        username = postData.get('username', '').strip()
        email = postData.get('email', '').strip()
 
        if not username:
            errors['username'] = "Username cannot be blank."
        elif self.filter(username__iexact=username).exclude(id=current_user.id).exists():
            errors['username'] = "This username is already taken."
 
        if not email_regex.match(email):
            errors['email'] = "Invalid email address."
        elif self.filter(email__iexact=email).exclude(id=current_user.id).exists():
            errors['email'] = "This email is already in use."
 
        return errors
 
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

# ---- ADDED THIS MODEL TO FIX THE IMPORT ERROR ----
class SupportMessage(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=200, null=True, blank=True)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Message from {self.name} - {self.email}"