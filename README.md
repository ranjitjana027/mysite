# sampleapi

REST API for POST and GET to save and fetch Student data from database.

# Installation of Required Package
     pip install django
     pip install djangorestframework

# Django 

## 1. Create a django project, mysite.
     django-admin startproject mysite
## 2. Create an API app, myapi.
     python manage.py startapp myapi
## 3. Create Student Model in myapi/models.py.
     from django.db import models
     class Student(models.Model):
     name=models.CharField(max_length=64)
     age=models.IntegerField()
     std=models.CharField(max_length=10)

     def __str__(self):
         return f"Name: {self.name}, Age: {self.age}, Std: {self.std}."

## 4. Register Student Model in myapi/admin.py
     admin.site.register(Student)
## 5. Add myapi app to INSTALLED_APPS list in mysite/settings.py.
     INSTALLED_APPS=[
        'myapi.apps.MyapiConig',
        ...
     ]
## 6. Make migrations and apply this migration to database(db.sqlite3).
     python manage.py makemigrations
     python manage.py migrate
## 7. Create a super User.
     python manage.py createsuperuser

# REST Framework 

## 1. Add 'rest_framework' to INSTALLED_APPS list in mysite/settings.py.
     INSTALLED_APPS=[
        ... ,
        'rest_framework'
     ]
## 2. Create a new file serializers.py under myapi app and create a new class that link Student Model to its Serializer.
     from rest_framework import serializers
     from .models import Student

     class StudentSerializer(serializers.HyperlinkedModelSerializer):
       class Meta:
            model=Student
            fields=('name','age','std')
## 3. In myapi/views.py, Retrieve data from the database and pass into the serializer.
     from django.shortcuts import render
     from rest_framework import viewsets
     from .serializers import StudentSerializer
     from .models import Student
     class StudentViewSet(viewsets.ModelViewSet):
        queryset=Student.objects.all().order_by('name')
        serializer_class = StudentSerializer

## 4. In myapi/urls.py add urlpatterns.
     from django.urls import path, include
     from .views import StudentViewSet
     from rest_framework import routers
     router=routers.DefaultRouter()
     router.register(r'students',StudentViewSet)
     urlpatterns=[
         path("",include(router.urls)),
         path("api-auth/", include('rest_framework.urls',namespace='rest_framework')),
     ]



5. In mysite/urls.py include app urls.

     from django.contrib import admin
     from django.urls import path, include
     urlpatterns = [
     path("",include('myapi.urls')),
     path('admin/', admin.site.urls),
     ]