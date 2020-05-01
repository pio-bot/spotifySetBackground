import spotipy
import spotipy.util as util
import urllib.request
import os
import ctypes


username = 'mnu543'
scope = 'user-read-currently-playing'

token = util.prompt_for_user_token(username, scope, '08a7ae778d104330854715ebdb9ab297', '1d8f3175dd3b4e5fa70c08f4ab788f5e', 'https://www.google.com/')

sp = spotipy.Spotify(auth=token)

sunny_uri = 'spotify:playlist:4GAjcWioumQ7JXbP7AiObR'
while True:
    results = sp.current_user_playing_track()
    album = results['item']['album']
    image = album['images'][0]['url']
    urllib.request.urlretrieve(image, 'Art.jpg')
    pathToJpg = os.path.normpath('C:\Python Practice\spotback\Art.jpg')
    ctypes.windll.user32.SystemParametersInfoW(20, 0, pathToJpg, 0)
