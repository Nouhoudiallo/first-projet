from googleapiclient.discovery import build
import random
import json


# Clé API YouTube (remplacez par votre clé API)
YOUTUBE_API_KEY = "AIzaSyAErCbf81jb8YLYe7hZMRXsKyPWbhTrtw8"

def load_data():
    # Simuler les données nécessaires
    return {
        "user_recent_streams": ["song1", "song2", "song3"],
        "user_liked_songs": ["song1", "song4"],
        "local_top_songs": ["song5", "song6", "song7"],
        "new_local_songs": ["song8", "song9"],
        "global_trending_songs": ["song10", "song11"]
    }

def get_random_music_videos():
    youtube = build("youtube", "v3", developerKey=YOUTUBE_API_KEY)
    
    # Rechercher des vidéos musicales aléatoires
    search_query = random.choice(["music", "pop", "rock", "jazz", "hip-hop", "afrobeat"])
    request = youtube.search().list(
        part="snippet",
        q=search_query,
        type="video",
        videoCategoryId="10",  # Catégorie "Musique"
        maxResults=5
        
    )
    response = request.execute()
    
    # Extraire les informations des vidéos
    videos = []
    for item in response["items"]:
        videos.append({
            "title": item["snippet"]["title"],
            "video_id": item["id"]["videoId"],
            "thumbnail_url": item["snippet"]["thumbnails"]["high"]["url"]
        })
    return videos

def calculate_scores(data):
    # Appliquer les pondérations pour chaque chanson
    scores = {}
    for song in set(data["user_recent_streams"] + data["user_liked_songs"] +
                    data["local_top_songs"] + data["new_local_songs"] +
                    data["global_trending_songs"]):
        scores[song] = 0
        if song in data["user_liked_songs"]:
            scores[song] += 5
        if song in data["user_recent_streams"]:
            scores[song] += 4
        if song in data["local_top_songs"]:
            scores[song] += 3
        if song in data["new_local_songs"]:
            scores[song] += 2
        if song in data["global_trending_songs"]:
            scores[song] += 1
    return scores

def generate_suggestions(data, youtube_videos):
    scores = calculate_scores(data)
    # Trier les chansons par score décroissant
    sorted_songs = sorted(scores.items(), key=lambda x: x[1], reverse=True)
    
    # Séparer les chansons locales et globales
    local_songs = [song for song, score in sorted_songs if song in data["local_top_songs"] or song in data["new_local_songs"]]
    global_songs = [song for song, score in sorted_songs if song not in local_songs]
    
    # Respecter la règle des 30% d'artistes locaux
    num_local_songs = max(2, int(0.3 * 20))  # Au moins 30% (6 chansons si 20 suggestions)
    selected_local_songs = local_songs[:num_local_songs]
    
    # Compléter avec des chansons globales
    remaining_slots = 20 - len(selected_local_songs)
    selected_global_songs = global_songs[:remaining_slots]
    
    # Ajouter des vidéos YouTube pour la découverte
    youtube_suggestions = youtube_videos[:2]  # Ajouter 2 vidéos aléatoires
    
    # Combiner les suggestions
    final_suggestions = selected_local_songs + selected_global_songs + youtube_suggestions
    
    # Limiter à 20 suggestions
    return json.dumps(final_suggestions[:20], indent=2)

if __name__ == "__main__":
    # Charger les données
    data = load_data()
    
    # Récupérer des vidéos YouTube
    youtube_videos = get_random_music_videos()
    
    # Générer les suggestions
    suggestions = generate_suggestions(data, youtube_videos)
    print("Suggestions finales :")
    print(suggestions)