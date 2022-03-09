from asyncio import AbstractServer
from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class RolyChoices(models.TextChoices):
    simple = 1, 'simple user'
    friend = 2, 'frined'

class Account(AbstractUser):
    roly = models.CharField(choices=RolyChoices.choices, max_length=30)


    @property
    def is_friend(self):
        return self.roly == '2'


    class Meta(AbstractUser.Meta):
        swappable = 'AUTH_USER_MODEL'
