import requests
import xmltodict
import json

def get_data(tracking_id):
    url = f'https://api.bluedart.com/servlet/RoutingServlet?handler=tnt&action=custawbquery&loginid=BOM00001&awb=awb&numbers={tracking_id}&format=xml&lickey=4ecbd06dc0b9737d69120029cb05c9df&verno=1.6&scan=1'
    response = requests.get(url)
    json_resopnse = json.dumps(xmltodict.parse(response.text, attr_prefix=''))
    json_data = json.loads(json_resopnse)
    return json_data
