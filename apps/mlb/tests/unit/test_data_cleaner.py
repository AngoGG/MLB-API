#!/usr/bin/env python3
'''
@desc    description
@author  ANGO <ango@afnor.org>
@version 0.0.1
@date    2021-10-25
@note    0.0.1 (2021-10-25) : Init file
'''

import json
from pathlib import Path
from typing import Any, Dict

from apps.mlb.utils import DataCleaner
from config.settings import BASE_DIR


class TestDataCleaner:
    """DataCleaner test class"""

    def test_game_data(self) -> None:

        expected_result = {
            "game_pk": 660900,
            "official_date": "2021-10-20",
            "home_team": 111,
            "away_team": 117,
            "winner_team": 117,
            "home_score": 1,
            "away_score": 9,
        }

        game_data: Dict[str, Any] = json.loads(
            Path(BASE_DIR.joinpath('apps/mlb/tests/samples/game-data.json')).read_text()
        )

        assert DataCleaner.get_game_data(game_data) == expected_result

    def test_team_data(self) -> None:

        expected_result = {
            "id": 117,
            "name": "Houston Astros",
            "team_name": "Astros",
            "location_name": "Houston",
            "abbreviation": "HOU",
            "link": "/api/v1/teams/117",
            "team_code": "hou",
            "team_league": "American League",
        }

        team_data: Dict[str, Any] = json.loads(
            Path(
                BASE_DIR.joinpath('apps/mlb/tests/samples/team-117-data.json')
            ).read_text()
        )

        assert DataCleaner.get_team_data(team_data) == expected_result
