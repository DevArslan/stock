from django.shortcuts import render
# from rest_framework import viewsets
from .models import stockAPIData
from .serializers import stockAPIDataSerializer
from rest_framework.response import Response
from rest_framework.renderers import JSONRenderer
from rest_framework.views import APIView

class resourcesDataViewSet(APIView):

    def get(self, request):
        queryset =  stockAPIData.objects.all()
        serializer = stockAPIDataSerializer(queryset, many = True)
        total_count = stockAPIData.objects.count()
        print(total_count)
        return Response({"resources":serializer.data, "total_count":total_count})
    
    def post(self, request):
        serializer = stockAPIDataSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
        return Response()
    
    def put(self, request, *args, **kwargs):
        IDselect = request.data.get('Id')
        queryset = stockAPIData.objects.get( Id = IDselect)
        serializer = stockAPIDataSerializer(instance=queryset, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
        return Response()
    

    def delete(self, request, *args, **kwargs):
        IDselect = request.data.get('Id')
        queryset = stockAPIData.objects.get( Id = IDselect)
        queryset.delete()
        return Response()

class totalCostViewSet(APIView):

    def get(self,request):
        queryset =  stockAPIData.objects.all()
        totalCost = 0
        for item in queryset:
            totalCost += item.amount * item.price
        print(totalCost)
        return Response({"total_cost":totalCost})
