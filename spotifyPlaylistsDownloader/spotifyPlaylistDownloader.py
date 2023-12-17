import json
import os
import shutil

import ffmpeg
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials, SpotifyOAuth
import youtube_dl as ytd


class Spotify:
    # Client ID: bec9c155c8524eb89634eb5d4f610195
    # Client Secret: ff527da25d0a4960a8b34f708887701f
    def __init__(self):
        pass

    def verifyCredentials(self, cid, secret):
        client_credentials_manager = SpotifyClientCredentials(client_id=cid,
                                                              client_secret=secret)
        sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

        return sp #Created Spotipy variable

    def selectPlaylist(self, userName):
        sp = spotipy.Spotify(auth_manager=SpotifyOAuth())

        userPlaylists = sp.user_playlist(userName)
        for playlist in userPlaylists['items']:
            print(playlist['name'])

        selectedPlaylist = input("\nEnter the playlist you wish to download: ")
        return selectedPlaylist



def main():
    print("\nWelcome to Kartik's Spotify Playlist Downloader!")
    spotify = Spotify()

    cid = input("\nEnter the spotify client ID: ")
    secret = input("\nenter the spotify Client Secret: ")
    redirectURI = input("\nEnter the redirect page(https://localhost:8888/callback) URI: ")
    userName = input("\nEnter the username: ")

    sp = spotify.verifyCredentials(cid, secret)
    print(sp)

    playList = spotify.selectPlaylist(userName)
    print(playList)


if __name__ == "__main__":
    main()