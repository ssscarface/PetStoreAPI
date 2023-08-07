from apimodels.PetModel import PetModelRequest
class ApiResponse:
    def __init__(self, response):
        self.response_data = response.json()

    def get_pet_from_post_response(self):
        pet_data = self.response_data
        if 'id' in pet_data:
            return PetModelRequest(**pet_data)
        return None
