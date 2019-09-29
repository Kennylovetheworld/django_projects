from django.db import models

class Category(models.Model) :
    name = models.CharField(max_length=128)

    def __str__(self) :
        return self.name

class Site(models.Model):
    name = models.CharField(max_length=128)
    year = models.IntegerField(null=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    description = models.CharField(max_length=1024)
    justification = models.CharField(max_length=1024)
    longitude = models.IntegerField(null=True)
    latitude = models.IntegerField(null=True)
    area_hectares = models.IntegerField(null=True)
    states = models.ForeignKey('States', on_delete=models.SET_NULL, null=True)
    region = models.ForeignKey('Region', on_delete=models.SET_NULL, null=True)
    iso = models.ForeignKey('ISO', on_delete=models.SET_NULL, null=True)

    def __str__(self) :
        return self.name

class States(models.Model):
    name = models.CharField(max_length=128)

    def __str__(self) :
        return self.name

class ISO(models.Model):
    name = models.CharField(max_length=128)

    def __str__(self) :
        return self.name

class Region(models.Model):
    name = models.CharField(max_length=128)

    def __str__(self) :
        return self.name
