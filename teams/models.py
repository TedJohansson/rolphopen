from django.db import models

# Create your models here.
class Player(models.Model):
    name = models.CharField(max_length=200)
    unwanted_teammates = models.ManyToManyField("self", blank=True, symmetrical=False)
    def __str__(self):
        return f"{self.name}"


class Team(models.Model):
    players = models.ManyToManyField(Player)
    year = models.IntegerField(default=2024)
    show = models.BooleanField(default=False)

class HCP(models.Model):
    player = models.ForeignKey(Player, on_delete=models.CASCADE)
    year = models.IntegerField(default=2024)
    hcp = models.FloatField()
