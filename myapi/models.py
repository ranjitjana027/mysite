from django.db import models

# Create your models here.

class Student(models.Model):
    name=models.CharField(max_length=64)
    age=models.IntegerField()
    std=models.CharField(max_length=10)

    def __str__(self):
        return f"Name: {self.name}, Age: {self.age}, Std: {self.std}."
