import pprint
import spotipy
from spotipy.oauth2 import SpotifyOAuth

# no user credentials
# from spotipy.oauth2 import SpotifyClientCredentials
# sp = spotipy.Spotify(auth_manager=SpotifyClientCredentials(
#     client_id=CLIENT_ID, client_secret=CLIENT_SECRET))
# results = sp.search(q='weezer', limit=20)
# for idx, track in enumerate(results['tracks']['items']):
#     print(idx, track['name'])

CLIENT_ID = ""
CLIENT_SECRET = ""

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=CLIENT_ID, client_secret=CLIENT_SECRET,
                     redirect_uri="http://example.com", scope="user-library-read playlist-modify-private"))

results = sp.current_user_saved_tracks()

for idx, item in enumerate(results['items']):
    track = item['track']
    print(idx, track['artists'][0]['name'], " – ", track['name'])

# print(sp.current_user())
user_id = sp.current_user()['id']

results = sp.search(
    q='track:Love Is Embarrassing year:2023', limit=1, type='track')

pprint.pprint(results)
for idx, track in enumerate(results['tracks']['items']):
    print(idx, track['name'], track['uri'])

tracks = []
tracks.append(results['tracks']['items'][0]['uri'])

# pl = sp.user_playlist_create(user=user_id, name="test", public=False)
# print(pl["id"])
# sp.user_playlist_add_tracks(user=user_id, playlist_id=pl["id"], tracks=tracks)
