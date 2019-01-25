from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    context = {}
    return render(request, 'veip\\index.html', context)

def vivod(request):
    radius = request.POST['radius']

    return HttpResponse("Radius is %s." % radius)