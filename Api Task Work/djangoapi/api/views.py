from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from api.models import Properity
from api.serializers import LeadSerializer
from django.db.models import Count

class LeadListCreateView(APIView):

    def get(self,request,*args,**kwargs):

        qs=Properity.objects.all()

        serializer_instance=LeadSerializer(qs,many=True)

        return Response(data=serializer_instance.data)
    
    def post(self,request,*args,**kwargs):

        serializer_instance=LeadSerializer(data=request.data)

        if serializer_instance.is_valid():

            serializer_instance.save()

            return Response(data=serializer_instance.data)

        return Response(data=serializer_instance.errors)

class LeadRetrieveUpdateDestroyView(APIView):

    serializer_class=LeadSerializer

    def get(self,request,*args,**kwargs):

        id=kwargs.get("pk")

        qs=Properity.objects.get(id=id)

        serializer_instance=LeadSerializer(qs)

        return Response(data=serializer_instance.data)
    
    def delete(self,request,*args,**kwargs):

        id=kwargs.get("pk")

        Properity.objects.get(id=id).delete()

        return Response(data={"message":"success delete"})
    
    def put(self,request,*args,**kwargs):

        id=kwargs.get("pk")

        led_obj=Properity.objects.get(id=id)

        serializer_instance=self.serializer_class(data=request.data,instance=led_obj)

        if serializer_instance.is_valid():

            serializer_instance.save()

            return Response(data=serializer_instance.data)
        
        return Response(data=serializer_instance.errors)

class ProperitySummaryView(APIView):

    def get(self,request,*args,**kwargs):

        total_properity=Properity.objects.all().count()

        bedroom_count_summary=Properity.objects.all().values("bedroom_count").annotate(total=Count("bedroom_count"))

        context={
            "total":total_properity,
            "bedroom_count_summary":bedroom_count_summary

        }

        return Response(data=context)
