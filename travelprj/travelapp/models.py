from django.db import models

class Locations(models.Model):
    name=models.CharField(max_length=150)
    img=models.ImageField(upload_to="pics")
    desc=models.TextField()

class Team(models.Model):
    name=models.CharField(max_length=150)
    img=models.ImageField(upload_to="pics")
    role=models.TextField()
