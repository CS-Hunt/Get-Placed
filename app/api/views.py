from rest_framework.generics import ListAPIView,RetrieveAPIView,CreateAPIView, DestroyAPIView
from app.models import ResorcesModel,Placement_Company_Detail
from .serializers import ResorcesSerializer,Placement_Company_DetailAPI
from rest_framework.filters import OrderingFilter
from rest_framework import viewsets

class ResourcesModelAPI(viewsets.ModelViewSet):
    queryset = ResorcesModel.objects.all()
    serializer_class =  ResorcesSerializer
    filter_backends = [OrderingFilter]
    ordering = ['title']

class JobAPI(viewsets.ModelViewSet):
    queryset = Placement_Company_Detail.objects.all()
    serializer_class =  Placement_Company_DetailAPI
    filter_backends = [OrderingFilter]
    ordering = ['-post_date']
