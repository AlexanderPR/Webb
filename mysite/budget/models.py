from django.db import models

class Person(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    income = models.IntegerField()
    description = models.TextField(default="Enter a description...")

    def __str__(self):
        return str(self.first_name) + ' ' + str(self.last_name)


class Stock_history(models.Model):
    _name = models.CharField(max_length=50)
    _date = models.CharField(max_length=50)
    _open = models.FloatField()
    _high = models.FloatField()
    _low = models.FloatField()
    _close = models.FloatField()
    _adj_close = models.FloatField()
    _volume = models.IntegerField()

    class Meta:
        unique_together = ('_name', '_date')

    def __str__(self):
        return str(self._name) + ' ' + str(self._date)