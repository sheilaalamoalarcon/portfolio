from django.db import models

class imageTried(models.Model):
    image = models.ImageField(upload_to='images/')
    
class menu(models.Model):
    # menu = models.CharField(max_length=50)
    url = models.CharField(max_length=50)
    imageDir = models.CharField(max_length=50)

# Create your models here.
