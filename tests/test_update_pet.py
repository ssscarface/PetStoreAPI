from petservice.PetAPIService import PetAPIService
from enums.pet_status_enum import PetStatus, Prefix
from utils.random_pet_generator import RandomPetGenerator
from apimodels.PetModel import *

pet_data = RandomPetGenerator().generate_random_pet_request(category=False)

pet_payload = PetModelRequest(
    45,
    CategoryModel(1, "name"),
    RandomPetGenerator.generate_random_string(8, Prefix.Name.value),
    Urls("http://test.test", "http://test2.test"),
    RandomPetGenerator.generate_random_tags(3),
    "available"
)


class TestUpdatePet:
    updated_pet = PetAPIService().update_pet(pet_payload)
    assert updated_pet.name == pet_payload.name
    assert updated_pet.status == PetStatus.AVAILABLE.value
