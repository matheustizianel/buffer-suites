from src.person import Person

class Staff(Person):
    def __init__(self, name, role, email, phone_number = None, address = None):
        super().__init__(name, email, phone_number, address)
        self.role = role.lower()

    def __str__(self):
        parent_str = super().__str__()
        return f"{parent_str} | Role: {self.role.title()}"