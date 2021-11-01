from django.http import HttpRequest, HttpResponse, JsonResponse
from django.shortcuts import render
from django.views.generic import View

from apps.mlb.api import Client
from apps.mlb.utils import DataCleaner


from .forms import DesiredGamesDateForm


class GetDateGames(View):
    def get(self, request: HttpRequest) -> HttpResponse:
        '''Displays an HTML page with a form allowing to choose the retrieval date for MLB games.'''
        return render(
            request, "mlb/get_game_from_date.html", {"form": DesiredGamesDateForm()}
        )

    def post(self, request: HttpRequest) -> JsonResponse:
        '''Returns all the games informations with its
        involved teams from a date given in parameters

        Returns:
            Dict: A Dictionary containing games and teams informations.
        '''

        # Will now take params from Django form
        day = request.GET['day']
        month = request.GET['month']
        year = request.GET['year']

        mlb_api: Client = Client()
        data = mlb_api.get_date_games(day, month, year)

        data_cleaner: DataCleaner = DataCleaner()

        games = []
        for game in data['dates'][0]['games']:
            game_infos = data_cleaner.get_game_data(game)

            home_team_infos = data_cleaner.get_team_data(
                mlb_api.get_team_info(game_infos['home_team'])
            )
            away_team_infos = data_cleaner.get_team_data(
                mlb_api.get_team_info(game_infos['away_team'])
            )

            games.append(
                {
                    'game_infos': game_infos,
                    'teams_infos': [home_team_infos, away_team_infos],
                },
            )

        return JsonResponse({'games': games})
