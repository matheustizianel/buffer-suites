from datetime import datetime
from src.person import Person

class Guest(Person):
    def __init__(self, name, email, phone_number = None, address = None, ):
        super().__init__(name, email, phone_number, address)

    def __str__(self):
        return super().__str__()