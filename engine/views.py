from django.http import HttpResponse
from django.template import loader
from .models import LocomSTRUCT, XapSTRUCT_TGxp, XapSTRUCT_RCxp


def report(request):
    latest_question_list = LocomSTRUCT.objects.order_by('LocmTyp')[:5]
    template = loader.get_template('engine\\list.html')
    context = {
        'latest_question_list': latest_question_list,
    }
    return HttpResponse(template.render(context, request))


def detail(request, locomot_id):
    l = LocomSTRUCT.objects.get(id=locomot_id)
    template = loader.get_template('engine\\detail.html')
    context = {
        'locomotive': l,
    }
    return HttpResponse(template.render(context, request))


def main_spec_resist_move(request, locomot_id):
    l = LocomSTRUCT.objects.get(id=locomot_id)
    template = loader.get_template('engine\\main_spec_resist_move.html')
    context = {
        'wo': l.LocWo,
    }
    return HttpResponse(template.render(context, request))


def tract_mod(request, locomot_id):
    l = LocomSTRUCT.objects.get(id=locomot_id)
    x = l.xapstruct_tgxp_set.all()
    template = loader.get_template('engine\\tract_mod.html')
    context = {
        'xap': x,
    }
    return HttpResponse(template.render(context, request))


def tract_mod_xap(request, xap_id):
    x = XapSTRUCT_TGxp.objects.get(id=xap_id)
    template = loader.get_template('engine\\tract_mod_xap.html')
    context = {
        'xap': x,
    }
    return HttpResponse(template.render(context, request))


def regenerat_braking(request, locomot_id):
    l = LocomSTRUCT.objects.get(id=locomot_id)
    x = l.xapstruct_rcxp_set.all()
    template = loader.get_template('engine\\regenerat_braking.html')
    context = {
        'xap': x,
    }
    return HttpResponse(template.render(context, request))


def regenerat_braking_xap(request, xap_id):
    x = XapSTRUCT_RCxp.objects.get(id=xap_id)
    template = loader.get_template('engine\\regenerat_braking_xap.html')
    context = {
        'xap': x,
    }
    return HttpResponse(template.render(context, request))


def therm_engine(request, locomot_id):
    l = LocomSTRUCT.objects.get(id=locomot_id)
    t = l.Tau8
    template = loader.get_template('engine\\therm_engine.html')
    context = {
        'locomotive': l,
        'tau': t,
    }
    return HttpResponse(template.render(context, request))

