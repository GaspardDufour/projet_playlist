import requests

class DeezerAPI:
    BASE_URL = "https://api.deezer.com"

    def get_playlist(self, playlist_id):
        url = f"{self.BASE_URL}/playlist/{playlist_id}"
        response = requests.get(url).json()
        
        sons = []

        for track in response['tracks']['data'] :
            title = track.get('title')
            artist = track.get('artist', {}).get('name')
            album = track.get('album', {}).get('title')
            sons.append({'title' : title, 'artist' : artist, 'album' : album})
        return sons
