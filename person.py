class Person:
    def __init__(self, name, address):
        self.name = name
        self.adress = address

    def __str__(self):
        return f"{self.name} ({self.adress})"