from django.http import HttpResponse
from django.shortcuts import render
from .run.jan25_19.veip_21jan19.go import go, work_dir


def index(request):
    context = {}
    for a in [6, 7]:
        context[f'p{a}'] = True
    return render(request, 'veip\\index.html', context)


def vivod(request):
    train_type = 9              # float(request.POST['train_type'])
    track_structure = 16        # float(request.POST['track_structure'])
    horizontal_spectrum = 1     # float(request.POST['horizontal_spectrum'])
    vertical_spectrum = 1       # float(request.POST['vertical_spectrum'])
    ignored = 0                 # float(request.POST['ignored'])
    vehicle_coordinates = 1     # float(request.POST['vehicle_coordinates'])
    speed =                       float(request.POST['speed'])
    radius =                      float(request.POST['radius'])
    tapes_distance = 0.8        # float(request.POST['tapes_distance'])
    superelevation = 0.05       # float(request.POST['superelevation'])
    creep_coefficient = 556     # float(request.POST['creep_coefficient'])
    horizontal_stiffness = 1900 # float(request.POST['horizontal_stiffness'])
    halved_gap = 0.007          # float(request.POST['halved_gap'])
    wheel_wear = 1.0            # float(request.POST['wheel_wear'])
    creeps_ratio = 0.8          # float(request.POST['creeps_ratio'])

    text = go(train_type,
              track_structure,
              horizontal_spectrum,
              vertical_spectrum,
              ignored,
              vehicle_coordinates,
              speed,
              radius,
              tapes_distance,
              superelevation,
              creep_coefficient,
              horizontal_stiffness,
              halved_gap,
              wheel_wear,
              creeps_ratio)
    #with open(r'C:\work\veip\djproj\veip\run\vivod', 'r') as file:

    return HttpResponse(f"<pre>{text}</pre>")