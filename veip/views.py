from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    context = {}
    return render(request, 'veip\\index.html', context)

def vivod(request):
    sp = request.POST['speed']
    rad = request.POST['radius']

    return HttpResponse("скорость: %.3f is %s." % (sp, rad))