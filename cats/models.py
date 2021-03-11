from django.db import models


class Cat(models.Model):
    name = models.CharField(max_length=16)
    color = models.CharField(max_length=16)
    birthday = models.DateField()

    def __str__(self):
        return self.name
