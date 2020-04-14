from django.shortcuts import render
# from rest_framework import viewsets
from .models import stockAPIData
from .serializers import stockAPIDataSerializer
from .models import resourcesData
from rest_framework.response import Response
from .serializers import resourcesDataSerializer
from rest_framework.renderers import JSONRenderer
from rest_framework.views import APIView
from django.shortcuts import get_list_or_404, get_object_or_404

# class stockAPIDataViewSet(viewsets.ModelViewSet):

#     queryset = stockAPIData.objects.all().order_by('Id','title','amount','unit','price','date')
#     serializer_class = stockAPIDataSerializer

# class resourcesDataViewSet(viewsets.ModelViewSet):

#     queryset = resourcesData.objects.all()
#     serializer_class = resourcesDataSerializer

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
    
    def put(self, request, pk):
        print(request.data.get('Id'))
        queryset = get_object_or_404(stockAPIData.objects.all(), pk=pk)
        serializer = stockAPIDataSerializer(instance=queryset, data=request.data, partial=True)
        if serializer.is_valid():
            article_saved = serializer.save()
        return Response()

        

        # def put(self, request, pk):
        #     queryset = get_object_or_404(stockAPIData.objects.all(), pk=Id)
        #     serializer = stockAPIDataSerializer(data = request.data)
        #     serializer = ArticleSerializer(instance=queryset, data=data, partial=True)
        #     if serializer.is_valid():
        #         article_saved = serializer.save()
        # return Response()

        # article = request.data.get('article')

        # # Create an article from the above data
        # serializer = ArticleSerializer(data=article)
        # if serializer.is_valid(raise_exception=True):
        #     article_saved = serializer.save()
        #  return Response({"success": "Article '{}' created successfully".format(article_saved.title)})
