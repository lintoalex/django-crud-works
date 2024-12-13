from crm.models import Employee

from django.forms import ModelForm

from django import forms

from django.contrib.auth.models import User

class EmployeeForm(ModelForm):

    class Meta():

        model=Employee

        fields="__all__"

        widgets={
            "name":forms.TextInput(attrs={"class":"form-control border border-dark"}),
            "email":forms.EmailInput(attrs={"class":"form-control border border-dark"}),
            "address":forms.Textarea(attrs={"class":"form-control border border-dark","row":5 }),
            "gender_type":forms.Select(attrs={"class":"form-control form-select border border-dark"}),
            "salary":forms.NumberInput(attrs={"class":"form-control border border-dark"}),
            "department":forms.TextInput(attrs={"class":"form-control border border-dark"}),
            "date_of_join":forms.DateInput(attrs={"class":"form-control border border-dark","type":"date"}),
            "age":forms.NumberInput(attrs={"class":"form-control border border-dark"}),
            "picture":forms.FileInput(attrs={"class":"form-control border border-dark"})

        }


class SignUpForm(forms.ModelForm):

    class Meta:

        model=User

        fields=["username","email","password"]

        widgets={
         "username":forms.TextInput(attrs={"class":"form-control"}),
         "email":forms.EmailInput(attrs={"class":"form-control"}),
         "password":forms.PasswordInput(attrs={"class":"form-control"})
        }

class SignInForm(forms.Form):

    username=forms.CharField(widget=forms.TextInput(attrs={"class":"form-control"}))

    password=forms.CharField(widget=forms.PasswordInput(attrs={"class":"form-control"}))