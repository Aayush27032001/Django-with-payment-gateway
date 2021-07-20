from django.db import models

# Create your models here.

class Donate(models.Model):
    fname=models.CharField(max_length=150)
    lname=models.CharField(max_length=150)
    email=models.CharField(max_length=50)
    phone=models.CharField(max_length=12)
    date=models.DateField()

    def __str__(self):
        return self.fname+" "+ self.lname