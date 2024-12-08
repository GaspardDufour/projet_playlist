from spotipy import Spotify
from spotipy.oauth2 import SpotifyClientCredentials

class SpotifyAPI:
    def __init__(self, client_id, client_secret):
        # Configuration de l'authentification via Spotipy
        self.auth_manager = SpotifyClientCredentials(client_id=client_id, client_secret=client_secret)
        self.spotify = Spotify(auth_manager=self.auth_manager)

    def create_playlist(self, name, description=""):
        user_id = self.spotify.me()["id"]  # Nécessite l'authentification utilisateur
        playlist = self.spotify.user_playlist_create(user_id, name, description=description)
        return playlist["id"]

    def add_tracks_to_playlist(self, playlist_id, track_titles):
        track_ids = []
        for title in track_titles:
            search_result = self.spotify.search(q=title, type="track", limit=1)
            if search_result["tracks"]["items"]:
                track_ids.append(search_result["tracks"]["items"][0]["id"])
        self.spotify.playlist_add_items(playlist_id, track_ids)

    def get_playlist_tracks(self, playlist_id):
        """Récupère les morceaux d'une playlist Spotify."""
        results = self.spotify.playlist_tracks(playlist_id)
        tracks = []
        for item in results['items']:
            track = item['track']
            tracks.append({
                'name': track['name'],
                'artist': track['artists'][0]['name'],
                'album': track['album']['name'],
                'id': track['id']
            })
        return tracks
