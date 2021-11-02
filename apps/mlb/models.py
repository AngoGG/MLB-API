from django.db import models

# Create your models here.


class Team(models.Model):
    id: models.IntegerField = models.IntegerField(
        verbose_name="ID MLB de l'équipe", primary_key=True
    )
    name: models.CharField = models.CharField(
        verbose_name="Nom complet de l'équipe", max_length=255
    )
    team_name: models.CharField = models.CharField(
        verbose_name="Nom court de l'équipe", max_length=255
    )
    location_name: models.CharField = models.CharField(
        verbose_name="Localisation de l'équipe", max_length=255
    )
    abbreviation: models.CharField = models.CharField(
        verbose_name="Acronyme de l'équipe", max_length=255
    )
    link: models.CharField = models.CharField(
        verbose_name="Route de l'équipe dans l'API MLB", max_length=255
    )
    team_code: models.IntegerField = models.IntegerField(
        verbose_name="Team Code de l'équipe"
    )
    team_league: models.CharField = models.CharField(
        verbose_name="League de l'équipe", max_length=255
    )


class Game(models.Model):
    game_pk: models.IntegerField = models.IntegerField(
        verbose_name="ID du match", primary_key=True
    )
    official_date: models.DateField = models.DateField(verbose_name="Date du match")
    home_team: models.ForeignKey = models.ForeignKey(
        Team,
        verbose_name="Equipe à domicile",
        related_name="home_team",
        on_delete=models.CASCADE,
    )
    away_team: models.ForeignKey = models.ForeignKey(
        Team,
        verbose_name="Equipe à l'extérieur",
        related_name="away_team",
        on_delete=models.CASCADE,
    )
    winner_team: models.ForeignKey = models.ForeignKey(
        Team,
        verbose_name="Vainqueur du match",
        related_name="winner_team",
        on_delete=models.CASCADE,
        null=True,
        blank=True,
    )
    home_score: models.IntegerField = models.IntegerField(
        verbose_name="Score de l'équipe à domicile"
    )
    away_score: models.IntegerField = models.IntegerField(
        verbose_name="Score de l'équipe à l'éxtérieur"
    )
