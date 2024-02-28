from django.urls import path
from django.apps import apps
from . import views
from .views import * 
from rest_framework.authtoken.views import obtain_auth_token


urlpatterns = [
    path('', views.home, name="home"),
    path('sic/', views.home, name="home"),
    path('SIC/', views.home, name="home"),
    path('results/', views.results, name="results"),
    path('menu/', views.home, name="menu"),
    path('success/', views.success, name="success"),
    path('<str:model>/', model_detail_view, name='model_detail'),
    
   
]


# Dynamically generate URL patterns and views for all models
for model in apps.get_models():
    model_name = model.__name__  # Get the lowercase name of the model
    # Create a URL pattern and view function for the model
    url_name = model_name.lower()
    urlpatterns.append(path(f'{model_name}/', views.model_detail_view, {'model': model_name}, name=f'{url_name}-detail'))



models = apps.get_models()
for model in models:
    view = views.create_model_view(model)
    urlpatterns.append(path('api/{}/'.format(model._meta.model_name), view))