from django.db import models

# Create your models here.
class Material(models.Model):
    mid=models.AutoField(primary_key=True)
    program=models.CharField(max_length=100)
    branch=models.CharField(max_length=100)
    year=models.CharField(max_length=100)
    subject=models.CharField(max_length=100)
    materialtype=models.CharField(max_length=100)
    filename=models.CharField(max_length=100)
    myfile=models.FileField(upload_to='')

    def __srt__(self):
        return f"{self.program} {self.branch}"

