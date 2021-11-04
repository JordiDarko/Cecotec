import json
import requests

def get_random_value(min_value, max_value):
    url = 'https://random.api.randomkey.io/v1/double'
    headers = {'auth': '96aac0784de8fc3aed39c0daffc5f8ed',
               "Content-Type": "application/json"}
    data = json.dumps({'min': min_value, 'max': max_value})
    response = requests.post(url, headers=headers, data=data)
    return response.json()['number']
