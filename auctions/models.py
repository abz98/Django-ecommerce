from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    pass

class Listing(models.Model):
    title=models.CharField(max_length=64)
    describe=models.CharField(max_length=200)
    date=models.DateTimeField(blank=True, null=True, verbose_name='last updated',auto_now=True)
    bid=models.IntegerField(null=True)

    def __str__(self):
        return f"{self.id}: {self.title} {self.bid} {self.describe} {self.date}"
