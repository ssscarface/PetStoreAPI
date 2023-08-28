from enums.pet_status_enum import Prefix
from petservice.PetAPIService import PetAPIService
from apimodels.PetModel import *
from utils.random_pet_generator import RandomPetGenerator

class TestAccountCreation:
    pet_random_data = RandomPetGenerator.generate_random_pet_request()
    createPet = PetAPIService().createPet(pet_random_data)
    assert createPet.name == pet_random_data.name
    assert createPet.photoUrls[0] == pet_random_data.photoUrls[0]
    #assert createPet.tags[0]['id'] == pet_random_data.tags[0]['id']
    #assert createPet.tags[0]['name'] == pet_random_data.tags[0]['name']
    assert createPet.status == pet_random_data.status

    pet_id=createPet.id
    verification_name=createPet.name
    print(pet_id)

    retrieved_pet=PetAPIService().get_pet_by_id(pet_id)
    assert retrieved_pet.id==pet_id
    assert retrieved_pet.name==verification_name

    updated_name = RandomPetGenerator.generate_random_string(8, Prefix.Name.value)
    updated_status = RandomPetGenerator.generate_random_status()
    petModelForUpdate = PetModelUpdateByID(updated_name, updated_status)
    pet__id = retrieved_pet.id
    response = PetAPIService().post_pet_by_id(petModelForUpdate, pet__id)
    updated_pet=PetAPIService().get_pet_by_id(pet__id)
    assert updated_pet.name==petModelForUpdate.name
    assert updated_pet.status==petModelForUpdate.status

    deleting_pet=PetAPIService().delete_pet(pet__id).json()
    deleted_pet_response = ResponseDeletedPet(deleting_pet['code'], deleting_pet['type'], deleting_pet['message'])
    assert deleted_pet_response.message == str(pet__id)
    assert deleted_pet_response.code == 200
    double_check_deleted_pet=PetAPIService().get_pet_by_id(pet__id)
    assert double_check_deleted_pet == None