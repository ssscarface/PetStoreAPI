
class ReadFile:
    @staticmethod
    def get_image(_path):
        file = {"file": open(_path, "rb")}
        return file
