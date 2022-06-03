# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.contrib import admin

from apps.home.models import Image, RunningApp, Volume

# Register your models here.
admin.site.register(Image)
admin.site.register(RunningApp)
admin.site.register(Volume)
