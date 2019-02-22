import numpy as np
from django.contrib.contenttypes.models import ContentType
from django.core import serializers
from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader

from .models import CategSTRUCT, StansSTRUCT, UchSTRUCT, Audit


def report(request):
    uch_list = UchSTRUCT.objects.order_by('UchNam')[:10]
    template = loader.get_template('track/list.html')
    context = {
        'uch': uch_list,
    }
    return HttpResponse(template.render(context, request))


def detail(request, uch_id):
    u = UchSTRUCT.objects.get(id=uch_id)
    x = np.array(u.stansstruct_set.all())
    prot = f'km {x[0].Kml[0][0]} - {x[-1].Kml[0][0]} (протяженность {round(abs(x[-1].Kml[0][0] - x[0].Kml[0][0]), 3)})'
    template = loader.get_template('track/detail.html')
    context = {
        'uch': u,
        'prot': prot,
        'odd_way_0': x[0].Nam,
        'odd_way_1': x[u.mStan].Nam,
        'odd_way_selected_is_last': bool(u.NechSt)
    }
    return HttpResponse(template.render(context, request))


def sep_points(request, uch_id):
    u = UchSTRUCT.objects.get(id=uch_id)
    x = u.stansstruct_set.all()
    template = loader.get_template('track/sep_points.html')
    context = {
        'stations': x,
    }
    return HttpResponse(template.render(context, request))


def api_track(request, KodDor, KodUch, fields):
    s = ''
    single = len(str(fields).split('+')) == 1  # флаг "один параметр"
    for field in str(fields).split('+'):
        if field == 'stans':
            x = UchSTRUCT.objects.get(
                KodDor=KodDor, KodUch=KodUch).stansstruct_set.all()
            for a in x:
                s += f'{a}\n'
        elif field == 'uch_list':
            x = UchSTRUCT.objects.all()
            for a in x:
                s += f'{a.UchNam}_+_{a.KodDor}_+_{a.KodUch}\n'
        elif field == 'uch':
            x = UchSTRUCT.objects.get(KodDor=KodDor, KodUch=KodUch).__dict__
            keys = list(x.keys())
            values = list(x.values())
            for a in range(len(keys)):
                s += f'{keys[a]}={values[a]}\n'
        else:
            y = UchSTRUCT.objects.get(
                KodDor=KodDor, KodUch=KodUch).__dict__  # словарь параметров
            s += y[field] + '\n'
        # if not single:
        #    s += '\n=====-=-=-=====\n\n'

    return HttpResponse(s)


def ctgs_types_train(request, uch_id):
    u = UchSTRUCT.objects.get(id=uch_id)
    x = u.categstruct_set.all()
    template = loader.get_template('track/ctgs_types_train.html')
    gPutStr = ''
    if u.mGput == 0:
        gPutStr = '1'
    elif u.mGput == 1:
        gPutStr = '1; 2'
    elif u.mGput == 2:
        gPutStr = '1...3'
    elif u.mGput == 3:
        gPutStr = '1...4'
    context = {
        'categs': x,
        'mGput': gPutStr,
    }
    return HttpResponse(template.render(context, request))


def speed_limits(request, uch_id):
    u = UchSTRUCT.objects.get(id=uch_id)
    v = u.Vorp
    template = loader.get_template('track/speed_limits.html')
    context = {
        'vogr': v,
    }
    return HttpResponse(template.render(context, request))


def save_uch(request, uch_id):
    u = UchSTRUCT.objects.get(id=uch_id)
    x = np.array(u.stansstruct_set.all())
    prot = f'km {x[0].Kml[0][0]} - {x[-1].Kml[0][0]} (протяженность {round(abs(x[-1].Kml[0][0] - x[0].Kml[0][0]), 3)})'
    context = {
        'uch': u,
        'prot': prot,
        'odd_way_0': x[0].Nam,
        'odd_way_1': x[u.mStan].Nam,
        'odd_way_selected_is_last': bool(u.NechSt)
    }
    if request.method != "POST":
        return render(request, 'track/detail.html', context)
    u.DorNam = request.POST['road-input']
    u.Comment = request.POST['comment-input']
    u.mGput = int(request.POST['put-count-select'])
    u.Difl = bool(request.POST.get('difference_peregon', False))
    u.NechSt = int(request.POST.get('odd-way-select'))
    u.save(force_update=True)
    context['just_saved'] = True
    context['odd_way_selected_is_last'] = bool(u.NechSt)
    if request.user.is_authenticated:
        Audit(
            user=request.user,
            object_id=u,
            object_repr='',
            change_message='Сохранен участок',
            action="U",
            user_ip=request.META['REMOTE_ADDR']
        ).save(force_insert=True)
    else:
        return HttpResponse(f"Вы не аутентифицированы")
        # Do something for anonymous users.
    return render(request, 'track/detail.html', context)


def auditPage(request):
    a = Audit.objects.all()
    context = {
        'au': a
    }
    return render(request, 'track/audit.html', context)


def new_uch_click(request):
    u = UchSTRUCT(
        UchNam="0км - 0км"
    )
    context = {
        'uch': u,
        'prot': "0км",
        'odd_way_0': "",
        'odd_way_1': "",
    }
    return render(request, 'track/create_uch.html', context)

def create_uch(request):
    if request.method == "POST":
        u = UchSTRUCT(
            DorNam=request.POST['road-input'],
            Comment=request.POST['comment-input'],
        )
        print(request.POST.getlist('koordFact[]'))
        context = {
            'uch': u,
        }
        return render(request, 'track/detail.html', context)
    return HttpResponse("А ты чего хотел?")
