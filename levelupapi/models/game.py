from django.db import models

class Game(models.Model):

    game_type = models.ForeignKey("GameType", on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    maker = models.CharField(max_length=30)
    gamer = models.ForeignKey("Gamer", on_delete=models.CASCADE)
    number_of_players = models.IntegerField(default=1)
    skill_level = models.IntegerField(default=1)