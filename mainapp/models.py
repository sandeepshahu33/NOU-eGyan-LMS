from django.db import models

# Create your models here.
class Enquiry(models.Model):
    name=models.CharField(max_length=50)
    gender=models.CharField(max_length=6)
    address=models.TextField()
    contactno=models.CharField(max_length=15)
    emailaddress=models.CharField(max_length=50)
    enquirytext=models.TextField()
    posteddate=models.CharField(max_length=30)


class StudentInfo(models.Model):
    rollno=models.IntegerField(primary_key=True)
    name=models.CharField(max_length=50)
    fname=models.CharField(max_length=50)
    mname=models.CharField(max_length=50)
    gender=models.CharField(max_length=6)
    address=models.TextField()
    program=models.CharField(max_length=100)
    branch=models.CharField(max_length=100)
    year=models.CharField(max_length=100)
    contactno=models.CharField(max_length=15)
    emailaddress=models.EmailField(max_length=50)
    regdate=models.CharField(max_length=30)

class LoginInfo(models.Model):
    username=models.CharField(max_length=50, primary_key=True)
    password=models.CharField(max_length=30)
    usertype=models.CharField(max_length=30)
