from bs4 import BeautifulSoup
import requests
from datetime import datetime
import polars as pl

url = "https://appbrewery.github.io/Zillow-Clone/"

# GET HTML
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

# GET items
items = soup.select(selector="#grid-search-results ul "
                             "li.ListItem-c11n-8-84-3-StyledListCardWrapper")

def extract_data(listing) -> (str, str, str):
    """Extract and format data from listing"""
    addr = listing.select_one(selector="address").text.strip().replace('|', '')
    price = listing.select_one(selector="[data-test='property-card-price']").text.strip()
    price = f"${''.join([char for char in price if char.isdigit()])}"
    link = listing.select_one(selector='a', href=True)['href']
    return addr, price, link


def create_columns(listings):
    """Create columns dict from listings data"""
    timestamp_column_data, address_column_data, price_column_data, link_column_data = [], [], [], []
    for listing in listings:
        timestamp = datetime.now().strftime("%d-%m-%Y %H:%M:%S")
        addr, price, link = extract_data(listing)
        timestamp_column_data = [*timestamp_column_data, timestamp]
        address_column_data = [*address_column_data, addr]
        price_column_data = [*price_column_data, price]
        link_column_data = [*link_column_data, link]
    return {
        "Timestamp": timestamp_column_data,
        "What's the address of the property?": address_column_data,
        "What's the price per month?": price_column_data,
        "What's the link to the property": link_column_data,
    }


# Extract price, link, address for each
# Create table
df = pl.DataFrame(create_columns(items))
df.write_excel("SF Renting Research.xlsx")