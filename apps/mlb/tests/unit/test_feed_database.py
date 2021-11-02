#!/usr/bin/env python3
'''
@desc    description
@author  ANGO <ango@afnor.org>
@version 0.0.1
@date    2021-11-02
@note    0.0.1 (2021-11-02) : Init file
'''
import pytest
from apps.mlb.models import Game, Team
from apps.mlb.utils import FeedDatabase
from django.db.models.query import QuerySet


class TestFeedDatabase:
    """FeedDatabase test class"""

    @pytest.mark.django_db(transaction=True)
    def test_update_game(self) -> None:

        game_data = {
            "game_pk": 660900,
            "official_date": "2021-10-20",
            "home_team": 111,
            "away_team": 117,
            "winner_team": 117,
            "home_score": 1,
            "away_score": 9,
        }
        home_team_data = {
            "id": 117,
            "name": "Houston Astros",
            "team_name": "Astros",
            "location_name": "Houston",
            "abbreviation": "HOU",
            "link": "/api/v1/teams/117",
            "team_code": "hou",
            "team_league": "American League",
        }
        away_team_data = {
            "id": 111,
            "name": "Boston Red Sox",
            "team_name": "Red Sox",
            "location_name": "Boston",
            "abbreviation": "BOS",
            "link": "/api/v1/teams/11",
            "team_code": "bos",
            "team_league": "American League",
        }

        feed_database: FeedDatabase = FeedDatabase()
        home_team = Team.objects.create(**home_team_data)
        away_team = Team.objects.create(**away_team_data)
        feed_database.update_game(game_data, home_team, away_team)
        game_created: QuerySet = Game.objects.first()

        assert game_created.game_pk == 660900

    @pytest.mark.django_db(transaction=True)
    def test_update_team(self) -> None:

        team_data = {
            "id": 117,
            "name": "Houston Astros",
            "team_name": "Astros",
            "location_name": "Houston",
            "abbreviation": "HOU",
            "link": "/api/v1/teams/117",
            "team_code": "hou",
            "team_league": "American League",
        }

        feed_database: FeedDatabase = FeedDatabase()
        team = feed_database.update_team(team_data)
        team_info: QuerySet = Team.objects.first()

        assert team_info.id == 117
        assert team.id == 117
