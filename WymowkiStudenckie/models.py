from django.db import models

class Wymowka(models.Model):
    Tresc = models.CharField(max_length=200)
    Ocena = models.FloatField()
    IloscOcen = models.IntegerField()

    def __str__(self):
        return self.Tresc