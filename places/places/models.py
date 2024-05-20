from django.db import models

class Place(models.Model):
    name = models.CharField(name=50)

    def __str__(self):
        return self.name