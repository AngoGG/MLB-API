# Considérations générales

En utilisant le template Django du pôle : https://github.com/AFNOR-PFNR/empty_django_project, créer un projet qui requête une API et récupère des données à stocker en base. Sont attendus 

- **[REQUIS]** un client d'API
- **[REQUIS]** les modèles représentant les données récupérées
- **[OPTIONNEL]** une vue pour récupérer les différentes données selon un paramètre fourni en entrée ; soit un simple paramètre en GET, soit avec un Form Django
- **[OPTIONNEL]** une vue pour afficher ces données
- **[OPTIONNEL]** une commande custom permettant de récupérer en CLI les données sur base d'un paramètre fourni en entrée

Les éléments essentiels sont les tests, le client API et les modèles. Le reste sera du bonus. Chaque élément devra être couvert par des tests, si possible en TDD. Les vues ne doivent pas être habillées, elles peuvent n'être qu'en texte brut ou en JSON.

# Considérations spécifiques

L'API à requêter sera celle de la MLB. Il est à noter qu'elle ne passe pas à travers le réseau interne. L'objectif est de récupérer les métadonnées concernant l'ensemble des matchs ayant eu lieu ou étant programmés pour une journée donnée. Pour ce faire, requêter

https://statsapi.mlb.com/api/v1/schedule/games/?sportId=1&date=%m/%d/%Y

Où `%m/%d/%Y` est la date du jour à contrôler. Attention, il s'agit bien d'un format de date à l'américaine, donc la date du jour est 10/20/2021.

Les données récupérées sont en JSON. Il est attendu de conserver les métadonnées utiles, il n'est pas nécessaire de tout stocker. Sur base de la réponse, il faudra récupérer des métadonnées générales concernant les équipes qui jouent (`id`, `name`, `link`, `teamCode`, `abbreviation`, `teamName`, `locationName`, et le nom de la league). Pour ce faire, récupérer le lien dans la liste des équipes

```json
"team":{"id":111,"name":"Boston Red Sox","link":"/api/v1/teams/111"}
```

et requêter l'URL

https://statsapi.mlb.com/api/v1/teams/111

L'objectif *in fine* sera de pouvoir récupérer les matchs soit par date, soit par équipe, soit par league.

# Bugs connus et améliorations à venir

- Erreur si aucun match ne ressort pour la date donnée.
- Erreur si un match n'a pas encore été joué (pas de vainqueur)