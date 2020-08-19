from django.db import models

class About(models.Model):
    title = models.CharField(max_length=100)
    subtitle = models.CharField(max_length=100)
    author = models.CharField(max_length=50)
    text = models.CharField(max_length=10000000)

class Boletim(models.Model):
    title = models.CharField(max_length=100)
    subtitle = models.CharField(max_length=100)
    author = models.CharField(max_length=50)
    text = models.CharField(max_length=10000000)

class General(models.Model):
    title = models.CharField(max_length=100)
    subtitle = models.CharField(max_length=100)
    author = models.CharField(max_length=50)
    text = models.CharField(max_length=10000000)

