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
