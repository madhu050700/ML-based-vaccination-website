from django.db import models


# Create your models here.
class Reports(models.Model):
    pname = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    mobileno = models.CharField(max_length=25)
    bloodgroup = models.CharField(max_length=25)
    locationinfo = models.CharField(max_length=100)
    pwd=models.CharField(max_length=100)
    disease = models.IntegerField()
    ailments = models.IntegerField()
    age=models.IntegerField()
    class Meta:
        db_table="reports"

class temp_measure(models.Model):
    temperature = models.CharField(max_length=100)

    def __str__(self):
        return self.temperature
    class Meta:
        db_table = "temp_measurement"

class heart_measure(models.Model):
    heartbeat = models.CharField(max_length=100)
    class Meta:
        db_table = "heart_measurement"
