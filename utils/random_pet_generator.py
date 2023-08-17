import string
import random
from apimodels.PetModel import *


class RandomPetGenerator:
    @staticmethod
    def generate_random_string(self):
        return ''.join(random.choice(string.ascii_letters) for _ in range(self))

    @staticmethod
    def generate_random_url():
        return f"https://www.petstore.cio/{RandomPetGenerator.generate_random_string(8)}"

    @staticmethod
    def generate_random_tag():
        return Tag(random.randint(1, 100), random.choice(["tag1", "tag2", "tag3", "tag4", "tag5"]))

    @staticmethod
    def generate_random_tags(self):
        return Tags(*[RandomPetGenerator.generate_random_tag() for _ in range(self)])

    @staticmethod
    def generate_random_category():
        return CategoryModel(random.randint(1, 50), RandomPetGenerator.generate_random_string(8))

    @staticmethod
    def generate_random_status():
        return random.choice(["available", "pending", "sold"])

    @classmethod
    def generate_random_pet_request(cls, category=True, name=True, photo_urls=True, tags=True, status=True):
        return PetModelRequest(
            random.randint(1, 1000),
            cls.generate_random_category() if category else None,
            cls.generate_random_string(8) if name else None,
            Urls(*[cls.generate_random_url() for _ in range(random.randint(1, 5))]) if photo_urls else None,
            cls.generate_random_tags(random.randint(1, 3)) if tags else None,
            cls.generate_random_status() if status else None
        )













