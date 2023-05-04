from django.db import models

class movies_dtl(models.Model):
    name=models.CharField(max_length=150)
    year=models.IntegerField()
    desc=models.TextField()
    pic=models.ImageField(upload_to='imgs')

