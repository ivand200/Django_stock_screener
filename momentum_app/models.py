from django.db import models


class SP500(models.Model):
    id = models.AutoField(primary_key=True)
    symbol = models.CharField(max_length=10)
    name = models.CharField(max_length=20)
    avg_momentum = models.FloatField()
    ep = models.FloatField()


class DJ30(models.Model):
    id = models.AutoField(primary_key=True)
    symbol = models.CharField(max_length=10)
    name = models.CharField(max_length=20)
    avg_momentum = models.FloatField()
    ep = models.FloatField()


class Divs(models.Model):
    id = models.AutoField(primary_key=True)
    symbol = models.CharField(max_length=10)
    name = models.CharField(max_length=20)
    div_p = models.FloatField()


class Etf(models.Model):
    id = models.AutoField(primary_key=True)
    symbol = models.CharField(max_length=10)
    name = models.CharField(max_length=20)
    momentum_12_1 = models.FloatField()
    ma10 = models.IntegerField()


class Notes(models.Model):
    id = models.AutoField(primary_key=True)
    text = models.TextField()
    user = models.CharField(max_length=30)