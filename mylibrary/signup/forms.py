from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User
from django.forms import widgets
from .models import Book, Borrow

class RegisterForm(UserCreationForm):

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2']



class UpdateForm(UserChangeForm):
    class Meta:
        model = User
        fields = (
            'username',
            'email',
            'first_name',
            'last_name',
            'password'
        )


class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields= ['title','author','category','ISBN','available','year']


class BorrowForm(forms.ModelForm):
    class Meta:
        model = Borrow
        fields= ['user','book','returndate']
       