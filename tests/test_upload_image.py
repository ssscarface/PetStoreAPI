from petservice.PetAPIService import PetAPIService
from utils.file_reader import FileReader

pet_id = "9223372036854762299"
image = FileReader.get_image("pet_image.png")


class TestUploadImage:
    upload_image_response = PetAPIService().upload_image(pet_id, image)
    assert upload_image_response.code == 200
