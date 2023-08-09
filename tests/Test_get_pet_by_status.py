from petservice.PetAPIService import PetAPIService
from enums.pet_status_enum import PetStatus


class TestGetByStatus:
    getPet = PetAPIService().get_pet_by_status(PetStatus.AVAILABLE.value)
    for pet in getPet:
        assert pet.status == PetStatus.AVAILABLE.value


