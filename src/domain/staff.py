from enum import Enum
from src.domain.person import Person

class StaffShift(Enum):
    DAY = "day"
    NIGHT = "night"
    MORNING = "morning"
    AFTERNOON = "afternoon"
    EVENING = "evening"
    FULL_TIME = "full_time"

class Staff(Person):
    def __init__(self, name, email, phone_number = None, address = None):
        super().__init__(name, email, phone_number, address)

    def get_role(self):
        return self.__class__.__name__

    def __str__(self):
        return f"Name: {self.name} | Role: {self.get_role()}"

    def __repr__(self):
        return self.__str__()