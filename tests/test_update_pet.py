from petservice.PetAPIService import PetAPIService
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
