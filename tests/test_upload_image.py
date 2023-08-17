from petservice.PetAPIService import PetAPIService
from utils.read_file import ReadFile

pet_id = "9223372036854762299"
image = ReadFile.get_image("pet_image.png")


class TestUploadImage:
    upload_image_response = PetAPIService().upload_image(pet_id, image)
    assert upload_image_response.code == 200
