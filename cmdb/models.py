from django.db import models

# Create your models here.

class UserInfo(models.Model):  #UserInfo类需要继承models.Model类
    user = models.CharField(max_length=32)
    pwd = models.CharField(max_length=32)

class UserDate(models.Model):
    year = models.CharField(max_length=32)
    month = models.CharField(max_length=32)
    day = models.CharField(max_length=32)