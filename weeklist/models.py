from django.db import models

class Year(models.Model):
    name = models.CharField(max_length=150)
    room = models.CharField(max_length=150)


class Week(models.Model):
    week_num = models.IntegerField(max_length=52)
    washer = models.CharField(max_length=100)

