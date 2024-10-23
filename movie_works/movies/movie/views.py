from django.shortcuts import render

from movie.forms import MovieForm

from django.views.generic import View

from movie.models import Movie


class MovieView(View):

    template_name="movie.html"

    form_class=MovieForm

    def get(self,request,*args,**kwargs):

        form_instance=self.form_class()

        return render(request,self.template_name,{"form":form_instance})
    
    def post(self,request,*args,**kwrags):

        form_data=request.POST  

        form_instance=self.form_class(form_data)

        if form_instance.is_valid():

           data=form_instance.cleaned_data

           print(data)

           Movie.objects.create(**data)

        return render(request,self.template_name,{"form":form_instance})

class MovieListView(View):

    template_name="movie_list.html"

    def get(self,request,*args,**kwargs):

        qs=Movie.objects.all()

        return render(request,self.template_name,{"data":qs})