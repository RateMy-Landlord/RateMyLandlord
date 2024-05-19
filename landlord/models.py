from django.db import models


class Landlord(models.Model):
    name = models.CharField(max_length=50)
    address = models.TextField()

    def __str__(self):
        return self.name