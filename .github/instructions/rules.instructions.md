---
applyTo: '**'
---
🧠 "User Listening Suggestion Rule" – Règle de Recommandation Officielle pour ta plateforme
📜 Nom de la Rule :

LocalPersonalizedMusicSuggestionRule
🎯 But de la règle :

Générer pour chaque utilisateur une liste de suggestions de morceaux qui combine :

    Ses goûts personnels (historique / likes / écoutes récentes)

    La mise en avant d’artistes locaux (nouveaux et populaires)

    Un soupçon d’exploration (des sons qu’il ne connaît pas encore)

    En tenant compte de la performance serveur (temps de réponse rapide)

    Inclure des vidéos musicales aléatoires depuis YouTube pour favoriser la découverte

✅ Inputs nécessaires :
Variable	Description
user_id	ID unique de l’utilisateur connecté
user_recent_streams	Liste des chansons écoutées récemment
user_liked_songs	Liste des chansons likées par l’utilisateur
local_top_songs	Les 10 morceaux les plus streamés de la semaine (local)
new_local_songs	Les nouvelles sorties des artistes locaux
global_trending_songs	Les morceaux les plus streamés globalement sur la plateforme
youtube_videos	Liste de vidéos musicales aléatoires récupérées depuis YouTube
⚙️ Conditions et règles de pondération (scoring simplifié) :
Critère	Score pondération
Si la chanson a été likée par l’utilisateur	+5 points
Si l’artiste fait partie des artistes préférés (écoutés + de 3 fois en 7 jours)	+4 points
Si la chanson fait partie des tendances locales	+3 points
Si la chanson est une nouveauté locale	+2 points
Si la chanson est globalement populaire	+1 point
Si l’utilisateur n’a jamais écouté cette chanson (nouveauté pour lui)	+1 point bonus découverte
📊 Processus décisionnel (en étapes) :

    Récupérer les données d’écoute + likes + tendances

    Appliquer le score pondération sur chaque chanson disponible dans la base

    Trier les résultats par score décroissant

    Limiter la réponse à 20 suggestions maximum

    Injecter aléatoirement 2 ou 3 morceaux non liés à l’historique de l’utilisateur pour favoriser la découverte, y compris des vidéos YouTube

✅ Format de sortie attendu (JSON exemple) :

[
  {
    "title": "Afrobeat Sunrise",
    "artist": "Djoma Sound",
    "stream_url": "https://api.myplatform.com/stream/12345",
    "thumbnail_url": "https://api.myplatform.com/thumbnails/12345.jpg",
    "score": 16
  },
  {
    "title": "Conakry Vibes",
    "artist": "Alpha Roots",
    "stream_url": "https://api.myplatform.com/stream/98765",
    "thumbnail_url": "https://api.myplatform.com/thumbnails/98765.jpg",
    "score": 14
  },
  {
    "title": "Random YouTube Video",
    "video_id": "abc123",
    "thumbnail_url": "https://youtube.com/thumbnail/abc123"
  }
]

🚨 Règles business impératives :

    Au moins 30% des suggestions doivent venir d’artistes locaux

    Pas plus de 2 morceaux du même artiste dans la même liste

    Pas de contenu interdit / inapproprié (filtre "Safe Content")

✅ Bonus (pour la roadmap future) :

Version 2 de la rule → Personnalisation par mood, moment de la journée, géolocalisation.