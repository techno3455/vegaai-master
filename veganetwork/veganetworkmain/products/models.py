from django.db import models


class Product(models.Model):
    title = models.CharField(max_length=200)
    image = models.CharField(max_length=200)
    #description = models.CharField(max_length=300)
    likes = models.PositiveIntegerField(default=0)


class User(models.Model):
    pass

class Experiment(models.Model):
    title = models.CharField(max_length=200)
    image = models.CharField(max_length=200)
    description = models.CharField(max_length=300)
    likes = models.PositiveIntegerField(default=0)