from APIs import SpotifyAPI
from APIs import DeezerAPI
def main():
    # Initialisation des API
    spotify = SpotifyAPI(client_id="client_id", client_secret="client_secret")
    print("SpotifyAPI: True")
    deezer = DeezerAPI()
    print("DeezerAPI: True")
    
    # Récupération des morceaux d'une playlist Spotify
    spotify_playlist_id = "3HANrwfRethvYLFdFH2xAI"  # Exemple de playlist Spotify
    spotify_tracks = spotify.get_playlist_tracks(spotify_playlist_id)
    print("\nChansons Spotify : ", spotify_tracks)

    # Récupération des morceaux d'une playlist Deezer
    deezer_playlist_id = "6595014704"  # Exemple de playlist Deezer
    deezer_tracks = deezer.get_playlist(deezer_playlist_id)
    print("\nChansons Deezer : ", deezer_tracks)

    # Combiner les chansons des deux playlists
    all_tracks = []

    # Ajouter les morceaux de Spotify
    for track in spotify_tracks:
        all_tracks.append({
            "title": track["title"],
            "artist": track["artist"],
            "album": track["album"]
        })

    # Ajouter les morceaux de Deezer
    for track in deezer_tracks:
        all_tracks.append({
            "title": track[""],
            "artist": track["artist"],
            "album": track["album"]
        })

    # Afficher les chansons combinées
    print("\nChansons combinées :")
    for track in all_tracks:
        print(f"{track['title']} by {track['artist']} from album {track['album']}")

    # (Optionnel) Créer une nouvelle playlist sur Spotify ou Deezer
    #create_playlist_on_spotify = True  # Changez à False si vous voulez utiliser Deezer
    """if create_playlist_on_spotify:
        # Créer une nouvelle playlist sur Spotify
        spotify_playlist_name = "Combined Playlist"
        new_playlist_id = spotify.create_playlist(spotify_playlist_name, description="Playlist combinée de Spotify et Deezer")
        spotify.add_tracks_to_playlist(new_playlist_id, [track['title'] for track in all_tracks])
        print(f"Nouvelle playlist créée sur Spotify avec ID : {new_playlist_id}")
    else:
        # Créer une nouvelle playlist sur Deezer
        print("Création de playlists sur Deezer non encore implémentée.")
"""
if __name__ == "__main__":
    main()
