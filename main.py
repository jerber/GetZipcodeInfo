from fastapi import FastAPI
import pprint
from uszipcode import SearchEngine

import usaddress

from timezonefinder import TimezoneFinder

tf = TimezoneFinder()

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/zipcode")
def get_zipcode(zipcode: str):
    search = SearchEngine(simple_zipcode=True)
    zipcode = search.by_zipcode(zipcode)
    pprint.pprint(zipcode.to_dict())
    return zipcode.to_dict()


import pprint


@app.get("/get_tz_from_coords")
def get_tz_from_coords(lat: float, lng: float):
    timezone = tf.timezone_at(lng=lng, lat=lat)
    print(f"{timezone=}")
    return timezone


@app.get("/parse_address")
def parse_address(address: str):
    parsed = usaddress.tag(address)
    if len(parsed) > 1:
        return parsed[0]
    return None


from pydantic import BaseModel


class Location(BaseModel):
    lat: float = None
    lng: float = None
    city: str = None
    state_abbr: str = None
    country_id: int = None
    country_name: str = None
    postal_code: str = None

    street_address: str = None
    unit: str = None

    # TODO this should not be None when this is pushed from the frontend
    timezone: str = None
    place_id: str = None


from geopy.geocoders import Nominatim

geolocator = Nominatim(user_agent="testing_geos")


@app.get("/location_from_city_and_state", response_model=Location)
def location_from_city_and_state(city: str, state_abbr: str):
    loc = geolocator.geocode(f"{city}, {state_abbr}")
    location = Location(
        lat=loc.latitude, lng=loc.longitude, city=city, state_abbr=state_abbr
    )
    return location
