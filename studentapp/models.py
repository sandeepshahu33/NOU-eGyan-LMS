from django.db import models

# Create your models here.
class Response(models.Model):
    responsetype=models.CharField( max_length=100)
    name=models.CharField( max_length=100)
    program=models.CharField(max_length=100)
    branch=models.CharField(max_length=100)
    year=models.CharField(max_length=100)
    responsetext=models.CharField(max_length=2000)
    posteddate=models.CharField(max_length=30)

    def __str__(self):
        return self.name