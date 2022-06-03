# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.db import models
from django.contrib.auth.models import User

# Create your models here.



class Image(models.Model):
    name = models.CharField(max_length=100)
    app = models.CharField(max_length=100,null=True)
    tag = models.CharField(max_length=100,null=True )
    link = models.CharField(max_length=100,null=True )

class RunningApp(models.Model):
    name = models.CharField(max_length=100)
    image = models.ForeignKey(Image ,on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE,related_name='runningapps')
    link = models.CharField(max_length=100,null=True)
    state = models.CharField(max_length=100,default="pending")
    port = models.IntegerField(null=True)
    

class Volume(models.Model):
    name = models.CharField(max_length=100)
    user = models.ForeignKey(User, on_delete=models.CASCADE ,related_name='volumes')
    link = models.CharField(max_length=100,null=True)
    

