from django.db import models
from django.utils import timezone
from django.core.validators import MinValueValidator, MaxValueValidator

class Reviews(models.Model):
    lord = models.ForeignKey('landlord.Landlord', on_delete=models.CASCADE)
    tenant = models.CharField(max_length=50)
    rating = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)], default=1)
    comment = models.TextField()
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.tenant} - {self.lord} - {self.rating}"