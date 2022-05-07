import requests
import json


def get_data(tracking):
    form = {
        "handler": 'tnt',
        "action": 'awbquery',
        "awb": 'awb',
        "numbers": tracking
    }
    headers = {
        'Content-Length': str(len(form)),
        'Content-Type': 'application/x-www-form-urlencoded'
    }
    r = requests.post(
        'https://www.bluedart.com/servlet/RoutingServlet', data=form, headers=headers)
    print(r.status_code)


# get_data('89259720480')
