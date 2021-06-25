from django.db import models

class Player(models.Model):
    name = models.CharField(max_length=10)
    won = models.IntegerField(default=0)
    total_played = models.IntegerField(default=0)

    def __str__(self) -> str:
        return self.name
    
    def __eq__(self,player):
        return self._id == player._id