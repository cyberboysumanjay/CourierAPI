import requests
from requests.structures import CaseInsensitiveDict


def get_data(tracking_id):
    url = "https://www.ekartlogistics.com/ws/getTrackingDetails"

    headers = CaseInsensitiveDict()
    headers["Connection"] = "keep-alive"
    headers["Accept"] = "application/json, text/plain, */*"
    headers["User-Agent"] = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.63 Safari/537.36"
    headers["Content-Type"] = "application/json"
    headers["Sec-GPC"] = "1"
    headers["Origin"] = "https://www.ekartlogistics.com"
    headers["Sec-Fetch-Site"] = "same-origin"
    headers["Sec-Fetch-Mode"] = "cors"
    headers["Sec-Fetch-Dest"] = "empty"
    headers["Referer"] = f"https://www.ekartlogistics.com/shipmenttrack/{tracking_id}"
    headers["Accept-Language"] = "en-GB,en-US;q=0.9,en;q=0.8"
    data = '{"trackingId":"' + str(tracking_id) + '"}'
    resp = requests.post(url, headers=headers, data=data)
    print("Gati Request Returned:", resp.status_code)
    return resp.json()


# print(get_data("FMPP0845214270"))
