class Hotel:
    def __init__(self, name, address):
        self.name = name
        self.address = address
        self.rooms = []
        self.guests = []
        self.staff = []

    def add_room(self, room):
        self.rooms.append(room)
    
    def add_guest(self, guest):
        self.guests.append(guest)

    def add_staff(self, staff_member):
        self.staff.append(staff_member)