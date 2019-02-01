from django.http import HttpResponse
from django.shortcuts import render
from .run.jan25_19.veip_21jan19.go import go, work_dir


def index(request):
    context = {}
    return render(request, 'veip\\index.html', context)


def vivod(request):
    sp = float(request.POST['speed'])
    rad = float(request.POST['radius'])

    text = go(9, 16, 1, 1, 0, 1, sp, rad, 0.8, 0.05, 556, 1900.0, 0.007, 1.0, 0.8)
    #with open(r'C:\work\veip\djproj\veip\run\vivod', 'r') as file:

    return HttpResponse(f"<pre>{text}</pre>")