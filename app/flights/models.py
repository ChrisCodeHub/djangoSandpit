from django.db import models

# Create your models here.
class Flight(models.Model):
    origin = models.CharField(max_length=64)
    destination = models.CharField(max_length=64)
    duration = models.IntegerField()

    def __str__(self):
        return f"{self.id}  {self.origin} --> {self.destination}"


"""  following model is used to hold the dynamc about us data field.  
"""
class AboutInfo(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()

    def __str__(self):
        return self.title