
from django.db import models

class Event(models.Model):

    game = models.ForeignKey("Game", on_delete=models.CASCADE)
    description = models.CharField(max_length=200)
    date= models.DateField(auto_now=True, auto_now_add=False)
    time = models.TimeField(auto_now=True, auto_now_add=False)
    organizer = models.ForeignKey("Gamer", on_delete=models.CASCADE)
    attendees = models.ManyToManyField(
        'Gamer',
        through='EventGamer',
        related_name='events'
    )
    
    @property
    def joined(self):
        return self.__joined

    @joined.setter
    def joined(self, value):
        self.__joined = value
    
# {
#     "id":7
#     "game": 1,
#     "description": "second test",
#     "date": "2345-64-78",
#     "time": "23:23:23",
#     "organizer": 1
# }