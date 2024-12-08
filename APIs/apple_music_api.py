import jwt
import requests
import time

class AppleMusicAPI:
    def __init__(self, team_id, key_id, private_key_path):
        self.team_id = team_id
        self.key_id = key_id
        self.private_key_path = private_key_path
        self.token = self.generate_token()

    def generate_token(self):
        with open(self.private_key_path, "r") as key_file:
            private_key = key_file.read()
        
        headers = {"alg": "ES256", "kid": self.key_id}
        payload = {
            "iss": self.team_id,
            "iat": int(time.time()),
            "exp": int(time.time()) + 3600  # 1 heure de validité
        }
        token = jwt.encode(payload, private_key, algorithm="ES256", headers=headers)
        return token

    def get_playlist(self, playlist_id, storefront="us"):
        url = f"https://api.music.apple.com/v1/catalog/{storefront}/playlists/{playlist_id}"
        headers = {"Authorization": f"Bearer {self.token}"}
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            return response.json()
        else:
            raise Exception("Failed to fetch playlist from Apple Music")
