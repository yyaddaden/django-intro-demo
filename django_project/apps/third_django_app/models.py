from django.db import models

# Create your models here.

class User(models.Model):
    id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=10)


class History(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey("User", on_delete=models.CASCADE)
    time = models.DateTimeField()
    initial_val = models.FloatField()
    final_val = models.FloatField()
    MET_CHOICES = (("C", "Celsieus"), ("F", "Fahrenheit"))
    initial_met = models.CharField(max_length=1, choices=MET_CHOICES)
    final_met = models.CharField(max_length=1, choices=MET_CHOICES)