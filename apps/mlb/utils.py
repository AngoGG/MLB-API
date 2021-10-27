#!/usr/bin/env python3
'''
@desc    description
@author  ANGO <ango@afnor.org>
@version 0.0.1
@date    2021-10-25
@note    0.0.1 (2021-10-25) : Init file
'''

from typing import Any, Dict


class DataCleaner:
    """Manages the retrieval of game data from the API for integration."""

    @staticmethod
    def get_game_data(game_data: Dict[str, Any]) -> Dict[str, Any]:
        '''From a Game API response data, retrieves need data to fill the database.

        Args:
            game (Dict[str, Any]): Dictionnary containing all API game data.

        Returns:
            Dict : A dictionnary containing all game and teams informations.
        '''

        if game_data['teams']['home']['isWinner'] is True:
            winner_team = game_data['teams']['home']['team']['id']
        else:
            winner_team = game_data['teams']['away']['team']['id']

        return {
            "game_pk": game_data['gamePk'],
            "official_date": game_data['officialDate'],
            "home_team": game_data['teams']['home']['team']['id'],
            "away_team": game_data['teams']['away']['team']['id'],
            "winner_team": winner_team,
            "home_score": game_data['teams']['home']['score'],
            "away_score": game_data['teams']['away']['score'],
        }

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
            "id": team_data['id'],
            "name": team_data['name'],
            "team_name": team_data['teamName'],
            "location_name": team_data['locationName'],
            "abbreviation": team_data['abbreviation'],
            "link": team_data['link'],
            "team_code": team_data['teamCode'],
            "team_league": team_data['league']['name'],
        }