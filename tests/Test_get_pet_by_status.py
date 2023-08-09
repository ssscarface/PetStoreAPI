from petservice.PetAPIService import PetAPIService
from enums.status_enum import Status

params = {
    'status': Status.AVAILABLE.value
}


class TestGetByStatus:
    getPet = PetAPIService().get_pet_by_status(params).convert_response_to_list_of_pet_models()
    for pet in getPet:
        assert pet.status == Status.AVAILABLE.value


