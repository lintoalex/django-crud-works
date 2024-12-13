from django import forms

from movie.models import Movie

from django.contrib.auth.models import User

from captcha.fields import CaptchaField

class MovieForm(forms.Form):

    title=forms.CharField(widget=forms.TextInput(attrs={"class":"form-control mb-3"}))

    genre=forms.CharField(widget=forms.TextInput(attrs={"class":"form-control mb-3"}))

    year=forms.IntegerField(widget=forms.NumberInput(attrs={"class":"form-control mb-3"}))

    runtime=forms.IntegerField(widget=forms.NumberInput(attrs={"class":"form-control mb-3"}))

    language=forms.CharField(widget=forms.TextInput(attrs={"class":"form-control mb-3"}))

    rating=forms.IntegerField(widget=forms.NumberInput(attrs={"class":"form-control mb-3"}))

    picture=forms.ImageField()

class MovieUpdateForm(forms.ModelForm):

    class Meta:

        model=Movie

        fields="__all__"

        widgets={
            "title":forms.TextInput(attrs={"class":"form-control"}),
            "genre":forms.TextInput(attrs={"class":"form-control"}),
            "year":forms.NumberInput(attrs={"class":"form-control"}),
            "runtime":forms.NumberInput(attrs={"class":"form-control"}),
            "rating":forms.NumberInput(attrs={"class":"form-control"}),
            "language":forms.TextInput(attrs={"class":"form-control"}),
            "picture":forms.FileInput(attrs={"class":"form-control"}),

        }

class SignUpForm(forms.ModelForm):
    captcha=CaptchaField()

    class Meta:

        model=User

        fields=["username","password","email","captcha"]

        widgets={
            "username":forms.TextInput(attrs={"class":"form-control mb-4"}),
            "password":forms.PasswordInput(attrs={"class":"form-control mb-4"}),
            "email":forms.EmailInput(attrs={"class":"form-control mb-4"})
        }

class SignInForm(forms.Form):

    username=forms.CharField(widget=forms.TextInput(attrs={"class":"form-control mb-4"}))

    password=forms.CharField(widget=forms.PasswordInput(attrs={"class":"form-control mb-4"}))