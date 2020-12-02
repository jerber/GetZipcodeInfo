from fastapi import FastAPI
import pprint
from uszipcode import SearchEngine

import usaddress


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


@app.get("/parse_address")
def parse_address(address: str):
    parsed = usaddress.tag(address)
    if len(parsed) > 1:
        return parsed[0]
    return None
