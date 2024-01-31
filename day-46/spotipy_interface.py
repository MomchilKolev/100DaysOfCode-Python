from dotenv import load_dotenv
import spotipy
from spotipy.oauth2 import SpotifyOAuth


class SpotipyInterface:
    # Get Spotify Credentials
    def __init__(self, input_date, input_datetime):
        self.user = ""
        self.input_date = input_date
        self.input_datetime = input_datetime
        self.playlist_name = f"{self.input_date} Billboard"
        self.playlist_id = ""
        self.playlist = []
        self.scope = "playlist-modify-private playlist-read-private"

        load_dotenv()
        self.sp = spotipy.Spotify(auth_manager=SpotifyOAuth(scope=self.scope))
        self.user = self.sp.me()['id']


    def add_track_uris(self, tracks):
        """For every track in tracks, add spotify uri"""
        for entry in tracks:
            try:
                response = self.sp.search(q=f"track={entry['title']}&year"
                                           f"={self.input_datetime.year}",
                                     limit=1,
                                     type="track")
                # print("response", response)
                track_uri = response["tracks"]["items"][0]["uri"]
                self.playlist.append(track_uri)
            except BaseException as error:
                print("error:", error)
        [print(item) for item in self.playlist]

    def create_playlist(self):
        """Create or reuse Spotify playlist"""
        # Check if playlist exists
        try:
            # if yes, use it
            playlists = self.sp.user_playlists(user=self.user)["items"]
            playlist_match = [playlist for i, playlist in enumerate(playlists) if
                              playlist["name"] ==
                              self.playlist_name]
            print(playlist_match)
            self.playlist_id = playlist_match[0]["id"]
            print("Using existing playlist")
        except IndexError as error:
            print("Creating playlist")
            # else create a new playlist
            response = self.sp.user_playlist_create(user=self.user, name=f"{self.playlist_name}",
                                               public=False)
            self.playlist_id = response["id"]

    def add_tracks(self):
        """Add tracks to Spotify playlist"""
        try:
            self.sp.playlist_add_items(playlist_id=self.playlist_id, items=self.playlist)
        except BaseException as error:
            print("Error: ", error)