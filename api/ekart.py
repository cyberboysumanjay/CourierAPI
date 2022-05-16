import requests
from requests.structures import CaseInsensitiveDict


def get_data(tracking_id):
    url = "https://ekartlogistics.com/ws/getTrackingDetails"
    headers = CaseInsensitiveDict()
    headers["Accept"] = "application/json, text/plain, */*"
    headers["Accept-Language"] = "en-US,en;q=0.9"
    headers["Connection"] = "keep-alive"
    headers["Content-Type"] = "application/json"
    headers["Cookie"] = "empid=; ab=testprodcluster; epoctime=1652180704.216"
    headers["Origin"] = "https://ekartlogistics.com"
    headers["Referer"] = f"https://ekartlogistics.com/shipmenttrack/{tracking_id}"
    headers["Sec-Fetch-Dest"] = "empty"
    headers["Sec-Fetch-Mode"] = "cors"
    headers["Sec-Fetch-Site"] = "same-origin"
    headers["Sec-GPC"] = "1"
    headers["User-Agent"] = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.54 Safari/537.36"
    data = '{"trackingId":"'+ tracking_id+'"}'
    resp = requests.post(url, headers=headers, data=data).json()
    return resp

