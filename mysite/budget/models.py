from django.db import models

class Person(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    income = models.IntegerField()
    description = models.TextField(default="Enter a description...")

    def __str__(self):
        return str(self.first_name) + ' ' + str(self.last_name)


class Stock_history(models.Model):
    name = models.CharField(max_length=50)
    date = models.CharField(max_length=50)
    p_open = models.FloatField()
    high = models.FloatField()
    low = models.FloatField()
    close = models.FloatField()
    adj_close = models.FloatField()
    volume = models.IntegerField()

    class Meta:
        unique_together = ('name', 'date')

    def __str__(self):
        return str(self.name) + ' ' + str(self.date)