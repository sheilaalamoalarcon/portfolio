from django.db import models

class imageTried(models.Model):
    image = models.ImageField(upload_to='images/')

# Create your models here.
