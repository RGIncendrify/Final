from django.db import models


# Create your models here.
class Booking(models.Model):
    first_name = models.CharField(max_length=200)
    reservation_date = models.DateField()
    reservation_slot = models.SmallIntegerField(default=10)
    no_of_guests = models.PositiveIntegerField(null=True)

    def __str__(self): 
        return self.first_name


# Add code to create Menu model
class Menu(models.Model):
   name = models.CharField(max_length=200) 
   price = models.IntegerField(null=False) 
   menu_item_description = models.TextField(max_length=1000, default='') 

   def __str__(self):
      return self.name
   


class Mine(models.Model):
    Tons = models.PositiveIntegerField()
    Grade = models.PositiveIntegerField()
    Manual_Tons = models.PositiveIntegerField()
    Notes = models.CharField(max_length=200)

    def __Int__(self): 
        return self.Tons
    

class Beneficiation(models.Model):
    From_MineTPH = models.PositiveIntegerField()
    ScrubberTPH = models.PositiveIntegerField()
    ThickenerTPH = models.PositiveIntegerField()
    CoarseGangueM3PH = models.PositiveIntegerField()
    RecycleWaterM3PH = models.PositiveIntegerField()
    Notes = models.CharField(max_length=200)

    def __Int__(self): 
        return self.From_MineTPH    
    


class MyModel(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
