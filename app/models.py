from django.db import models
from django.urls import reverse
# Create your models here.

class School(models.Model):
    sc_name = models.CharField(max_length=30)
    sc_loc = models.CharField(max_length=20)
    sc_principal = models.CharField(max_length=20)
    
    def __str__(self):
        return self.sc_name
    
    def get_absolute_url(self):
        return reverse('SchoolDetails',kwargs={'pk':self.pk})
    
class Student(models.Model):
    sc_name = models.ForeignKey(School, on_delete=models.CASCADE, related_name='myStudent')
    st_name = models.CharField(max_length=20)
    st_age = models.IntegerField()
    
    def __str__(self):
        return self.st_name
    
    
    