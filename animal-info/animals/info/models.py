from django.db import models

class Family(models.Model):
    name = models.CharField(max_length=100)

class Animal(models.Model):
    legs = models.IntegerField()
    weight = models.FloatField()
    height = models.FloatField()
    speed = models.FloatField()
    family = models.ForeignKey(Family, on_delete=models.CASCADE)
