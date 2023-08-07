from petservice.PetAPIService import PetAPIService
from apimodels.PetModel import *


class TestAccountCreation:
    pet_data = PetModelRequest(
        0,
        CategoryModel(0, "string"),
        "doggie",
        Urls("url1"),
        Tags(Tag(1, "FirstName")),
        "available"
    )
    createPet = PetAPIService().createPet(pet_data).convert_response_to_pet_model()
    assert createPet.name == 'doggie'
    assert createPet.photoUrls[0] == "url1"
    assert createPet.tags[0]['id'] == 1
    assert createPet.tags[0]['name'] == "FirstName"
    assert createPet.status == "available"

    pet_id=createPet.id
    verification_name=createPet.name
    print(pet_id)

    retrieved_pet=PetAPIService().get_pet_by_id(pet_id).convert_response_to_pet_model()
    assert retrieved_pet.id==pet_id
    assert retrieved_pet.name==verification_name