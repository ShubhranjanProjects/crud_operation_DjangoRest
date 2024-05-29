from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Products(models.Model):
    id=models.AutoField(primary_key=True,editable=False)
    name=models.CharField(max_length=50)
    category=models.CharField(max_length=50)
    price=models.IntegerField(null=True,blank=True)
    createdAt=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return (self.name)



