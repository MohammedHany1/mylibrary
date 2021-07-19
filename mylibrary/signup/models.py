import django
from django.db import models
from django.conf import settings
from django.db.models.expressions import OrderBy
from django.utils.timezone import datetime 

class Book(models.Model):
    title= models.CharField(max_length=50)
    author= models.CharField(max_length=150)
    category= models.CharField(max_length=80)
    ISBN= models.IntegerField()
    #period= models.IntegerField(null=True,blank=True)
    available= models.BooleanField(default=True) #Not borrowed 
    year= models.IntegerField()

    def __str__(self):
     return self.title
    

class Borrow(models.Model):
    user=models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE,default='user')
    book=models.ForeignKey(Book, on_delete=models.CASCADE,default='book')
    returndate= models.DateField(default=datetime.now)
    def __str__(self):
        return f'{self.user} has borrowed {self.book} untill {self.returndate}'
 