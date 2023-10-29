from django.db import models

class Branch(models.Model):
    name = models.CharField(max_length=250)
    ifsc = models.CharField(max_length=10)
    code = models.TextField(blank=True,null=True)

class Applicant(models.Model):
    name = models.CharField(max_length=250)
    dob = models.DateField(blank=True,null=True)
    age = models.IntegerField(blank=True,null=True)
    gender = models.IntegerField(blank=True,null=True)
    phone = models.IntegerField(blank=True,null=True)
    email = models.CharField(max_length=30)
    address = models.TextField(blank=True,null=True)
    district = models.IntegerField(blank=True,null=True)
    branch = models.IntegerField(blank=True,null=True)
    acctype = models.IntegerField(blank=True,null=True)
    materials = models.IntegerField(blank=True,null=True)

    def __str__(self):
        return self.name