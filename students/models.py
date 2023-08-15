from django.db import models


class UserEnquiry(models.Model):    #contactEnquiry model name h
   fname = models.CharField(max_length=50)
   lname = models.CharField(max_length=50)
#    phone= models.CharField(max_length=12, )
   phone= models.CharField(max_length=12, )
   email=models.EmailField( max_length=64)
   city=models.CharField(max_length=25)
   text= models.TextField(max_length=200)




