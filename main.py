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
