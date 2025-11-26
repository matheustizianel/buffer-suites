from src.classes.person import Person

class Staff(Person):
    def __init__(self, name, email, phone_number = None, address = None):
        super().__init__(name, email, phone_number, address)

    def __str__(self):
        return f"Name: {self.name}"

    def __repr__(self):
        return self.__str__()