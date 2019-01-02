from django.db import models

class CricketTeamModel(models.Model):

    team_id             =     models.BigAutoField(primary_key=True)
    team_name           =     models.CharField(max_length=100)
    team_captain        =     models.CharField(max_length=100)


    def __str__(self):
        return self.team_name
