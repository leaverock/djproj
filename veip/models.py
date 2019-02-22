from django.db import models


# https://www.caktusgroup.com/blog/2018/05/07/creating-dynamic-models-django/
class Computation(models.Model):
    user_name = models.CharField(max_length=128)
    user_pass = models.CharField(max_length=128)

    #train_type = models.IntegerField(         )
    #track_structure = models.IntegerField(    )
    #horizontal_spectrum = models.IntegerField()
    #vertical_spectrum = models.IntegerField(  )
    #ignored = models.IntegerField(            )
    #vehicle_coordinates = models.IntegerField()
    #speed = models.FloatField(                )
    #radius = models.FloatField(               )
    #tapes_distance = models.FloatField(       )
    #superelevation = models.FloatField(       )
    #creep_coefficient = models.FloatField(    )
    #horizontal_stiffness = models.FloatField( )
    #halved_gap = models.FloatField(           )
    #wheel_wear = models.FloatField(           )
    #creeps_ratio = models.FloatField(         )


class GroupOfParams(models.Model):
    name = models.CharField(max_length=128)
    #computation = models.ForeignKey(Computation)


class ParamsInGroup(models.Model):
    group = models.ForeignKey(GroupOfParams, on_delete='CASCADE')
    param = models.CharField(max_length=20)