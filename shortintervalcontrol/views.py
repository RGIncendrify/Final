from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseNotAllowed, HttpResponseRedirect, Http404
from django.apps import apps
from .forms import BeneficiationForm
from rest_framework import generics
from .serializers import *

from .models import *
from django.forms.models import modelform_factory


def home(request):
    model_names = get_shortintervalcontrol_models()
    return render(request, 'index2.html', {'models': model_names})

def results(request):
    model_names = get_shortintervalcontrol_models()
    return render(request, 'results.html', {'models': model_names})


def success(request):
    model_name = request.session.get('model_name')
    instance_id = request.session.get('instance_id')

    if not model_name or not instance_id:
        raise Http404("Model or instance not specified.")

    Model = apps.get_model('shortintervalcontrol', model_name)
    try:
        instance = Model.objects.get(pk=instance_id)
    except Model.DoesNotExist:
        raise Http404(f"No instance found for model {model_name} with ID {instance_id}.")

    fields_data = []
    for field in instance._meta.fields:
        fields_data.append({
            'verbose_name': field.verbose_name,
            'value': getattr(instance, field.name, '')
        })

    return render(request, 'success.html', {
        'fields_data': fields_data
    })

def get_shortintervalcontrol_models():
    """
    Helper function to fetch models from the 'shortintervalcontrol' app.
    Returns a list of model names.
    """
    app_label = 'shortintervalcontrol'
    models = apps.get_app_config(app_label).get_models()
    return [model.__name__ for model in models]



def model_detail_view(request, model):
    model_names = get_shortintervalcontrol_models()
    Model = apps.get_model(app_label='shortintervalcontrol', model_name=model.capitalize()) 
    instances = Model.objects.all()

    # Dynamically create a ModelForm class for the given model
    ModelForm = modelform_factory(Model, exclude=())  # Customize 'exclude' as needed

    if request.method == 'POST':
        form = ModelForm(request.POST)
        if form.is_valid():
            instance = form.save()  #form.save()
            request.session['model_name'] = instance._meta.model_name #added
            request.session['instance_id'] = instance.pk   #added
            return redirect('success') #  # Replace 'success' with your actual URL name for the success view
    else:
        form = ModelForm()

    return render(request, 'shortintervalcontrol/generic_model_detail.html', {
        'model_name': model.capitalize(), 
        'instances': instances, 
        'models': model_names, 
        'form': form
    })



def create_model_view(model):
    queryset = model.objects.all()
    serializer_class = create_model_serializer(model)
    view_class = type(f'{model.__name__}View', (generics.ListAPIView,), {'queryset': queryset, 'serializer_class': serializer_class})
    return view_class.as_view()