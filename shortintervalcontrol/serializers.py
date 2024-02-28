from django.apps import apps
from django.db.models.base import Model
from rest_framework import serializers
from .models import *

def create_dynamic_serializers():
    # Retrieve all models from the app
    models = apps.get_models()

    serializers_dict = {}

    # Create serializers for each model
    for model in models:
        # Define Meta class for the serializer
        Meta = type('Meta', (), {'model': model, 'fields': '__all__'})

        # Create the serializer class dynamically
        serializer_class = type(f'{model.__name__}Serializer', (serializers.ModelSerializer,), {'Meta': Meta})

        # Add the serializer class to the dictionary
        serializers_dict[model.__name__] = serializer_class

    return serializers_dict

# Create serializers dynamically
serializers_dict = create_dynamic_serializers()

# Now you have a dictionary mapping model names to their respective serializer classes
# You can access them like serializers_dict['BeneficiationSerializer'], serializers_dict['MinesSerializer'], etc.