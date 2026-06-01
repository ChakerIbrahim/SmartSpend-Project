from django.db import models


# Manager responsible for dojo-related database operations
class DojoManager(models.Manager):

    # Create a new dojo using form data
    def create_dojo(self, post_data):
        return self.create(
            name=post_data["name"],
            city=post_data["city"],
            state=post_data["state"]
        )


# Manager responsible for ninja-related database operations
class NinjaManager(models.Manager):

    # Create a new ninja and assign it to a dojo
    def create_ninja(self, post_data):

        # Get the selected dojo from the dropdown
        dojo = Dojo.objects.get(id=post_data["dojo_id"])

        # Create the ninja
        return self.create(
            first_name=post_data["first_name"],
            last_name=post_data["last_name"],
            dojo=dojo
        )


class Dojo(models.Model):

    # Database fields
    name = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    state = models.CharField(max_length=2)

    # Attach custom manager
    objects = DojoManager()


class Ninja(models.Model):

    # Database fields
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)

    # One dojo can have many ninjas
    dojo = models.ForeignKey(
        Dojo,
        related_name="ninjas",
        on_delete=models.CASCADE
    )

    # Attach custom manager
    objects = NinjaManager()