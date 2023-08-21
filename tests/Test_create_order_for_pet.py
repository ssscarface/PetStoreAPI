from petservice.PetAPIService import PetAPIService
from apimodels.PetModel import *
from petservice.OrderAPIService import OrderPetApi
from apimodels.OrderModel import OrderModel
from enums.Order_status_enum import OrderStatus

class CreateOrderForPet:
    pet_data = PetModelRequest(
        999997,
        CategoryModel(0, "string"),
        "doggie",
        Urls("url1"),
        Tags(Tag(1, "FirstName")),
        "available"
    )
    createPet = PetAPIService().createPet(pet_data)
    assert createPet.name == 'doggie'
    assert createPet.photoUrls[0] == "url1"
    assert createPet.tags[0]['id'] == 1
    assert createPet.tags[0]['name'] == "FirstName"
    assert createPet.status == "available"

    order_data = OrderModel(
        0,
        createPet.id,
        1,
        "2023-08-13T11:24:17.312Z",
        "placed",
        True
    )
    create_order = OrderPetApi().createOrder(order_data)
    assert create_order.petId == createPet.id
    assert create_order.status == OrderStatus.PLACED.value
