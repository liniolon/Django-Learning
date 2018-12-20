from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Expense(models.Model):
    title = models.CharField(max_length=255)
    date  = models.DateTimeField()
    amount = models.BigIntegerField()
    user = models.ForeignKey(User)

    def __str__(self):
        return "%s" % self.title


class Income(models.Model):
    title = models.CharField(max_length=255)
    date = models.DateTimeField()
    amount = models.BigIntegerField()
    user = models.ForeignKey(User)

    def __str__(self):
        return "{} - {}".format(self.title, self.amount)
