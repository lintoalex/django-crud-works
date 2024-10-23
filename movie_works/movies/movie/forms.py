from django import forms

class MovieForm(forms.Form):

    title=forms.CharField(widget=forms.TextInput(attrs={"class":"form-control mb-3"}))

    genre=forms.CharField(widget=forms.TextInput(attrs={"class":"form-control mb-3"}))

    year=forms.IntegerField(widget=forms.NumberInput(attrs={"class":"form-control mb-3"}))

    runtime=forms.IntegerField(widget=forms.NumberInput(attrs={"class":"form-control mb-3"}))

    language=forms.CharField(widget=forms.TextInput(attrs={"class":"form-control mb-3"}))

    rating=forms.IntegerField(widget=forms.NumberInput(attrs={"class":"form-control mb-3"}))