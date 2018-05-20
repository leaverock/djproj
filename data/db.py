from django.apps import apps
from . import dbg_data_db


############################################
#
#    all base
#
############################################
def del_model(model):
    #info_model(model)
    # https://docs.djangoproject.com/en/1.11/ref/models/querysets/
    q = model.objects.all()
    q_lng = len(q)
    q.delete()
    if dbg_data_db: print("data.db.del_model: стёрли из %s: %d шт." % (model, q_lng))


def del_models_from_app(app):
    #if dbg_data: print("data.db.del_models_from_app: '%s'" % app)
    myapp = apps.get_app_config(app)
    models = myapp.models.values()
    for model in models:
        del_model(model)
        #if dbg_data: print("data.db.del_models_from_app: '%s': exit" % app)


def info_model(model):
    # https://docs.djangoproject.com/en/1.11/ref/models/querysets/
    q = model.objects.all()
    q_lng = len(q)
    #q_lng = q.__len__()
    if dbg_data_db: print("data.db.info_model: всего %s.objects: %d шт." % (model, q_lng))


def info_app(app):
    # https://stackoverflow.com/questions/29738976/how-can-i-get-all-models-in-django-1-8
    myapp = apps.get_app_config(app)
    models = myapp.models.values()
    if dbg_data_db: print()
    for model in models:
        #if dbg_data: print("data.db.info_app: model from app '%s': '%s'" % (app, model))
        info_model(model)
    if dbg_data_db: print()


def info_proj():
    # https://stackoverflow.com/questions/29738976/how-can-i-get-all-models-in-django-1-8
    if dbg_data_db: print()
    for model in apps.get_models():
        if dbg_data_db: print("data.db.info_proj: model: %s" % model)
        info_model(model)

