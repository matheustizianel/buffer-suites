from src.reservation import Reservation

class Hotel:
    def __init__(self, name, address):
        self.name = name
        self.address = address
        self.rooms = []
        self.guests = []
        self.staff = []
        self.reservations = []

    def add_room(self, room):
        self.rooms.append(room)
    
    def add_guest(self, guest):
        self.guests.append(guest)

    def add_staff(self, staff_member):
        self.staff.append(staff_member)

    def create_reservation(self, guest, room):
        if room not in self.rooms:
            raise Exception("Room does not belong to this hotel.")
        
        if guest not in self.guests:
            raise Exception("Guest is not registered in this hotel.")
        
        # TO DO: VALIDADE DATES AVAILABLE AND DATE CONFLICTS

        reservation = Reservation(guest, room)
        reservation.reserve()
        self.reservations.append(reservation)

        return reservation