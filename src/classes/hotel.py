from src.classes.reservation import Reservation
from src.classes.room import RoomStatus

class Hotel:
    def __init__(self, name, address):
        self.name = name
        self.address = address

        self.rooms = []
        self.guests = []
        self.staff = []
        # self.reservations = []

    def add_room(self, room):
        self.rooms.append(room)
    
    def add_guest(self, guest):
        self.guests.append(guest)

    def add_staff(self, staff_member):
        self.staff.append(staff_member)

    # def create_reservation(self, guest, room):
    #     if room not in self.rooms:
    #         raise Exception("Room does not belong to this hotel.")
        
    #     if guest not in self.guests:
    #         raise Exception("Guest is not registered in this hotel.")

    #     reservation = Reservation(guest, room)
    #     reservation.reserve()
    #     self.reservations.append(reservation)

    #     return reservation
    #     # TO DO: VALIDATE DATES AVAILABLE AND DATE CONFLICTS

    # def cancel_reservation(self, reservation):
    #     if reservation not in self.reservations:
    #         raise Exception("Reservation not found in this hotel.")

    #     reservation.cancel()

    # def list_reservations(self):
    #     if not self.reservations:
    #         #raise Exception("No reservations found in this hotel.")
    #         print("No reservations found for this hotel.")
    #         return

    #     for reservation in self.reservations:
    #         print(f"Guest: {reservation.guest.name}, Room: {reservation.room.room_number}, Status: {reservation.status.value}`")
    #         # print(reservation)

    # def show_reservation(self, reservation):
    #     if reservation not in self.reservations:
    #         raise Exception("Reservation not found.")

    #     print(f"Reservation for {reservation.guest.name}")
    #     print(f"Room: {reservation.room.room_number}")
    #     print(f"Status: {reservation.status.value}")
    #     print(f"Booking time: {reservation.booking_time}")
    #     print(f"Check-in: {reservation.checkin_time}")
    #     print(f"Checkout: {reservation.checkout_time}")
    #     print(f"Cancellation: {reservation.cancellation_time}")

    # def check_in(self, reservation):
    #     if reservation not in self.reservations:
    #         raise Exception("Reservation not found.")

    #     reservation.check_in()

    # def check_out(self, reservation):
    #     if reservation not in self.reservations:
    #         raise Exception("Reservation not found.")

    #     reservation.check_out()

    def get_available_rooms(self):
        return [
            room for room in self.rooms
            if room.status == RoomStatus.AVAILABLE
        ]
    
    def get_available_rooms_by_type(self, room_type):
        return [
            room for room in self.rooms
            if room.room_type == room_type
            and room.status == RoomStatus.AVAILABLE
        ]

    def find_guest_by_name(self, name):
        return [
            g for g in self.guests 
            if g.name.lower() == name.lower()
        ]
    
    def find_staff_by_type(self, staff_type):
        return [
            s for s in self.staff
            if isinstance(s, staff_type)
        ]
    
    def __str__(self):
        return (
            f"Hotel: {self.name}\n"
            f"Address: {self.address}\n"
            f"Rooms: {len(self.rooms)}\n"
            f"Guests: {len(self.guests)}\n"
            f"Staff: {len(self.staff)}"
        )

    # def list_guests(self):
    #     if not self.guests:
    #         print("No guests found registered.")
    #         return

    #     for g in self.guests:
    #         print(f"Guest: {g.name} | Email: {g.email}")

    # def find_reservations_by_guest(self, guest):
    #     return [res for res in self.reservations if res.guest == guest]

    # def assign_cleaning_task(self, room, cleaner):
    #     if room not in self.rooms:
    #         raise Exception("Room does not belong to this hotel.")

    #     cleaner.add_cleaning_task(room)

    # def clean_room(self, room, cleaner):
    #     if room not in self.rooms:
    #         raise Exception("Room does not belong to this hotel.")

    #     cleaner.clean_room(room)
    #     room.mark_cleaned(cleaner)

