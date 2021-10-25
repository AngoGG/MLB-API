#!/usr/bin/env python3
'''
@desc    description
@author  ANGO <ango@afnor.org>
@version 0.0.1
@date    2021-10-25
@note    0.0.1 (2021-10-25) : Init file
'''

from typing import Any, Dict, List


class DataCleaner:
    """Manages the retrieval of game data from the API for integration."""

    def get_game_data(self, game: Dict[str, Any]) -> Dict[str, Dict]:
        '''From a Game API response data, retrieves need data to fill the database.

        Args:
            game (Dict[str, Any]): Dictionnary containing all API game data.

        Returns:
            Dict : A dictionnary containing all game and teams informations.
        '''
        pass

    @staticmethod
    def get_team_data(team_data: Dict[str, Any]) -> Dict[str, Any]:
        '''From a MLB Team response API, retrieves and return data needed.

        Args:
            team_data (Dict[str, Any]): MLB response API for a Team.

        Raises:
        Returns:
            Dict : A dictionnary containing all need team data.
        '''

        return {
            "id": team_data['teams'][0]['id'],
            "name": team_data['teams'][0]['name'],
            "team_name": team_data['teams'][0]['teamName'],
            "location_name": team_data['teams'][0]['locationName'],
            "abbreviation": team_data['teams'][0]['abbreviation'],
            "link": team_data['teams'][0]['link'],
            "team_code": team_data['teams'][0]['teamCode'],
            "team_league": team_data['teams'][0]['league']['name'],
        }
