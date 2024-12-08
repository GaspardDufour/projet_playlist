import requests

class DeezerAPI:
    BASE_URL = "https://api.deezer.com"

    def get_playlist(self, playlist_id):
        url = f"{self.BASE_URL}/playlist/{playlist_id}"
        response = requests.get(url)
        if response.status_code == 200:
            return response.json()
        else:
            raise Exception("Failed to fetch playlist from Deezer")
