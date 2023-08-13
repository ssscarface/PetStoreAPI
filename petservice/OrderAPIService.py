from api.APIStore import APIOrder
from api.APIResponse import ApiResponse

pestStoreUrl = "https://petstore.swagger.io/v2"

class OrderPetApi:
    def __init__(self):
        pass

    def createOrder(self, payload):
        response = APIOrder(pestStoreUrl).post("store/order", payload)
        return ApiResponse(response).convert_response_to_order_model()