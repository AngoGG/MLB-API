#!/usr/bin/env python3
'''
@desc    description
@author  ANGO <ango@afnor.org>
@version 0.0.1
@date    2021-11-01
@note    0.0.1 (2021-11-01) : Init file
'''
import json
from datetime import datetime
from pathlib import Path
from typing import Any, Dict

from config.settings import BASE_DIR
from django.http import HttpResponse
from django.test import Client, TestCase
from django.utils.encoding import force_text
from pytest_mock import mocker


class TestGetDateGamesView(TestCase):
    """DataCleaner test class"""

    def test_get_game_data_access(self) -> None:
        client: Client = Client()
        response: HttpResponse = client.get(
            f"/games/",
        )

        assert response.status_code == 200
        self.assertTemplateUsed(response, "mlb/get_game_from_date.html")


class TestGetDateGamesView:
    """DataCleaner test class"""

    def test_get_game_data(self, mocker: mocker) -> None:
        expected_result = {
            'games': [
                {
                    'game_infos': {
                        "game_pk": 660900,
                        "official_date": "2021-10-20",
                        "home_team": 111,
                        "away_team": 117,
                        "winner_team": 117,
                        "home_score": 1,
                        "away_score": 9,
                    },
                    'teams_infos': [
                        {
                            "id": 117,
                            "name": "Houston Astros",
                            "team_name": "Astros",
                            "location_name": "Houston",
                            "abbreviation": "HOU",
                            "link": "/api/v1/teams/117",
                            "team_code": "hou",
                            "team_league": "American League",
                        },
                        {
                            "id": 117,
                            "name": "Houston Astros",
                            "team_name": "Astros",
                            "location_name": "Houston",
                            "abbreviation": "HOU",
                            "link": "/api/v1/teams/117",
                            "team_code": "hou",
                            "team_league": "American League",
                        },
                    ],
                }
            ]
        }

        mocker.patch(
            'apps.mlb.api.Client.get_date_games',
            return_value=json.loads(
                Path(
                    BASE_DIR.joinpath(
                        'apps/mlb/tests/samples/mbl-date-response-data.json'
                    )
                ).read_text()
            ),
        )
        mocker.patch(
            'apps.mlb.api.Client.get_team_info',
            return_value=json.loads(
                Path(
                    BASE_DIR.joinpath('apps/mlb/tests/samples/team-117-data.json')
                ).read_text()
            ),
        )

        client: Client = Client()
        response: HttpResponse = client.post(
            f"/games/",
            {
                "date": [datetime.now()],
            },
        )

        assert response.status_code == 200
        assert json.loads(force_text(response.content)) == expected_result
