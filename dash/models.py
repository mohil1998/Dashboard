from django.db import models
from django.contrib.auth import get_user_model
User = get_user_model()
# Create your models here.
class FilesDB(models.Model):
    user = models.ForeignKey(User, related_name='user_groups',on_delete=models.PROTECT)
    datafile = models.FileField(null=True,blank=True)

class Dashboard(models.Model):
    dash_name = models.CharField(null=False,blank=False,max_length=30)
    description = models.TextField(blank=True, default='')
    user = models.ForeignKey(User,on_delete=models.PROTECT)

class Graph(models.Model):
    dash_name = models.ForeignKey(Dashboard,on_delete=models.PROTECT)
    datafile = models.FileField(null=True,blank=True)
    graph_type = models.CharField(max_length=10)
    x_axis = models.CharField(max_length=100)
    y_axis = models.CharField(max_length=100)
