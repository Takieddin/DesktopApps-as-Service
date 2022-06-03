# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from random import randint
from xmlrpc.client import SERVER_ERROR
from django import template
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import redirect
from django.template import loader
from django.urls import reverse

from django.contrib.auth.models import User


from apps.home.models import Image, RunningApp
from apps.home.kubeclient import create_service, create_deployment,\
    delete_service, delete_deployment

# TODO get server ip using env vars
SERVER_IP = 'http://192.168.43.240'


@login_required(login_url="/login/")
def index(request):
    context = {'segment': 'index'}

    html_template = loader.get_template('home/index.html')
    return HttpResponse(html_template.render(context, request))

@login_required(login_url="/login/")
def images(request):
    images=Image.objects.all()
    context = {}
    context['images']=images
    html_template = loader.get_template('home/images-table.html')


    return HttpResponse(html_template.render(context, request))
@login_required(login_url="/login/")
def applications(request):
    apps=RunningApp.objects.filter(user=request.user).all()
    context = {}
    context['apps']=apps
    images=Image.objects.all()
    context['images']=images    

    html_template = loader.get_template('home/running-apps-table.html')


    return HttpResponse(html_template.render(context, request))
@login_required(login_url="/login/")
def launchapp(request):
    data=request.POST.dict()['imageIdName'].split('+')
    image_id=data[0]
    image = Image.objects.get(pk=image_id)
    image_name=data[1]
    image_app=data[2]
    user_id=request.user.pk
    user = User.objects.get(pk=user_id)

    print('image_name')
    print(image_name)
    
    app=RunningApp.objects.filter(user=request.user,image=image_id).first()
    if app is None:
        ports=RunningApp.objects.values_list('port', flat=True)

        print('none')
        print(type(ports))
        port = randint(30000,32768)
        while port in ports:
            port = randint(30000,32768)
        service_name = 'user-'+str(user_id)+'-image-'+str(image_id)
        print(service_name)

        svc = create_service(service_name,port)
        dep = create_deployment(service_name,image_name)
        link = SERVER_IP+':'+str(port)+'/vnc.html'
        newapp = RunningApp()
        newapp.name = image_app
        newapp.image = image
        newapp.user = user
        newapp.link = link
        newapp.state = "ready"
        newapp.port = port
        newapp.save()
    return redirect(reverse('applications'))

@login_required(login_url="/login/")
def deletechapp(request):
    image_id=int(request.POST.dict()['imageID'])
    user_id=request.user.pk    
    app=RunningApp.objects.filter(user=request.user,image=image_id).first()
    if app is not  None:

        service_name = 'user-'+str(user_id)+'-image-'+str(image_id)
        svc = delete_service(service_name)
        dep = delete_deployment(service_name)
        app.delete()
        
    return redirect(reverse('applications'))


@login_required(login_url="/login/")
def pages(request):
    context = {}
    # All resource paths end in .html.
    # Pick out the html file name from the url. And load that template.
    try:

        load_template = request.path.split('/')[-1]

        if load_template == 'admin':
            return HttpResponseRedirect(reverse('admin:index'))
        context['segment'] = load_template

        html_template = loader.get_template('home/' + load_template)
        return HttpResponse(html_template.render(context, request))

    except template.TemplateDoesNotExist:

        html_template = loader.get_template('home/page-404.html')
        return HttpResponse(html_template.render(context, request))

    except:
        html_template = loader.get_template('home/page-500.html')
        return HttpResponse(html_template.render(context, request))
