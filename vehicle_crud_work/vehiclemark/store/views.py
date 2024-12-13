from django.shortcuts import render,redirect,get_list_or_404,get_object_or_404

from django.views.generic import View

from store.forms import VehicleForm,VehicleUpdateForm,SignUpForm,SignInForm

from store.models import Vehicle

from django.db.models import Q

from django.contrib.auth.models import User

from django.contrib.auth import authenticate,login,logout

from django.contrib import messages

from store.decorators import signin_required

from django.utils.decorators import method_decorator

from django.views.decorators.cache import never_cache

desc=[signin_required,never_cache]

@method_decorator(desc,name="dispatch")
class VehicleCreateView(View):

    template_name="vehicle_add.html"

    form_class=VehicleForm

    def get(self,request,*args,**kwargs):

        form_instance=self.form_class()

        return render(request,self.template_name,{"form":form_instance})
    
    def post(self,request,*args,**kwargs):

        form_data=request.POST

        form_instance=self.form_class(form_data,files=request.FILES)

        if form_instance.is_valid():

            data=form_instance.cleaned_data

            print(data)

            Vehicle.objects.create(**data)

            messages.success(request,"succesully create vehicle list")

            return redirect("vehicle-all")
        
        messages.error(request,"vehicle list create has error")

        return render(request,self.template_name,{"form":form_instance}) 

@method_decorator(desc,name="dispatch")
class VehicleListView(View):

    template_name="vehicle_list.html"

    def get(self,request,*args,**kwargs):

        search_text=request.GET.get("filter")

        qs=Vehicle.objects.all()

        all_names=Vehicle.objects.values_list("name",flat=True).distinct()

        all_brands=Vehicle.objects.values_list("brand",flat=True).distinct()

        all_fuel_type=Vehicle.objects.values_list("fuel_type",flat=True).distinct()

        all_owner_type=Vehicle.objects.values_list("owner_type",flat=True).distinct()

        all_records=[]

        all_records.extend(all_names)

        all_records.extend(all_brands)

        all_records.extend(all_fuel_type)

        all_records.extend(all_owner_type)


        if search_text:

            qs=qs.filter(Q(name__contains=search_text)|Q(fuel_type__contains=search_text)|Q(owner_type__contains=search_text))

        return render(request,self.template_name,{"data":qs,"records":all_records})

@method_decorator(desc,name="dispatch")
class VehicleDetailsView(View):

    template_name="vehicle_details.html"

    def get(self,request,*args,**kwargs):

        id=kwargs.get("pk") 

        qs=Vehicle.objects.get(id=id)

        return render(request,self.template_name,{"data":qs})

@method_decorator(desc,name="dispatch")  
class VehicleDeleteView(View):

    def get(self,request,*args,**kwargs):

        id=kwargs.get("pk")

        Vehicle.objects.get(id=id).delete()

        messages.success(request,"vehicle list has successfully delete")

        return redirect("vehicle-all")

# class VehicleUpdateView(View):

#     template_name="vehicle_update.html"

#     form_class=VehicleForm

#     def get(self,request,*args,**kwargs):

#         id=kwargs.get("pk")

#         vehicle_object=Vehicle.objects.get(id=id)

#         data={
#             "name":vehicle_object.name,
#             "varient":vehicle_object.varient,
#             "description":vehicle_object.description,
#             "fuel_type":vehicle_object.fuel_type,
#             "running_km":vehicle_object.running_km,
#             "color":vehicle_object.color,
#             "price":vehicle_object.price,
#             "brand":vehicle_object.brand,
#             "ower_type":vehicle_object.owner_type
#         }

#         form_instance=self.form_class(initial=data)

#         return render(request,self.template_name,{"form":form_instance})
    
#     def post(self,request,*args,**kwargs):

#         id=kwargs.get("pk")

#         form_data=request.POST

#         form_instance=self.form_class(form_data,files=request.FILES)

#         if form_instance.is_valid():

#             data=form_instance.cleaned_data

#             Vehicle.objects.filter(id=id).update(**data)

#             return redirect("vehicle-all")
        
#         return render(request,self.template_name,{"form":form_instance})
    
@method_decorator(desc,name="dispatch")
class VehicleUpdateView(View):

    template_name="vehicle_update.html"

    form_class=VehicleUpdateForm

    def get(self,request,*args,**kwargs):

        id=kwargs.get("pk")

        Vehicle_objects=get_object_or_404(Vehicle,id=id)

        form_instance=self.form_class(instance=Vehicle_objects)

        return render(request,self.template_name,{"form":form_instance})
    
    def post(self,request,*args,**kwargs):

        id=kwargs.get("pk")

        vehicle_objects=get_object_or_404(Vehicle,id=id)

        form_data=request.POST

        form_instance=self.form_class(form_data,files=request.FILES,instance=vehicle_objects)

        if form_instance.is_valid():

            form_instance.save()

            messages.success(request,"vehicle has update successfully")

            return redirect("vehicle-all")
        
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

            return redirect("signin")
        
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

                messages.success(request,"your signin successfully ")

                return redirect("vehicle-all")
            
            return render(request,self.template_name,{"form":form_instance})

@method_decorator(desc,name="dispatch")
class SignOutView(View):
    
    def get(self,request,*args,**kwargs):

        logout(request)

        messages.success(request,"you have signout successfully")

        return redirect("signin")