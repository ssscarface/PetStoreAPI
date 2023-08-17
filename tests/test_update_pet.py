from petservice.PetAPIService import PetAPIService
from enums.pet_status_enum import PetStatus
from utils.random_pet_generator import RandomPetGenerator

pet_data = RandomPetGenerator().generate_random_pet_request(category=False)


class TestUpdatePet:
    updated_pet = PetAPIService().update_pet(pet_data)
    assert updated_pet.name == pet_data.name
    assert updated_pet.status == PetStatus.AVAILABLE.value
