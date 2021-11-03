#!/usr/bin/env python3
'''
@desc    description
@author  ANGO <ango@afnor.org>
@version 0.0.1
@date    2021-10-25
@note    0.0.1 (2021-10-25) : Init file
'''

import json
from os import environ
from pathlib import Path

import requests_mock
from apps.mlb.api import Client
from config.settings import BASE_DIR
from pytest_mock import mocker


class TestApi:
    """Api  test class"""

    def test_get_date_games(self, requests_mock: requests_mock) -> None:
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

        url = f'{environ["MLB_BASE_URL"]}/api/v1/schedule/games/'

        requests_mock.get(
            url=url,
            json=json.loads(
                Path(
                    BASE_DIR.joinpath(
                        'apps/mlb/tests/samples/mbl-date-response-data.json'
                    )
                ).read_text()
            ),
        )

        api: Client = Client()
        assert api.get_date_games(25, 10, 2021) == expected_result

    def test_get_team_info(self, requests_mock: requests_mock) -> None:
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

        url = f'{environ["MLB_BASE_URL"]}/api/v1/teams/117'

        requests_mock.get(
            url=url,
            json=json.loads(
                Path(
                    BASE_DIR.joinpath('apps/mlb/tests/samples/team-117-data.json')
                ).read_text()
            ),
        )

        api: Client = Client()
        assert api.get_team_info(117) == expected_result
