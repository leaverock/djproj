from django.http import HttpResponse
from django.shortcuts import render
from .run.jan25_19.veip_21jan19.init__ import go


def index(request):
    context = {}
    return render(request, 'veip\\index.html', context)


def vivod(request):
    sp = request.POST['speed']
    rad = request.POST['radius']

    go(9, 16, 1, 1, 0, 1, float(sp), float(rad), 0.8, 0.05, 556, 1900.0, 0.007, 1.0, 0.8)

    with open(r'C:\work\veip\djproj\veip\run\vivod', 'r') as file:
        text = file.read()

    return HttpResponse(f"<pre>{text}</pre>")