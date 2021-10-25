from django.db import models

# Create your models here.


class Team(models.Model):
    id: models.IntegerField = models.IntegerField(verbose_name="ID MLB de l'équipe")
    name: models.CharField = models.CharField(verbose_name="Nom complet de l'équipe")
    team_name: models.CharField = models.CharField(verbose_name="Nom court de l'équipe")
    location_name: models.CharField = models.CharField(
        verbose_name="Localisation de l'équipe"
    )
    abbreviation: models.CharField = models.CharField(
        verbose_name="Acronyme de l'équipe"
    )
    link: models.CharField = models.CharField(
        verbose_name="Route de l'équipe dans l'API MLB"
    )
    team_code: models.IntegerField = models.IntegerField(
        verbose_name="Team Code de l'équipe"
    )
    team_league: models.CharField = models.CharField(verbose_name="League de l'équipe")


class Game(models.Model):
    game_pk: models.IntegerField = models.IntegerField(verbose_name="ID du match")
    official_date: models.DateField = models.DateField(verbose_name="Date du match")
    home_team: models.ForeignKey = models.ForeignKey(
        Team, verbose_name="Equipe à domicile", on_delete=models.CASCADE
    )
    away_team: models.ForeignKey = models.ForeignKey(
        Team, verbose_name="Equipe à l'extérieur", on_delete=models.CASCADE
    )
    winner_team: models.ForeignKey = models.ForeignKey(
        Team, verbose_name="Vainqueur du match", on_delete=models.CASCADE
    )
    home_score: models.IntegerField = models.IntegerField(
        verbose_name="Score de l'équipe à domicile"
    )
    away_score: models.IntegerField = models.IntegerField(
        verbose_name="Score de l'équipe à l'éxtérieur"
    )
