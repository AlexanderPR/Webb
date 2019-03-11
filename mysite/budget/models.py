from django.db import models

class Person(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    income = models.IntegerField()
    description = models.TextField(default="Enter a description...")

    def __str__(self):
        return str(self.first_name) + ' ' + str(self.last_name)