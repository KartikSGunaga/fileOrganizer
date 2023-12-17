import pprint, base64, os

import spotipy
import requests, json
from requests import post
from spotipy.oauth2 import SpotifyClientCredentials
from spotipy.oauth2 import SpotifyOAuth
# import dotenv
# from dotenv import load_dotenv
#
# load_dotenv()

clientID = os.getenv("CLIENT_ID")
clientSecret = os.getenv("CLIENT_SECRET")
class Spotify:
    def __init__(self, name):
        self.username = name

    def getToken(self, clientID, clientSecret):
        authString = f"{clientID}:{clientSecret}"
        authBytes = authString.encode("utf-8")
        authBase64 = str(base64.b64encode(authBytes), "utf-8")

        url = "https://accounts.spotify.com/api/token"
        headers = {
            "Authorization": "Basic " + authBase64,
            "Content-Type": "application/x-www-form-urlencoded"
        }

        data = {"grant_type": "client_credentials"}
        result = post(url, headers=headers, data= data)
        try:
            jsonResult = result.json()
            token = jsonResult['access_token']
            return token
        except (json.JSONDecodeError, KeyError):
            print("Error: Unable to retrieve access token.")
            return None

    def getAuthHeader(self, token):
        return {"Authorization": "Bearer " + token}

    def showUserPlaylist(self, username):
        sp = spotipy.Spotify(auth_manager=SpotifyOAuth())
        playlists = sp.user_playlist(username)
        allPlaylists = []

        for playlist in playlists["items"]:
            allPlaylists.append(playlist["name"])
            print(playlist["name"])

        return allPlaylists

    def showUserDetails(self):
        clientCredentialsManager = SpotifyClientCredentials()
        sp = spotipy.Spotify(client_credentials_manager=clientCredentialsManager)

        sp.trace = True
        user = sp.user(self.username)
        pprint.pprint(user)


def main():
    print("\nWelcome to Kartik's Spotify downloader!")

    username = "93ouloy2o81gxtb75q0fsa0od" #input("\nEnter the username: ")
    spotify = Spotify(username)

    # cid = "bec9c155c8524eb89634eb5d4f610195" #input("\nEnter the Client ID:")
    # clientSecret = "ff527da25d0a4960a8b34f708887701f" #input("\nEnter the client secret: ")

    token = spotify.getToken(clientID, clientSecret)
    print(f"Token:  {token}")

    authHeader = spotify.getAuthHeader(token)
    print(f"Suth Header: {authHeader}")
    spotify.showUserDetails()

if __name__ == "__main__":
    main()