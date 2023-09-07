from django.db import models


class Product(models.Model):
    title = models.CharField(max_length=500)
    link = models.CharField(max_length=500)
