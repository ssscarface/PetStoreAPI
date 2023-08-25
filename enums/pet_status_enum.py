from enum import Enum


class PetStatus(Enum):
    AVAILABLE = "available"
    PENDING = "pending"
    SOLD = "sold"


class Prefix(Enum):
    Name = "Name"
    CategoryName = "Cat_Name"
    URL = "URL"

