from django.db import models


class Person(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()

    def __str__(self):
        return self.first_name + '_' + self.last_name


class Log(models.Model):
    path = models.CharField(max_length=400)
    method = models.CharField(max_length=100)
    timestamp = models.TimeField()

    def __str__(self):
        return self.timestamp + '_' + self.path
