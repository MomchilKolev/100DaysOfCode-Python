from billboard import Billboard
from spotipy_interface import SpotipyInterface

from datetime import datetime

# Verify Date is valid
try:
    # Get Input Date
    input_date = input("What year would you like to travel to in YYYY-MM-DD format?\n")
    input_datetime = datetime.strptime(input_date, "%Y-%m-%d")
except ValueError as error:
    print("Please provide an input in YYYY-MM-DD format")
    exit(1)

billboard = Billboard(input_date)
spotipy_interface = SpotipyInterface(input_date, input_datetime)

spotipy_interface.add_track_uris(billboard.tracks)
spotipy_interface.create_playlist()
spotipy_interface.add_tracks()

