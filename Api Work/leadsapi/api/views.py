from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from api.models import Lead
from api.serializers import LeadSerializer
from django.db.models import Count
from rest_framework import permissions,authentication


class BookListCreate(APIView):

    def get(self,request,*args,**kwargs):

        context={"message":"list book"}

        return Response(data=context)
    
    def post(self,request,*args,**kwargs):

        context={"message":"new book create"}

        return Response(data=context)
    
    
class RetriveUpdateDestroy(APIView):

    def get(self,request,*args,**kwargs):

        context={"message":"specific book detail"}

        return Response(data=context)
    
    def put(self,request,*args,**kwargs):

        context={"message":"book detail update"}

        return Response(data=context)
    
    def delete(self,request,*args,**kwargs):

        context={"message":"book details delete"}

        return Response(data=context)
    
    
class LeadListCreateView(APIView):

    authentication_classes=[authentication.BasicAuthentication]

    permission_classes=[permissions.IsAdminUser]

    def get(self,request,*args,**kwargs):

        qs=Lead.objects.all()

        serializer_instance=LeadSerializer(qs,many=True)

        return Response(data=serializer_instance.data)
    
    def post(self,request,*args,**kwargs):

        serializer_instance=LeadSerializer(data=request.data)

        if serializer_instance.is_valid():

            serializer_instance.save()

            return Response(data=serializer_instance.data)
        
        return Response(data=serializer_instance.errors)
        
    
class LeadRetrieveUpdateDestroyView(APIView):

    authentication_classes=[authentication.BasicAuthentication]

    permission_classes=[permissions.IsAdminUser]

    serializer_class=LeadSerializer

    def get(self,request,*args,**kwargs):

        id=kwargs.get("pk")

        qs=Lead.objects.get(id=id)

        serializer_instance=LeadSerializer(qs)

        return Response(data=serializer_instance.data)
    
    def delete(self,request,*args,**kwargs):

        id=kwargs.get("pk")

        Lead.objects.get(id=id).delete()

        return Response(data={"message":"delete"})
    
    def put(self,request,*args,**kwargs):

        id=kwargs.get("pk")

        lead_obj=Lead.objects.get(id=id)

        serializer_instance=self.serializer_class(data=request.data,instance=lead_obj)

        if serializer_instance.is_valid():

            serializer_instance.save()

            return Response(data=serializer_instance.data)
        
        return Response(data=serializer_instance.errors)
    

class LeadSummaryView(APIView):

    def get(self,request,*args,**kwargs):

        total_lead=Lead.objects.all().count()

        source_summary=Lead.objects.all().values("source").annotate(total=Count("source"))

        course_summary=Lead.objects.all().values("course").annotate(total=Count("course"))

        status_summary=Lead.objects.all().values("status").annotate(total=Count("status"))

        context={
            "total":total_lead,
            "source_summary":source_summary,
            "course_summary":course_summary,
            "status_summary":status_summary
        }

        return Response(data=context)
    





