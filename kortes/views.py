from django.http import HttpResponse
from django.shortcuts import render
from django.http import HttpResponseRedirect

from .uchastk_views import *


def index(request):
    context = {}
    return render(request, 'kortes/index.html', context)
