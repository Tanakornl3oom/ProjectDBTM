from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Customer(models.Model):
    cid = models.AutoField(primary_key=True)
    username=models.CharField(max_length=100)
    password=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    image=models.ImageField(upload_to='Customer')	
    # first_name=models.CharField(max_length=100)
    # last_name=models.CharField(max_length=100)
     
# class Seller(models.Model):
#     sid
#     username
#     password
#     name

# class Promotion(models.Model):
#     pid
#     subject
#     content
#     image_promotion
#     type_promotion
#     startdate
#     enddate
#     promoter

# class Interest(models.Model):
#     iid
#     pid
#     cid 
#     location
#     status