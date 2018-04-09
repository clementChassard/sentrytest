# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse, Http404
from django.shortcuts import redirect, render, reverse, get_object_or_404
from django.contrib.auth import login, authenticate
from .models import client

def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")


def login(request):
    render(request,'monapp/login.html')


##si form valide et submit bas redirect to monapp/moncompte
def moncompte(request, client_id):
    try:
        question = client.objects.get(pk=client_id)
    except client.DoesNotExist:
        raise Http404("client does not exist")
    return render(request, 'uneApp/moncompte.html', {'client': client})

def register(request):
    return render(request, 'uneApp/register.html')

def brokenpage(request):
    return render(request, 'uneApp/brokenpage.html')



