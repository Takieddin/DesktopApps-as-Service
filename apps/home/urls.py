# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.urls import path, re_path
from apps.home import views

urlpatterns = [

    # The home page
    path('', views.index, name='home'),
    path('images', views.images, name='images'),
    path('applications', views.applications, name='applications'),
    path('launchapp', views.launchapp, name='launchapp'),
    path('deletechapp', views.deletechapp, name='deletechapp'),

    # Matches any html file
    re_path(r'^.*\.*', views.pages, name='pages'),

]
