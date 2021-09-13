import requests


def get_data(dktno):
    """
    Get the data from the GATI API
    """
    import requests
    from requests.structures import CaseInsensitiveDict

    url = "https://www.gati.com/gwebforms/GatijsonDktTrack3.jsp"

    headers = CaseInsensitiveDict()
    headers["Content-Type"] = "application/x-www-form-urlencoded"

    data = f"dktno={dktno}"
    resp = requests.post(url, headers=headers, data=data)
    print("Gati Request Returned:", resp.status_code)
    return resp.json()


# print(get_gati_data(409143138))
