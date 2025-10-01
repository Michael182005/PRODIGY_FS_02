from django.db import models
from django.core.validators import RegexValidator, MinValueValidator
from django.utils import timezone

class Employee(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    phone_regex = RegexValidator(
        regex=r'^\+?1?\d{9,15}$',
        message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed."
    )
    phone = models.CharField(validators=[phone_regex], max_length=17, blank=True)
    salary = models.DecimalField(max_digits=10, decimal_places=2, validators=[MinValueValidator(0.01)])
    hire_date = models.DateField(default=timezone.now)

    def __str__(self):
        return self.name
