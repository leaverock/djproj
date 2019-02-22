from django import forms


from .models import Computation, GroupOfParams, ParamsInGroup


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


class GroupOfParamsForm(forms.ModelForm):
    #name = forms.CharField(max_length=128, required=True)
    #user_name = forms.HiddenInput()
    #user_pass = forms.HiddenInput()

    class Meta:
        model = GroupOfParams
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        params = ParamsInGroup.objects.filter(
            group=self.instance
        )
        for i in range(len(params) + 1):
            field_name = 'param_%s' % (i,)
            self.fields[field_name] = forms.CharField(required=False)
            try:
                self.initial[field_name] = params[i].param
            except IndexError:
                self.initial[field_name] = ""
        # create an extra blank field
        field_name = 'param_%s' % (i + 1,)
        self.fields[field_name] = forms.CharField(required=False, widget=forms.TextInput(attrs={'class' :'param-list-new'}))
        #self.fields[field_name] = ""
    
    def clean(self):
        params = set()
        i = 0
        field_name = 'param_%s' % (i,)
        while self.cleaned_data.get(field_name):
           param = self.cleaned_data[field_name]
           if param in params:
               self.add_error(field_name, 'Duplicate')
           else:
               params.add(param)
           i += 1
           field_name = 'param_%s' % (i,)
        self.cleaned_data["params"] = params

    #def save(self):
    #    group = self.instance
    #    group.first_name = self.cleaned_data["first_name"]
    #    group.last_name = self.cleaned_data["last_name"]
    #
    #    group.interest_set.all().delete()
    #    for param in self.cleaned_data["params"]:
    #       ParamsInGroup.objects.create(
    #           group=group,
    #           param=param,
    #       )

    def get_param_fields(self):
        for field_name in self.fields:
            if field_name.startswith("param"):
                yield self[field_name]

    #train_type = forms.IntegerField(         required=True,)
    #track_structure = forms.IntegerField(    required=True,)
    #horizontal_spectrum = forms.IntegerField(required=True,)
    #vertical_spectrum = forms.IntegerField(  required=True,)
    #ignored = forms.IntegerField(            required=True,)
    #vehicle_coordinates = forms.IntegerField(required=True,)
    #speed = forms.FloatField(                required=True,)
    #radius = forms.FloatField(               required=True,)
    #tapes_distance = forms.FloatField(       required=True,)
    #superelevation = forms.FloatField(       required=True,)
    #creep_coefficient = forms.FloatField(    required=True,)
    #horizontal_stiffness = forms.FloatField( required=True,)
    #halved_gap = forms.FloatField(           required=True,)
    #wheel_wear = forms.FloatField(           required=True,)
    #creeps_ratio = forms.FloatField(         required=True,)