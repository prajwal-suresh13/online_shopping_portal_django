from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile
class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username','email','password1','password2']

class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()
    class Meta:
        model=User
        fields = ['username','email']

class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['image']

class Delivery(forms.Form):
    name = forms.CharField(max_length=200)
    mobile = forms.IntegerField()
    pincode = forms.IntegerField()
    city=forms.CharField(max_length=200)
    state=forms.CharField(max_length=200)
    houseno=forms.IntegerField()
    housename=forms.CharField(max_length=200)
    street=forms.CharField(max_length=100)
options=[('UPI','UPI'),
          ('Debit Card','Debit Card'),
          ('Credit Card','Credit Card'),
          ('Net Banking','Net Banking') ]

class Payment(forms.Form):
    option=forms.ChoiceField(choices=options,widget=forms.RadioSelect())
    name = forms.CharField(max_length=200)
    cardNo=forms.IntegerField()
    cvv=forms.IntegerField(widget=forms.PasswordInput)
