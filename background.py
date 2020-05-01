import spotipy
import spotipy.util as util
import urllib.request
import os
import ctypes


username = 'username'
scope = 'user-read-currently-playing'

token = util.prompt_for_user_token(username, scope, 'client-token', 'private-token', 'https://www.google.com/')

sp = spotipy.Spotify(auth=token)

while True:
    results = sp.current_user_playing_track()
    album = results['item']['album']
    image = album['images'][0]['url']
    urllib.request.urlretrieve(image, 'Art.jpg')
    pathToJpg = os.path.normpath('C:\Python Practice\spotback\Art.jpg')
    ctypes.windll.user32.SystemParametersInfoW(20, 0, pathToJpg, 0)
