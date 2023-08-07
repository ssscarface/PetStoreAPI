import requests
import json
from apimodels.PetModel import *

headers = {
    'accept': 'application/json',
    'Content-Type': 'application/json',
}
class APIClient:

    def __init__(self, url):
        self.base_url = url

    def post(self, endpoint, payload):
        url = f"{self.base_url}/{endpoint}"
        print("URL: " + str(url))
        response = requests.post(url, headers=headers,
                             data=json.dumps(payload.__dict__, default=lambda o: o.__dict__))
        return response


