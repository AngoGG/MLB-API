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
    """Manages the retrieval of game data from the API for integration.

    """

    def get_game_data(self, game: Dict[str, Any]) -> Dict[str, Dict]:
        '''From a Game API response data, retrieves need data to fill the database.
        
        Args:
            game (Dict[str, Any]): Dictionnary containing all API game data.

        Returns:
            Dict : A dictionnary containing all game and teams informations.
        '''
        pass
