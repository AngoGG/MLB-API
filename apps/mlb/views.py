from django.views.generic import View


class GetDateGames(View):
    def get(self, request):
        '''Returns all the games informations with its
        involved teams from a date given in parameters

        Returns:
            Dict: A Dictionary containing games and teams informations.
        '''

        pass
