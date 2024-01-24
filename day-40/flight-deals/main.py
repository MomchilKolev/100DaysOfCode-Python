from datetime import datetime, timedelta

from data_manager import DataManager
from flight_search import FlightSearch
from notification_manager import NotificationManager

ORIGIN_CITY_IATA = "LON"

# This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.

data_manager = DataManager()
flight_search = FlightSearch()
notification_manager = NotificationManager()

# If there are cities without IATA Codes, fetch them
if any(data_manager.df.get_column("IATA Code").is_null().to_list()):
    rows = []
    for row in data_manager.df.iter_rows(named=True):
        if row["IATA Code"] is None:
            code = flight_search.get_destination_code(row["City"])
            row["IATA Code"] = code
        rows.append(row)
    data_manager.save(rows)

tomorrow = datetime.now() + timedelta(days=1)
six_month_from_today = datetime.now() + timedelta(days=(6 * 30))

# For every destination search flights
for destination in data_manager.df.iter_rows():
    flight = flight_search.check_flights(
        ORIGIN_CITY_IATA,
        destination[1],
        date_from=tomorrow,
        date_to=six_month_from_today
    )
    message = (f"Low price alert! Only {flight.price} Euro to fly from {flight.origin_city}-"
               f"{flight.origin_airport} to  {flight.destination_city}-"
               f"{flight.destination_airport}, from {datetime.fromtimestamp(flight.out_date)} to "
               f"{datetime.fromtimestamp(flight.return_date)}.")

    # If there is a lower price, send notification
    if flight and flight.price < destination[2]:
        if flight.stop_overs > 0:
            message += f"\nFlight has {flight.stop_overs} stop overs, via {flight.via_city} City."

    # notification_manager.send_notification(message=message.encode("utf-8"))
    notification_manager.send_emails(message=message.encode('utf-8'))
