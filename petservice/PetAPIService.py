from api.APIResponse import ApiResponse
from api.APIClient import APIClient

pestStoreUrl = "https://petstore.swagger.io/v2"


class PetAPIService:

    def __init__(self):
        pass

    def createPet(self, payload):
        print("Payload: " + str(payload.__dict__))
        response = APIClient(pestStoreUrl).post("pet", payload)
        return ApiResponse(response)

    def get_pet_by_status(self, pet_status):
        response = APIClient(pestStoreUrl).get("pet/findByStatus", pet_status)
        return ApiResponse(response)
