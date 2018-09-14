from django.shortcuts import render, HttpResponse, redirect
from Fm import models

Create your views here.


def index(request):

    return HttpResponse("ok")