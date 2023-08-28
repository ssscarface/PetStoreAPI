from api.APIResponse import ApiResponse
from api.APIClient import APIClient


pestStoreUrl = "https://petstore.swagger.io/v2"


class PetAPIService:

    def __init__(self):
        pass

    def createPet(self, payload):
        response = APIClient(pestStoreUrl).post("pet", payload)
        return ApiResponse(response).convert_response_to_pet_model()


    def get_pet_by_status(self, pet_status):
        params = {
            'status': pet_status
        }
        response = APIClient(pestStoreUrl).get("pet/findByStatus", params)
        return ApiResponse(response).convert_response_to_list_of_pet_models()

    def get_pet_by_id(self, pet_id):
        response = APIClient(pestStoreUrl).get(f"pet/{pet_id}")
        return ApiResponse(response).convert_response_to_pet_model()

    def post_pet_by_id(self,payload, pet_id):
        response = APIClient(pestStoreUrl).post_by_ID(f"pet/{pet_id}", payload)
        return response


    def delete_pet(self,pet_id):
        response = APIClient(pestStoreUrl).delete_pet(f"pet/{pet_id}")
        return response


    def update_pet(self, payload):
        response = APIClient(pestStoreUrl).put("pet", payload)
        return ApiResponse(response).convert_response_to_pet_model()


    def upload_image(self, pet_id, file):
        response = APIClient(pestStoreUrl).post_image(f"pet/{pet_id}", file)
        return ApiResponse(response).convert_response_to_upload_image_model()
