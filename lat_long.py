from geopy.geocoders import Nominatim
import time
from pprint import pprint

def getCoordinates(Address):
    # instantiate a new Nominatim client
    app = Nominatim(user_agent="tutorial")
    address_local = Address
    # get location raw data
    location = app.geocode(f"{address_local}").raw
    # print raw data
    latitude = (location["lat"])
    longitude = (location["lon"])
    print(f"latitude = {latitude}, longitude = {longitude}")
    coordinates = f"/lots/v3?point={latitude}%257C{longitude}&radius=500"
    print(coordinates)
    return coordinates
