from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render
from django.http import HttpResponseRedirect

from .forms import UchEditForm
from track.models import UchSTRUCT, CategSTRUCT, StansSTRUCT


def uch_index(request):
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = UchEditForm(request.POST)
        context = {'uchModelForm': form}

        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # вроде как нужно по нажатию на "сохранить" просить юзера ввести имя файла
            # redirect to a new URL:
            return HttpResponseRedirect('/kortes/index')
    # if a GET (or any other method) we'll create a blank form
    else:
        template = loader.get_template('track\\detail.html')
        context = {

        }
        return HttpResponse(template.render(context, request))

    return render(request, 'kortes/uchastk/uch_index.html', context)

def razdel_punkt(request):
    context = {}
    return render(request, 'kortes/uchastk/razdel_punkt.html', context)