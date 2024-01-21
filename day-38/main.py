import os
from datetime import datetime

import requests
import polars as pl
from dotenv import load_dotenv

load_dotenv()

APP_ID = os.environ.get("APP_ID")
API_KEY = os.environ.get("API_KEY")
EXERCISE_ENDPOINT = "https://trackapi.nutritionix.com/v2/natural/exercise"

headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY,
    "x-remote-user-id": "0",  # 0 if in dev mode
}

# Get exercise data
exercise = input("Tell me which exercises you did: ")

data = {
    "query": exercise
}

response = requests.post(url=EXERCISE_ENDPOINT, headers=headers, json=data)
response.raise_for_status()
exercise_data = response.json()

# Format data
today = datetime.today()
date_formatted = today.strftime("%d/%m/%y")
time = today.strftime("%H:%M:%S")
formatted_dict = {
    "Date": date_formatted,
    "Time": time,
    "Exercise": exercise_data["exercises"][0]["name"],
    "Duration": exercise_data["exercises"][0]["duration_min"],
    "Calories": exercise_data["exercises"][0]["nf_calories"]
}

# Polars
df = pl.DataFrame(
    formatted_dict,
)

# Read file if it exists
try:
    json = pl.read_json("data.json")
# Except create new
except FileNotFoundError:
    print("Creating new data.json")
    df.write_json("data.json")
    print(df)
else:
    json_df = pl.DataFrame(json)
    result = pl.concat([json_df, df])
    result.write_json("data.json")
    print(result)



