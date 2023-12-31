class Urls:
    def __init__(self, *urls):
        self.urls = urls


class Tag:
    def __init__(self, id, name):
        self.id = id
        self.name = name


class Tags:
    def __init__(self, *tags):
        self.tags = tags


class CategoryModel:
    def __init__(self, id, name):
        self.id = id
        self.name = name


class PetModelRequest:
    def __init__(self, id, category=None, name=None, photoUrls=None, tags=None, status=None):
        self.id = id
        self.category = category
        self.name = name
        self.photoUrls = photoUrls.urls if isinstance(photoUrls, Urls) else photoUrls
        self.tags = tags.tags if isinstance(tags, Tags) else tags
        self.status = status


class PetModelUpdateByID:
    def __init__(self, name, status):
        self.name= name
        self.status=status



class UploadImageResponse:
    def __init__(self, code, type, message):
        self.code = code
        self.type = type
        self.message = message

class ResponseDeletedPet:
    def __init__(self, code,type,message):
        self.code=code
        self.type=type
        self.message=message


