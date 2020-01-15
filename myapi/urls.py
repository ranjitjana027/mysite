from django.urls import path, include
from .views import StudentViewSet
from rest_framework import routers
router=routers.DefaultRouter()
router.register(r'students',StudentViewSet)

urlpatterns=[
    path("",include(router.urls)),
    path("api-auth/", include('rest_framework.urls',namespace='rest_framework')),
]