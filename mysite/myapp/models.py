from django.db import models

class employee(models.Model):
    First_name = models.CharField(max_length=50)
    Last_name = models.CharField(max_length=50)
    Email_id = models.EmailField(max_length=50)
    Phone_no = models.CharField(max_length=11)


# Create your models here.
