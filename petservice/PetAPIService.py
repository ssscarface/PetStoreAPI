from api.APIResponse import ApiResponse
from api.APIClient import APIClient

pestStoreUrl = "https://petstore.swagger.io/v2"


class PetAPIService:

    def __init__(self):
        pass

    def createPet(self, payload):
        response = APIClient(pestStoreUrl).post("pet", payload)
        return ApiResponse(response)

    def get_pet_by_id(self, pet_id):
        response = APIClient(pestStoreUrl).get(f"pet/{pet_id}")
        return ApiResponse(response).convert_response_to_pet_model()

    def post_pet_by_id(self,payload, pet_id):
        response = APIClient(pestStoreUrl).post_by_ID(f"pet/{pet_id}", payload)
        return response
    def delete_pet(self,pet_id):
        response = APIClient(pestStoreUrl).delete_pet(f"pet/{pet_id}")
        return response