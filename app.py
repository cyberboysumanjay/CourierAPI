from fastapi import FastAPI
from api import gati, ekart


app = FastAPI()


@app.get("/")
def main():
    return {"message": "API is UP!"}


@app.get("/gati/{dktno}")
def _gati(dktno: str):
    return gati.get_data(dktno)


@app.get("/ekart/{trackingId}")
def _ekart(trackingId: str):
    return ekart.get_data(trackingId)
