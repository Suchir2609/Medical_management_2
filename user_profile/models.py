from django.db import models
from users.models import User


class Profile(models.Model):
    user = models.OneToOneField(User, related_name='profile', on_delete=models.CASCADE)
    gender = models.CharField(max_length=5)
    age = models.IntegerField(default=0)
    history_of_Illness = models.TextField()

    def __str__(self):
        return f'{self.user.username} Profile'


class Account(models.Model):
    patient = models.ForeignKey(User, related_name='accounts', on_delete=models.CASCADE)
    bill = models.IntegerField(default=0)
    status = models.CharField(max_length=50, default='pending')
