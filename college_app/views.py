# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def index(request):
    return render(request,"college_app/index.html")

def signup(request):
    return render(request,"college_app/signup.html")
