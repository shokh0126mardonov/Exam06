from django.db import models
from games.models import Game
from players.models import Player

# Create your models here.

class Score(models.Model):
    CHOICES = [
        ['win','Win'],
        ['loss','Loss'],
        ['draw','Draw'],
    ]
    game = models.ForeignKey(Game,on_delete=models.PROTECT)
    player = models.ForeignKey(Player,on_delete=models.PROTECT)
    result = models.CharField(max_length=50,choices=CHOICES)
    points = models.IntegerField()
    opponent_name = models.CharField(max_length=50,blank=True,null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return 