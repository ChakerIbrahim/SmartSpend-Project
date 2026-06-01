from django.db import models
import re
from datetime import date


class UserManager(models.Manager):
    def register_validator(self, post_data):
        errors = {}

        if len(post_data['first_name']) < 2:
            errors['first_name'] = "First name must be at least 2 characters"

        if len(post_data['last_name']) < 2:
            errors['last_name'] = "Last name must be at least 2 characters"

        email_regex = r'^[\w\.-]+@[\w\.-]+\.\w+$'
        if not re.match(email_regex, post_data['email']):
            errors['email'] = "Invalid email"

        if len(post_data['password']) < 8:
            errors['password'] = "Password must be at least 8 characters"

        if post_data['password'] != post_data['confirm_password']:
            errors['confirm_password'] = "Passwords do not match"

        return errors

    def login_validator(self, post_data):
        errors = {}

        if len(post_data['email']) == 0:
            errors['email'] = "Email is required"

        if len(post_data['password']) == 0:
            errors['password'] = "Password is required"

        return errors


class ProjectManager(models.Manager):
    def project_validator(self, post_data):
        errors = {}

        if len(post_data['title']) < 3:
            errors['title'] = "Title must be at least 3 characters"

        if len(post_data['description']) < 10:
            errors['description'] = "Description must be at least 10 characters"

        if post_data['end_date'] == "":
            errors['end_date'] = "End date is required"

        elif post_data['end_date'] < str(date.today()):
            errors['end_date'] = "End date cannot be in the past"

        return errors


class User(models.Model):
    first_name = models.CharField(max_length=45)
    last_name = models.CharField(max_length=45)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=255)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = UserManager()


class Project(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    end_date = models.DateField()

    created_by = models.ForeignKey(
        User,
        related_name="created_projects",
        on_delete=models.CASCADE
    )

    joined_users = models.ManyToManyField(
        User,
        related_name="joined_projects",
        blank=True
    )

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = ProjectManager()
