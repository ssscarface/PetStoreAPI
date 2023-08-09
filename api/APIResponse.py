import json

from apimodels.PetModel import *


class ApiResponse:
    def __init__(self, response):
        self.response_data = response.json()


    def convert_response_to_pet_model(self):
        pet_data = self.response_data
        if 'id' in pet_data:
            return PetModelRequest(**pet_data)
        return None

    def convert_response_to_list_of_pet_models(self):
        response = self.response_data
        list_of_pet_models = []
        if isinstance(response, list):
            for pet_data in response:
                if 'id' in pet_data:
                    list_of_pet_models.append(PetModelRequest(**pet_data))
        return list_of_pet_models

