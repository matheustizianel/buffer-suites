class Person:
    def __init__(self, name, email, phone_number = None, address = None):
        self.name = name
        self.email = email
        self.phone_number = phone_number
        self.address = address

    def __str__(self):
        return f"Name: {self.name} | Email: {self.email}"