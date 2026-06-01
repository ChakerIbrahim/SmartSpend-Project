from django.db import models

# Create your models here.
class Dojo(models.Model):
    name = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    state = models.CharField(max_length=2)
    desc = models.TextField(default="old dojo")
    
    def __str__(self):
        return self.name
    
# "related_name is used to define the reverse access name for related objects.
# For example, instead of user.project_set.all(), I can use user.created_projects.all().

# on_delete specifies what happens to related records when the parent record is deleted.
# The most common option is CASCADE, which deletes all related records automatically." 

class Ninja(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    dojo = models.ForeignKey(Dojo, related_name="ninjas",on_delete=models.CASCADE)
    
    def __str__(self):
        return f"{self.first_name} {self.last_name}"
