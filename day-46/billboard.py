import requests
from bs4 import BeautifulSoup


class Billboard:
    def __init__(self, input_date):
        self.url = f"https://www.billboard.com/charts/hot-100/{input_date}/"
        self.tracks = []

        # Get top 100 tracks
        response = requests.get(self.url)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, 'html.parser')

        # Format into list
        tracks = soup.select(selector=".chart-results-list .o-chart-results-list-row")
        for i, track in enumerate(tracks):
            title = track.select_one(
                selector="li:nth-child(4) #title-of-a-story").get_text().strip()
            artist = track.select_one(selector="li:nth-child(4) span").get_text().strip()
            self.tracks.append({"place": i + 1, "title": title, "artist": artist})