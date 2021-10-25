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

from apps.api.data_cleaner import DataCleaner
from config.settings import BASE_DIR


class TestDataCleaner:
    """DataCleaner test class"""

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
                BASE_DIR.joinpath('apps/api/tests/samples/team-117-data.json')
            ).read_text()
        )

        assert DataCleaner.get_team_data(team_data) == expected_result
