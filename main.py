from fastapi import FastAPI
from fastapi.responses import JSONResponse
from api import gati, ekart, dtdc


app = FastAPI()


@app.get("/")
def main():
    return {"message": "API is UP!"}


@app.get("/active")
def active():
    return JSONResponse({"gati": True, "ekart": True, "dtdc": True})


@app.get("/gati")
@app.get("/gati/{dktno}")
def _gati(dktno: str):
    return JSONResponse(gati.get_data(dktno))


@app.get("/ekart/{trackingId}")
def _ekart(trackingId: str):
    return JSONResponse(ekart.get_data(trackingId))


@app.get("/dtdc/{trackingId}")
def _dtdc(trackingId: str):
    return JSONResponse(dtdc.get_data(trackingId))
