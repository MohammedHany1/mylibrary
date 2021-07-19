import datetime

from django.db.models.fields import BooleanField
from signup.models import Book,Borrow

def checkavailability(book,returndate):
    availList=BooleanField()
    borrowingList= Borrow.objects.filter(book=book)
    for book in borrowingList:
        if returndate > datetime.date.today():
            availList=True
        else:
            availList=False
   
    return availList
