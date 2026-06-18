from django.db import models
from datetime import date


class ShowManager(models.Manager):
    def show_validator(self, post_data):
        errors = {}
        # Title validation
        if len(post_data["title"]) < 3:
            errors["title"] = "Title should be at least 3 characters"

            # Network validation
        if len(post_data["network"]) < 4:
            errors["network"] = "Network should be at least 4 characters"
            
            # Release date validation
        if post_data['release_date'] == "":
            errors['release_date'] = "Release date is required"
        elif post_data['release_date'] > str(date.today()):
            errors['release_date'] = "Release date must be in the past"


# Create Show Table
class Show(models.Model):
    title = models.CharField(max_length=255)
    network = models.CharField(max_length=255)
    release_date = models.DateField()
    desc = models.TextField(default="")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = ShowManager()
