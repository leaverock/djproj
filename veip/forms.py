from django import forms


class VeipInputForm(forms.Form):
    train_type = forms.IntegerField(            initial=9,      required=True, label='Тип подвижного состава')
    track_structure = forms.IntegerField(       initial=16,     required=True, label='Тип верхнего строения пути')
    horizontal_spectrum = forms.IntegerField(   initial=1,      required=True, label='Тип спектра горизонтального')
    vertical_spectrum = forms.IntegerField(     initial=1,      required=True, label='Тип спектра вертикального')
    ignored = forms.IntegerField(               initial=0,      required=True, label='Игнорируется')
    vehicle_coordinates = forms.IntegerField(   initial=1,      required=True, label='Номер экипажа')
    speed = forms.FloatField(                   initial=12.0,   required=True, label='Скорость движения (м/с)')
    radius = forms.FloatField(                  initial=350.0,  required=True, label='Радиус кривой (м)')
    tapes_distance = forms.FloatField(          initial=0.8,    required=True, label='Расстояние между кругами катания (м)')
    superelevation = forms.FloatField(          initial=0.05,   required=True, label='Возвышение наружного рельса (м)')
    creep_coefficient = forms.FloatField(       initial=556.0,  required=True, label='Коэффициент крипа (тс/м)')
    horizontal_stiffness = forms.FloatField(    initial=1900.0, required=True, label='Горизонтальная жесткость пути')
    halved_gap = forms.FloatField(              initial=0.007,  required=True, label='Половина зазора в колее (м)')
    wheel_wear = forms.FloatField(              initial=1.0,    required=True, label='Коэффициент износа колес')
    creeps_ratio = forms.FloatField(            initial=0.8,    required=True, label='Соотношения крипов')


class VeipMultiVarInputForm(forms.Form):
    train_type = forms.IntegerField(            initial=9,      disabled=True , required=True, label='Тип подвижного состава')
    track_structure = forms.IntegerField(       initial=16,     disabled=True , required=True, label='Тип верхнего строения пути')
    horizontal_spectrum = forms.IntegerField(   initial=1,      disabled=True , required=True, label='Тип спектра горизонтального')
    vertical_spectrum = forms.IntegerField(     initial=1,      disabled=True , required=True, label='Тип спектра вертикального')
    ignored = forms.IntegerField(               initial=0,      disabled=True , required=True, label='Игнорируется')
    vehicle_coordinates = forms.IntegerField(   initial=1,      disabled=True , required=True, label='Номер экипажа')
    speed = forms.FloatField(                   initial=12.0,   disabled=True , required=True, label='Скорость движения (м/с)')
    radius = forms.FloatField(                  initial=350.0,  disabled=True , required=True, label='Радиус кривой (м)')
    tapes_distance = forms.FloatField(          initial=0.8,    disabled=True , required=True, label='Расстояние между кругами катания (м)')
    superelevation = forms.FloatField(          initial=0.05,   disabled=True , required=True, label='Возвышение наружного рельса (м)')
    creep_coefficient = forms.FloatField(       initial=556.0,  disabled=True , required=True, label='Коэффициент крипа (тс/м)')
    horizontal_stiffness = forms.FloatField(    initial=1900.0, disabled=True , required=True, label='Горизонтальная жесткость пути')
    halved_gap = forms.FloatField(              initial=0.007,  disabled=True , required=True, label='Половина зазора в колее (м)')
    wheel_wear = forms.FloatField(              initial=1.0,    disabled=True , required=True, label='Коэффициент износа колес')
    creeps_ratio = forms.FloatField(            initial=0.8,    disabled=True , required=True, label='Соотношения крипов')