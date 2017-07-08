from django.db import models

class Year(models.Model):
    name = models.CharField(max_length=150)
    room = models.CharField(max_length=150)

    def __str__(self):
        return self.name + ': ' + self.room


class Week(models.Model):
    Year = models.ForeignKey(Year, on_delete=models.CASCADE)
    week_num = models.IntegerField()
    washer = models.CharField(max_length=100)

    def __str__(self):
        return str(self.week_num)

