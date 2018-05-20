from django.http import HttpResponse
from django.template import loader
from .models import UchSTRUCT, StansSTRUCT, CategSTRUCT


def report(request):
    uch_list = UchSTRUCT.objects.order_by('UchNam')[:10]
    template = loader.get_template('track\\report.html')
    context = {
        'uch': uch_list,
    }
    return HttpResponse(template.render(context, request))


def detail(request, uch_id):
    u = UchSTRUCT.objects.get(id=uch_id)
    template = loader.get_template('track\\detail.html')
    context = {
        'uch': u,
    }
    return HttpResponse(template.render(context, request))


def sep_points(request, uch_id):
    u = UchSTRUCT.objects.get(id=uch_id)
    x = u.stansstruct_set.all()
    template = loader.get_template('track\\sep_points.html')
    context = {
        'stations': x,
    }
    return HttpResponse(template.render(context, request))


def ctgs_types_train(request, uch_id):
    u = UchSTRUCT.objects.get(id=uch_id)
    x = u.categstruct_set.all()
    template = loader.get_template('track\\ctgs_types_train.html')
    context = {
        'categs': x,
    }
    return HttpResponse(template.render(context, request))


def speed_limits(request, uch_id):
    u = UchSTRUCT.objects.get(id=uch_id)
    v = u.Vorp
    template = loader.get_template('track\\speed_limits.html')
    context = {
        'vogr': v,
    }
    return HttpResponse(template.render(context, request))
