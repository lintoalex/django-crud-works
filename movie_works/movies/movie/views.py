from django.shortcuts import render,redirect,get_object_or_404

from movie.forms import MovieForm,MovieUpdateForm,SignUpForm,SignInForm

from django.views.generic import View

from movie.models import Movie

from django.db.models import Q

from django.contrib.auth.models import User

from django.contrib.auth import authenticate,login,logout

from django.contrib import messages

from movie.decorators import signin_required

from django.utils.decorators import method_decorator

from django.views.decorators.cache import never_cache

desc=[signin_required,never_cache]

@method_decorator(desc,"dispatch")
class MovieView(View):

    template_name="movie.html"

    form_class=MovieForm

    def get(self,request,*args,**kwargs):

        form_instance=self.form_class()

        return render(request,self.template_name,{"form":form_instance})
    
    def post(self,request,*args,**kwrags):

        form_data=request.POST  

        form_instance=self.form_class(form_data,files=request.FILES)

        if form_instance.is_valid():

           data=form_instance.cleaned_data

           print(data)

           Movie.objects.create(**data)

           messages.success(request,"movie list create successfully added")

           return redirect("movie-list")
        
        messages.error(request,"movie list add fail")

        return render(request,self.template_name,{"form":form_instance})

@method_decorator(desc,"dispatch")
class MovieListView(View):

    template_name="movie_list.html"

    def get(self,request,*args,**kwargs):

        search_text=request.GET.get("filter")

        qs=Movie.objects.all()

        all_title=Movie.objects.values_list("title",flat=True).distinct()

        all_language=Movie.objects.values_list("language",flat=True).distinct()

        all_genre=Movie.objects.values_list("genre",flat=True).distinct()

        all_records=[]

        all_records.extend(all_title)

        all_records.extend(all_language)

        all_records.extend(all_genre)

        if search_text:

            qs=qs.filter(Q(title__contains=search_text)|Q(language__contains=search_text)|Q(genre__contains=search_text))

        return render(request,self.template_name,{"data":qs,"records":all_records})
    
@method_decorator(desc,"dispatch")
class MovieDetailsView(View):

    template_name="movie_details.html"

    def get(self,request,*args,**kwargs):

        id=kwargs.get("pk")

        qs=Movie.objects.get(id=id)

        return render(request,self.template_name,{"data":qs})

@method_decorator(desc,"dispatch")
class MovieDeleteView(View):

    def get(self,request,*args,**kwargs):

        id=kwargs.get("pk")

        Movie.objects.get(id=id).delete()

        messages.success(request,"sucessfully delete")

        return redirect("movie-list")

# class MovieUpdateView(View):

#     template_name="movie_update.html"

#     form_class=MovieForm

#     def get(self,request,*args,**kwargs):

#         id=kwargs.get("pk")

#         movie_object=Movie.objects.get(id=id)

#         data={
#             "title":movie_object.title,
#             "genre":movie_object.genre,
#             "year":movie_object.year,
#             "runtime":movie_object.runtime,
#             "language":movie_object.language,
#             "rating":movie_object.rating
#         }

#         form_instance=self.form_class(initial=data)

#         return render(request,self.template_name,{"form":form_instance})
    
#     def post(self,request,*args,**kwargs):

#         id=kwargs.get("pk")

#         form_data=request.POST

#         form_instance=self.form_class(form_data)

#         if form_instance.is_valid():

#             data=form_instance.cleaned_data

#             Movie.objects.filter(id=id).update(**data)

#             return redirect("movie-list")
        
#         return render(request,self.template_name,{"form":form_instance})

@method_decorator(desc,"dispatch")
class MovieUpdateView(View):

    template_name="movie_update.html"

    form_class=MovieUpdateForm

    def get(self,request,*args,**kwargs):

        id=kwargs.get("pk")

        movie_objects=get_object_or_404(Movie,id=id)

        form_instance=self.form_class(instance=movie_objects)

        return render(request,self.template_name,{"form":form_instance})
    
    def post(self,request,*args,**kwrags):

        id=kwrags.get("pk")

        movie_objects=get_object_or_404(Movie,id=id)

        form_data=request.POST

        form_instance=self.form_class(form_data,files=request.FILES,instance=movie_objects)

        if form_instance.is_valid():

            form_instance.save()

            messages.success(request,"movie list update successfully complete")

            return redirect("movie-list")
        
        messages.error(request,"movie list update fail")
        
        return render(request,self.template_name,{"form":form_instance})

class SignUpView(View):

    template_name="signup.html"

    form_class=SignUpForm

    def get(self,request,*args,**kwargs):

        form_instance=self.form_class()

        return render(request,self.template_name,{"form":form_instance})
    
    def post(self,request,*args,**kwargs):

        form_data=request.POST

        form_instance=self.form_class(form_data)

        if form_instance.is_valid():

            data=form_instance.cleaned_data

            User.objects.create_user(**data)

            return redirect("signup")
        
        return render(request,self.template_name,{"form":form_instance})
    
class SignInView(View):

    template_name="signin.html"

    form_class=SignInForm

    def get(self,request,*args,**kwargs):

        form_instance=self.form_class()

        return render(request,self.template_name,{"form":form_instance})
    
    def post(self,request,*args,**kwargs):

        form_data=request.POST

        form_instance=self.form_class(form_data)

        if form_instance.is_valid():

            data=form_instance.cleaned_data

            uname=data.get("username")

            pwd=data.get("password")

            user_object=authenticate(request,username=uname,password=pwd)

            if user_object:

                login(request,user_object)

                messages.success(request,"successfully signin")

                return redirect("movie-list")
        
        return render(request,self.template_name,{"form":form_instance})

@method_decorator(desc,"dispatch")
class SignOutView(View):

    def get(self,request,*args,**kwargs):

        logout(request)

        messages.success(request,"successfully logout")

        return redirect("signin")