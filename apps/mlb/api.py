#!/usr/bin/env python3
'''
@desc    description
@author  ANGO <ango@afnor.org>
@version 0.0.1
@date    2021-10-22
@note    0.0.1 (2021-10-22) : Init file
'''

import requests
from os import environ
from typing import Dict


class Client:
    '''Api class.
    Manages interactions with MLB API

    Attributes:
        base_url (str): MLB Api url
    '''

    def __init__(self) -> None:
        '''Constructor'''
        ...
        self.base_url: str = environ['MLB_BASE_URL']

    def _request(self, url: str, payloads: Dict = None) -> Dict:
        """Query the Api and get the response.
        Returns:
            Dict: A Dictionary containing the requests Response.
        """
        return requests.get(url, params=payloads).json()

    def get_date_games(self, day: int, month: int, year: int) -> Dict:
        '''Get all the games informations for a given date.
        Args:
            date (str): The date for which the games informations are expected

        Returns:
            Dict: A Dictionary containing the informations for all matchs on the given date.
        '''

        payloads: Dict = {
            'sportId': '1',
            'date': f'{month}/{day}/{year}',
        }
        url = f'{self.base_url}/api/v1/schedule/games/'

        return self._request(url, payloads)

    def get_team_info(self, team_id: int) -> Dict:
        '''Get all informations for a given team.
        Args:
            team_id (int): The MLB team ID.

        Returns:
            Dict: A Dictionary containing the informations for the given team.
        '''

        url = f'{self.base_url}/api/v1/teams/{team_id}'

        return self._request(url)
