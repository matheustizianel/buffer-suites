from src.person import Person

class Staff(Person):
    def __init__(self, name, role, address):
        super().__init__(name, address)
        self.role = role.lower()

    def __str__(self):
        return f"{self.name} - {self.role.title()} ({self.adress})"