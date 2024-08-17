from django.db import models

# Create your models here.
class CrudModel(models.Model):
    name = models.CharField(max_length=40)
    book = models.CharField(max_length=50)
    game = models.CharField(max_length=50)
    
def __str__(self):
    return self.__str__
    
    