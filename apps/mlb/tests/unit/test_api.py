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

from apps.mlb.api import Client
from config.settings import BASE_DIR
from pytest_mock import mocker


class TestApi:
    """Api  test class"""

    def test_get_date_games(self, mocker: mocker) -> None:
        '''Method Description.
        Description details here (if needed).

        Args:
            name (type): Description. Default to False.

        Raises:
        Returns:
        '''
        expected_result = json.loads(
            Path(
                BASE_DIR.joinpath('apps/mlb/tests/samples/mbl-date-response-data.json')
            ).read_text()
        )

        mocker.patch(
            'requests.Response.json',
            return_value=json.loads(
                Path(
                    BASE_DIR.joinpath(
                        'apps/mlb/tests/samples/mbl-date-response-data.json'
                    )
                ).read_text()
            ),
        )

        api: Client = Client()
        assert api.get_date_games(20, 10, 2021) == expected_result

    def test_get_team_info(self, mocker: mocker) -> None:
        '''Method Description.
        Description details here (if needed).

        Args:
            name (type): Description. Default to False.

        Raises:
        Returns:
        '''

        expected_result = json.loads(
            Path(
                BASE_DIR.joinpath('apps/mlb/tests/samples/team-117-data.json')
            ).read_text()
        )

        mocker.patch(
            'requests.Response.json',
            return_value=json.loads(
                Path(
                    BASE_DIR.joinpath('apps/mlb/tests/samples/team-117-data.json')
                ).read_text()
            ),
        )

        api: Client = Client()
        assert api.get_team_info(117) == expected_result
