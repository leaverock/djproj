from django.http import HttpResponse
from django.shortcuts import render
from .run.jan25_19.veip_21jan19.go import go, work_dir

from .forms import *


def index(request):
    if request.method != 'POST':
        form = VeipInputForm()
        multiVarForm = VeipMultiVarInputForm()
    context = {
        'form': form,
        'multiVarForm': multiVarForm,
        'multiForm': GroupOfParamsForm()
    }
    return render(request, 'veip\\index.html', context)


def vivod(request):
    #train_type = 9              # float(request.POST['train_type'])
    #track_structure = 16        # float(request.POST['track_structure'])
    #horizontal_spectrum = 1     # float(request.POST['horizontal_spectrum'])
    #vertical_spectrum = 1       # float(request.POST['vertical_spectrum'])
    #ignored = 0                 # float(request.POST['ignored'])
    #vehicle_coordinates = 1     # float(request.POST['vehicle_coordinates'])
    #speed =                       float(request.POST['speed'])
    #radius =                      float(request.POST['radius'])
    #tapes_distance = 0.8        # float(request.POST['tapes_distance'])
    #superelevation = 0.05       # float(request.POST['superelevation'])
    #creep_coefficient = 556     # float(request.POST['creep_coefficient'])
    #horizontal_stiffness = 1900 # float(request.POST['horizontal_stiffness'])
    #halved_gap = 0.007          # float(request.POST['halved_gap'])
    #wheel_wear = 1.0            # float(request.POST['wheel_wear'])
    #creeps_ratio = 0.8          # float(request.POST['creeps_ratio'])
    if request.method == 'POST':
        form = VeipInputForm(request.POST)
        if form.is_valid():
            text = go(form.cleaned_data['train_type'],
                      form.cleaned_data['track_structure'],
                      form.cleaned_data['horizontal_spectrum'],
                      form.cleaned_data['vertical_spectrum'],
                      form.cleaned_data['ignored'],
                      form.cleaned_data['vehicle_coordinates'],
                      form.cleaned_data['speed'],
                      form.cleaned_data['radius'],
                      form.cleaned_data['tapes_distance'],
                      form.cleaned_data['superelevation'],
                      form.cleaned_data['creep_coefficient'],
                      form.cleaned_data['horizontal_stiffness'],
                      form.cleaned_data['halved_gap'],
                      form.cleaned_data['wheel_wear'],
                      form.cleaned_data['creeps_ratio'])
            return HttpResponse(f"<pre>{text}</pre>")
    else:
        form = VeipInputForm()
    context = {
        'form': form,
    }
    return render(request, 'veip\\index.html', context)

def multiVar(request):
    
    context = {

    }
    return render(request, 'veip\\index.html', context)


def recur(masArgs, ww):
    res = []
    elems = []
    goodMas = True
    for index, arg in enumerate(masArgs):
        if not is_list(arg):
            res.append(arg)
            continue
        else:
            for argEl in arg:
                elems.append(argEl)
            goodMas = False
        newArgArr = [[]]*len(elems)
        for j, a in enumerate(newArgArr):
            newArgArr[j] = res[:]
            newArgArr[j].append(elems[j])
            for u in masArgs[index+1:]:
                newArgArr[j].append(u)
            recur(newArgArr[j], ww)
        break
    if goodMas:
        ww.append(res)