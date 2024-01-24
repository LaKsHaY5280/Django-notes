from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Person(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL,null=True,blank=True )
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    email = models.EmailField(max_length=254)
    
class Department(models.Model):
    department = models.CharField(max_length=10)
    
    def __str__(self) -> str:
        return self.department
    
    class Meta:
        ordering = ['department']
        

class StudentID(models.Model):
    student_id = models.CharField(max_length=10)
    
    def __str__(self) -> str:
        return self.student_id
    

class Student(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL,null=True,blank=True )
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    email = models.EmailField(unique=True)
    department = models.ForeignKey(Department, on_delete=models.SET_NULL,null=True,blank=True )
    student_id = models.OneToOneField(StudentID, on_delete=models.CASCADE )
    
    def __str__(self) -> str:
        return self.name
    
    class Meta:
        ordering = ['name']
        verbose_name = 'student'
