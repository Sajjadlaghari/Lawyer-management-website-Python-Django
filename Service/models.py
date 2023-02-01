from django.db import models

class Service(models.Model):
    service_title = models.CharField(max_length=50)
    service_des = models.CharField(max_length=230)
    service_icon = models.CharField(max_length=230)
# Create your models here.
