from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    is_staff = models.BooleanField('Is staff', default=False)
    is_patient = models.BooleanField('Is patient',default=True,)


class Doctor(models.Model):
    doctor_name = models.CharField(max_length=100)
    specialization = models.CharField(max_length=25)

    def __str__(self):
        return f'{self.doctor_name}, {self.specialization}'


class Appointment(models.Model):
    patient_name = models.ForeignKey(User, on_delete=models.CASCADE)
    problems = models.TextField()
    doctors_wanted = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    CHOICES = (
        ('Approved', 'Approved'),
        ('Denied', 'Denied'),
    )
    status = models.CharField(max_length=50, default='pending',choices=CHOICES )
    date = models.DateField(null=True, default=None)




