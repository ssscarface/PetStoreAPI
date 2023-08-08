import requests
import json

headers = {
    'accept': 'application/json',
    'Content-Type': 'application/json',
}

headers_for_post_by_id={
            'accept': 'application/json',
            'Content-Type': 'application/x-www-form-urlencoded'
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

    def get(self, endpoint):
        url = f"{self.base_url}/{endpoint}"
        print("URL: " + str(url))
        return requests.get(url, headers=headers)

    def post_by_ID(self,endpoint,payload):
        url = f"{self.base_url}/{endpoint}"
        print("URL: " + str(url))
        response = requests.post(url, headers=headers_for_post_by_id,data=payload.__dict__)
        return response