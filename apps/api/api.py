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


class Api:
    '''Api class.
    Manages interactions with MLB API

    Attributes:
        base_url (str): MLB Api url
    '''

    def __init__(self) -> None:
        '''Constructor'''
        ...
        self.base_url: str = environ['MLB_BASE_URL']

    def _request(self, url: str, payloads=Dict) -> Dict:
        """Query the Api and get the response.
        Returns:
            Dict: A Dictionary containing the requests Response.
        """
        return requests.get(url, params=payloads).json()
