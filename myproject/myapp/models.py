from django.db import models


class StudentModel(models.Model):
    StudentName = models.CharField(max_length=100)
    StudentId = models.CharField(max_length=50)
    Department = models.CharField(max_length=50)
    Mobile = models.CharField(max_length=15)
    Date_of_Birth = models.DateField()
    Age = models.IntegerField(blank=True, null=True)
    Address= models.TextField()

    
   

