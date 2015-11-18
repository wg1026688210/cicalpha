from django.db import models

# Create your models here.
class Manager(models.Model):
    def __unicode__(self):
        return self.name
    total=models.IntegerField(default=0)
    name=models.CharField(max_length=200)
    weight=models.IntegerField(default=0)

class User(models.Model):
    name =models.CharField(max_length=200)
    age =models.IntegerField()
    
        