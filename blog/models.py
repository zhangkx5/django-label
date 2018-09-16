from django.db import models

# Create your models here.
class BlogsPost(models.Model):
    title = models.CharField(max_length=150)
    body = models.TextField()
    timestamp = models.DateTimeField()

class ExcelCount(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=150)
    label = models.CharField(max_length=150)
    num = models.IntegerField()
    sum = models.IntegerField()