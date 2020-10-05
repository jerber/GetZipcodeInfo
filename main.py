from fastapi import FastAPI
import pprint
from uszipcode import SearchEngine


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
