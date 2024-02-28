"""from django.forms import ModelForm
from django import forms
from .models2 import Booking, Menu, Mine, Beneficiation, MyModel

class BookingForm(ModelForm):
    class Meta:
        model = Booking
        fields= "__all__"

class MenuForm(ModelForm):
    class Meta:
        model = Menu
        fields= "__all__"



class MineForm(ModelForm):
    class Meta:
        model = Mine
        fields= "__all__"        


class BeneficiationForm(ModelForm):
    class Meta:
        model = Beneficiation
        fields= "__all__"

class MyForm(forms.ModelForm):
    class Meta:
        model = MyModel
        fields = ['name', 'email', 'message']  """