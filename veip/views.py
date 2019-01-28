from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    context = {}
    return render(request, 'veip\\index.html', context)

def vivod(request):
    sp = request.POST['speed']
    rad = request.POST['radius']
    with open(r'C:\Users\yaroschuk.denis\Desktop\ФОРП СЕНДЕРКИН.txt', 'r') as file:
        text = file.read()

    return HttpResponse(text)#"скорость: %.3f is %.3f." % (float(sp), float(rad)))