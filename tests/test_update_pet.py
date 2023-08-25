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

from apimodels.PetModel import *
from enums.pet_status_enum import PetStatus


class TestUpdatePet:
    pet_data = PetModelRequest(
        3,
        CategoryModel(0, "string"),
        "doggie",
        Urls("url1"),
        Tags(Tag(1, "FirstName")),
        "available"
    )
    updated_pet = PetAPIService().update_pet(pet_data)
    assert updated_pet.name == "doggie"

    assert updated_pet.status == PetStatus.AVAILABLE.value
