from django.shortcuts import render

from django.views.generic import View

# Create your views here.

class IndexView(View):

    def get(self,request,*args,**kwargs):

        person_data={
            "id":1,
            "age":32,
            "name":"Ram",
            "location":"Tvm",
            "address":"Ernakulam Kakkanad"
        }
        
        return render(request,"index.html",{"person":person_data})
    

class ProjectView(View):

    def get(self,request,*args,**kwargs):

        projects=[
            {"id":1,"title":"codehub",
             "description":"project decsription",
             "front_end":"react","back_end":"django"
             },
              {"id":2,"title":"ServiceHub",
             "description":"project decsription",
             "front_end":"Angular","back_end":"django"
             },
              {"id":3,"title":"linksphere",
             "description":"project decsription",
             "front_end":"react","back_end":"django"
             }
        ]

        return render(request,"projects.html",{"projects":projects})
    
class ContactView(View):

    def get(self,request,*args,**kwargs):

        personal_name="vipin"

        personal_contact=95887744235

        personal_address="Ernakulam Kakkanad Kunnumpuram near luminar"

        personal_place="Ernakulam"

        return render(request,"contact.html",{"name":personal_name,"contact":personal_contact,"address":personal_address,"place":personal_place})
    
class SkillsView(View):

    def get(self,request,*args,**kwargs):

        backend_dataproceesing="Python"
        backend_framework="Django"

        database="MySql"

        frontend_framework="React"

        return render(request,"skills.html",{"backend":backend_dataproceesing,"framework":backend_framework,"database":database,"frontend":frontend_framework})

class ServicesView(View):

    def get(self,request,*args,**kwargs):

        services=["webapplication","development","Api","Ui/Ux"]

        return render(request,"services.html",{"services":services})