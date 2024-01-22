from dotenv import load_dotenv
import os
import requests
from datetime import datetime, timedelta
from flight_data import FlightData

load_dotenv()

class FlightSearch():
    #This class is responsible for talking to the Flight Search API.
    def __init__(self):
        super().__init__()
        self.api_key = os.environ.get("KIWI_API_KEY")
        self.api_endpoint = os.environ.get("KIWI_API_ENDPOINT")
        self.headers = {
            "apikey": self.api_key
        }
        self.departure_iata = "LON"
        self.tomorrow = (datetime.today() + timedelta(1)).strftime("%d/%m/%Y")
        self.future_date = (datetime.today() + timedelta(weeks=26)).strftime("%d/%m/%Y")

    def get_destination_code(self, city_name):
        locations_endpoint = f"{self.api_endpoint}/locations/query"
        params = {
            "term": city_name
        }
        response = requests.get(url=locations_endpoint, headers=self.headers, params=params)
        response.raise_for_status()
        json = response.json()["locations"]
        code = json[0]["code"]
        return code

    def check_flights(self, origin_city_code, destination_city_code, date_from, date_to):
        query = {
            "fly_from": origin_city_code,
            "fly_to": destination_city_code,
            "date_from": date_from.strftime("%d/%m/%Y"),
            "date_to": date_to.strftime("%d/%m/%Y"),
            "nights_in_dst_from": 7,
            "nights_in_dst_to": 28,
            "one_for_city": 1,
            "max_stopovers": 0,
            "curr": "EUR"
        }

        response = requests.get(
            url=f"{self.api_endpoint}/search",
            headers=self.headers,
            params=query
        )

        try:
            data = response.json()["data"][0]
        except IndexError:
            print(f"No flights found for {destination_city_code}.")
            return None


        flight_data = FlightData(
            price=data["price"],
            origin_city=data["route"][0]["cityFrom"],
            origin_airport=data["route"][0]["flyFrom"],
            destination_city=data["route"][0]["cityTo"],
            destination_airport=data["route"][0]["flyTo"],
            out_date=data["route"][0]["dTime"],
            return_date=data["route"][1]["dTime"]
        )
        print(f"{flight_data.destination_city}: €{flight_data.price} from "
              f"{datetime.fromtimestamp(flight_data.out_date).strftime('%d-%m-%Y')} to "
              f"{datetime.fromtimestamp(flight_data.return_date).strftime('%d-%m-%Y')}")
        return flight_data
