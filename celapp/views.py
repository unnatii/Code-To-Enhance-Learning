# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render,redirect
from django.http import HttpResponseRedirect
from django.http import HttpResponse

# Create your views here.

def index(request):
    return render(request,'celapp/index.html')

def board(request):
    return render(request,'celapp/board.html')

def details(request):
    return render(request,'celapp/details.html')

def tutor(request):
    return render(request,'celapp/tutor.html')    