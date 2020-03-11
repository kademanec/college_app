# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
STREAM_CHOICES = (
    ('Computer Science', 'CSE'),
    ('Electronics', 'EC'),
    ('Mechanical', 'ME'),
)

class Update_profile(models.Model):
    first_name = models.CharField(max_length=256,unique=True)
    last_name=models.CharField(max_length=256)
    phone_no=models.IntegerField()
    stream=models.CharField(max_length=256,choices=STREAM_CHOICES)
    college=models.CharField(max_length=256)
    YOP=models.IntegerField()

    def __str__(self):
        return self.first_name

class Sign_up(models.Model):
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=256)
