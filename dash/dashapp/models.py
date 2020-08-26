from django.db import models
import datetime
from django.utils import timezone
from datetime import timedelta

# Create your models here.
class Visitor(models.Model):
    name = models.CharField(max_length=25)
    email = models.EmailField(default = None)
    Time_of_visit = models.DateTimeField('Time Visited',default=timezone.now())

    class Meta:
        verbose_name = 'Visitor'
        verbose_name_plural = 'Visitors'

    def __str__(self):
        return self.name

class Visit(models.Model):
    page_visits = models.IntegerField(default=0)
    
    def __str__(self):
        return self.page_visits
