from rest_framework import routers
# from .views import stockAPIDataViewSet
# from .views import resourcesDataViewSet
from .views import resourcesDataViewSet
from .views import totalCostViewSet
from django.contrib import admin
from django.urls import path
from django.conf.urls import include, url
# router = routers.DefaultRouter()
# router.register(r'stockAPI', resourcesDataViewSet.as_view(), basename='stock')

# urlpatterns = router.urls

urlpatterns = [
    path('resources/', resourcesDataViewSet.as_view()),
    path('total_cost/', totalCostViewSet.as_view()),
]
