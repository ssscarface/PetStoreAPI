from petservice.PetAPIService import PetAPIService

params = {
    'status': 'available'
}


class TestGetByStatus:
    getPet = PetAPIService().get_pet_by_status(params).convert_response_to_list_of_pet_models()
    for pet in getPet:
        assert pet.status == 'available'


