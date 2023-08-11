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

    retrieved_pet=PetAPIService().get_pet_by_id(pet_id)
    assert retrieved_pet.id==pet_id
    assert retrieved_pet.name==verification_name

    petModelForUpdate = PetModelUpdateByID("Bob", "sold")
    pet__id = retrieved_pet.id
    response = PetAPIService().post_pet_by_id(petModelForUpdate, pet__id)
    updated_pet=PetAPIService().get_pet_by_id(pet__id)
    assert updated_pet.name==petModelForUpdate.name
    assert updated_pet.status==petModelForUpdate.status

    deleting_pet=PetAPIService().delete_pet(pet__id).json()
    deleted_pet_response = ResponseDeletedPet(deleting_pet['code'], deleting_pet['type'], deleting_pet['message'])
    assert deleted_pet_response.message == str(pet__id)
    double_check_deleted_pet=PetAPIService().get_pet_by_id(pet__id)
    assert double_check_deleted_pet is None