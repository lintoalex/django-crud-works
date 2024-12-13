from django.shortcuts import render,redirect,get_object_or_404
from django.views.generic import View
from crm.forms import EmployeeForm,SignUpForm,SignInForm
from crm.forms import Employee
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from django.utils.decorators import method_decorator
from crm.decorators import signin_required
from django.views.decorators.cache import never_cache


desc=[signin_required,never_cache]

@method_decorator(desc,name="dispatch")
class EmployeeCreateView(View):

    template_name="employe_create.html"

    form_class=EmployeeForm

    def get(self,request,*args,**kwargs):

        form_instance=self.form_class()

        return render(request,self.template_name,{"form":form_instance})
    
    def post(self,request,*args,**kwargs):

        form_data=request.POST

        form_instance=self.form_class(form_data,files=request.FILES)

        if form_instance.is_valid():

            form_instance.save()

            messages.success(request,"create has successfully")

            return redirect("employee-list")
        
        messages.error(request,"fail to add")

        return render(request,self.template_name,{"form":form_instance})

@method_decorator(desc,name="dispatch")
class EmployeeListView(View):

    template_name="employee_list.html"

    def get(self,request,*args,**kwargs):

        qs=Employee.objects.all()

        return render(request,self.template_name,{"data":qs})
    
@method_decorator(desc,name="dispatch")
class EmployeeDeleteView(View):

    def get(self,request,*args,**kwargs):

        id=kwargs.get("pk")

        qs=Employee.objects.get(id=id).delete()

        messages.success(request,"delete successfully")

        return redirect("employee-list")

@method_decorator(desc,name="dispatch") 
class EmployeeUpdate(View):

    temaplate_name="employee_update.html"

    form_class=EmployeeForm

    def get(self,request,*args,**kwargs):

        id=kwargs.get("pk")

        employee_objects=Employee.objects.get(id=id)

        form_instance=self.form_class(instance=employee_objects)

        return render(request,self.temaplate_name,{"form":form_instance})

    def post(self,request,*args,**kwargs):

        id=kwargs.get("pk")

        employee_objects=Employee.objects.get(id=id)

        form_data=request.POST

        form_instance=self.form_class(form_data)      

        form_data=request.POST

        form_instance=self.form_class(form_data,files=request.FILES,instance=employee_objects)

        if form_instance.is_valid():

            form_instance.save()

            messages.success(request,"update has employe successfully")

            return redirect("employee-list")
        
        messages.error(request,"fail to update")

        return render(request,self.temaplate_name,{"form":form_instance})
    
@method_decorator(desc,name="dispatch")
class EmployeeDetailView(View):

    template_name="employee_detail.html"

    def get(self,request,*args,**kwargs):

        id=kwargs.get("pk")

        qs=Employee.objects.get(id=id)

        return render(request,self.template_name,{"data":qs})
    
class SignUpView(View):

    template_name="register.html"

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

            messages.success(request,"successfully signup")

            return redirect("register")
        
        return render(request,self.template_name,{"form":form_instance})
    
class SignInView(View):

    template_name="sign.html"

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
            print(user_object)

            if user_object:

                login(request,user_object)

                return redirect("employee-list")
            
        return render(request,self.template_name,{"form":form_instance})
    
class SignOutView(View):

    def get(self,request,*args,**kwargs):

        logout(request)

        return redirect("signin")
    
