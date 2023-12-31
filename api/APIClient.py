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




headers_for_delete = {
    'accept': 'application/json'
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

    def get(self, endpoint, params=None):
        url = f"{self.base_url}/{endpoint}"
        print("URL: " + str(url))
        response = requests.get(url, params=params)
        return response

    def post_by_ID(self,endpoint,payload):
        url = f"{self.base_url}/{endpoint}"
        print("URL: " + str(url))
        response = requests.post(url, headers=headers_for_post_by_id,data=payload.__dict__)
        return response


    def delete_pet (self, endpoint):
        url = f"{self.base_url}/{endpoint}"
        print("URL: " + str(url))
        return requests.delete(url, headers=headers_for_delete)


    def put(self, endpoint, payload):
        url = f"{self.base_url}/{endpoint}"
        response = requests.put(url, headers=headers, data=json.dumps(payload.__dict__, default=lambda o: o.__dict__))
        return response


    def post_image(self, endpoint, file):
        url = f"{self.base_url}/{endpoint}/uploadImage"
        response = requests.post(url, files=file)
        return response

