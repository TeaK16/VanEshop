from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Van(models.Model):
    van_name = models.CharField(max_length=200, verbose_name="Име")
    description = models.CharField(max_length=200, verbose_name="Опис")
    image_of_van = models.ImageField(upload_to='image/', verbose_name="Слика")
    user = models.ForeignKey(User, on_delete=models.CASCADE)
   
    def __str__(self):
        return f"{self.van_name}"
    
class MakeReservation(models.Model):
    name = models.CharField(max_length=100, verbose_name="Име")
    surname = models.CharField(max_length=100,verbose_name="Презиме")
    phone_number = models.CharField(max_length=100, verbose_name="Телефонски број")
    pick_up_location = models.CharField(max_length=100, verbose_name="Локација на подигање возило")
    van = models.ForeignKey(Van, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    

    def __str__(self):
        return f"{self.name}{self.surname}"
    
class RentVan(models.Model):
    name = models.CharField(max_length=100,verbose_name="Име")
    surname = models.CharField(max_length=100,verbose_name="Презиме")
    card_number = models.IntegerField(verbose_name="Број на картичка")
    cvc = models.IntegerField(verbose_name="CVC")
    expiry_date = models.DateField(verbose_name="Датум на важење")
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    van = models.ForeignKey(Van, on_delete=models.CASCADE)
    

    def __str__(self):
        return f"{self.name}{self.surname}"

    
