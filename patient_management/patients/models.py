from django.db import models
# from patients.models import Patient
class Patient(models.Model):
    GENDER_CHOICES = [
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other'),
    ]

    full_name = models.CharField(max_length=100)
    age = models.IntegerField()
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    insurance_provider = models.CharField(max_length=100)
    policy_number = models.CharField(max_length=100)

    def __str__(self):
        return self.full_name
