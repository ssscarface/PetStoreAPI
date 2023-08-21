from enum import Enum

class OrderStatus(Enum):
    PLACED = "placed"
    APPROVED = "approved"
    DELIVERED = "delivered"