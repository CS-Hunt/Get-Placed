
from django.contrib import admin
from django.urls import path,include

from app.api import views
from rest_framework.routers import DefaultRouter

# Creaing Router Objects
router = DefaultRouter()

# Register StudentViewSet with Router
router.register('resources',views.ResourcesModelAPI,basename='Resources')
router.register('job-post',views.JobAPI,basename='job-post')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('app.urls')),
    path('api/',include(router.urls)),
]
