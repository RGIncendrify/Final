from django.contrib import admin

# Register your models here.
from .models2 import Menu
from .models2 import Booking
from .models2 import Mine
from .models2 import Beneficiation



admin.site.register(Menu)
admin.site.register(Booking)
admin.site.register(Mine)
admin.site.register(Beneficiation)