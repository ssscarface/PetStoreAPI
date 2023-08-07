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
    createPet = PetAPIService().createPet(pet_data).get_pet_from_post_response()
    assert createPet.name == 'doggie'
    assert createPet.photoUrls[0] == "url1"
    assert createPet.tags[0]['id'] == 1
    assert createPet.tags[0]['name'] == "FirstName"
    assert createPet.status == "available"




