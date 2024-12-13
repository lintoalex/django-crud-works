from django.db import models

class Employee(models.Model):

 name=models.CharField(max_length=200)
 
 email=models.EmailField()
 
 address=models.TextField()
 
 gender_option=(
    ("male","male"),
    ("female","female")
    )
 
 gender_type=models.CharField(max_length=200,choices=gender_option,default="male")
 
 salary=models.PositiveIntegerField()
 
 department=models.CharField(max_length=200)
 
 date_of_join=models.DateField()
 
 age=models.PositiveIntegerField()
 
 picture=models.ImageField(upload_to="employee",null=True,blank=True)
