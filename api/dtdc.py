import requests


def get_data(tracking_id):
    raw_data = {}
    url = f'http://track.dtdc.com/ctbs-tracking/customerInterface.tr?submitName=getLoadMovementDetails&cnNo={tracking_id}'
    resp = requests.get(url).json()
    if resp[0]['activityType'] == "Invalid Data":
        raw_data['status'] = False
        return raw_data
    else:
        raw_data["status"] = True
        raw_data['tracking_id'] = tracking_id
        raw_data['data'] = []
        for r in resp:
            data = {}
            data['activity'] = r['activityType']
            data['date'] = r['dateWithNoSuffix']
            data['time'] = r['time']
            data['status'] = r['deliveryStatus']
            data['origin'] = r['origin']
            data['destination'] = r['dest']
            raw_data['data'].append(data)
        return raw_data
    return None
