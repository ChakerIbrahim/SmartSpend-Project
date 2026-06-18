from django.db import models

# Create your models here.

# Dojo Table
class Dojo(models.Model):
    name = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    state = models.CharField(max_length=255)

    def __str__(self):
        return self.name


# Ninja Table
class Ninja(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)

    # One Dojo can have many Ninjas
    dojo = models.ForeignKey(
        Dojo,
        related_name="ninjas",
        on_delete=models.CASCADE
    )

    def __str__(self):
        return f"{self.first_name} {self.last_name}"