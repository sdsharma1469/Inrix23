from geopy.geocoders import Nominatim
import time
from pprint import pprint

def OffGetCoordinates(Address):
    # instantiate a new Nominatim client
    app = Nominatim(user_agent="tutorial")
    address_local = Address
    # get location raw data
    location = app.geocode(f"{address_local}").raw
    
    # print raw data
    latitude = (location["lat"])
    longitude = (location["lon"])
    coordinates = f"/lots/v3?point={latitude}%7C{longitude}&radius=500"
    return coordinates

def OnGetCoordinates(Address):
    # instantiate a new Nominatim client
    app = Nominatim(user_agent="tutorial")
    address_local = Address
    # get location raw data
    location = app.geocode(f"{address_local}").raw
    
    # print raw data
    latitude = (location["lat"])
    longitude = (location["lon"])
    coordinates = f"/blocks/v3?point={latitude}%7C{longitude}&radius=500"
    return coordinates
