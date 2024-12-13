from django import forms

from store.models import Vehicle

from django.contrib.auth.models import User



class VehicleForm(forms.Form):

    name=forms.CharField(widget=forms.TextInput(attrs={"class":"form-control"}))

    varient=forms.CharField(widget=forms.TextInput(attrs={"class":"form-control"}))

    description=forms.CharField(widget=forms.TextInput(attrs={"class":"form-control"}))

    fuel_type=forms.ChoiceField(choices=Vehicle.fuel_options,widget=forms.Select(attrs={"class":"form-control form-select"}))

    running_km=forms.IntegerField(widget=forms.NumberInput(attrs={"class":"form-control"}))

    color=forms.CharField(widget=forms.TextInput(attrs={"class":"form-control"}))

    price=forms.IntegerField(widget=forms.NumberInput(attrs={"class":"form-control"}))

    brand=forms.CharField(widget=forms.TextInput(attrs={"class":"form-control"}))

    owner_type=forms.ChoiceField(choices=Vehicle.owner_options,widget=forms.Select(attrs={"class":"form-control form-select"}))

    picture=forms.ImageField()

class VehicleUpdateForm(forms.ModelForm):

    class Meta:

            model=Vehicle

            fields="__all__"

            widgets={
                 "name":forms.TextInput(attrs={"class":"form-control"}),
                 "varient":forms.TextInput(attrs={"class":"form-control"}),
                 "description":forms.Textarea(attrs={"class":"form-control","row":5}),
                 "fuel_type":forms.Select(attrs={"class":"form-control form-select"}),
                 "running_km":forms.NumberInput(attrs={"class":"form-control"}),
                 "color":forms.TextInput(attrs={"class":"form-control"}),
                 "price":forms.NumberInput(attrs={"class":"form-control"}),
                 "brand":forms.TextInput(attrs={"class":"form-control"}),
                 "owner_type":forms.Select(attrs={"class":"form-control form-select"}),
                 "picture":forms.FileInput(attrs={"class":"form-control"})
            }

class SignUpForm(forms.ModelForm):
     
    class Meta:
         
        model=User

        fields=["username","password","email"]

        widgets={
            "username":forms.TextInput(attrs={"class":"form-control"}),
            "password":forms.PasswordInput(attrs={"class":"form-control"}),
            "email":forms.EmailInput(attrs={"class":"form-control"})
        }

class SignInForm(forms.Form):
     
     username=forms.CharField(widget=forms.TextInput(attrs={"class":"form-control mb-3"}))

     password=forms.CharField(widget=forms.PasswordInput(attrs={"class":"form-control mb-3"}))