from django.db import models
from datetime import datetime
from users.models import User


class Room(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return f'{self.name} '

class Message(models.Model):
    value = models.CharField(max_length=10000)
    date = models.DateTimeField(default=datetime.now, blank = True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    room = models.CharField(max_length=1000000)