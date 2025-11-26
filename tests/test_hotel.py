from src.classes.hotel import Hotel
from src.classes.room import Room, RoomStatus
from src.classes.guest import Guest

def test_create_reservation():
    hotel = Hotel("Test Hotel", "Address")
    room = Room(101, "deluxe")
    guest = Guest("Matheus", "Rua A")

    hotel.add_room(room)
    hotel.add_guest(guest)

    reservation = hotel.create_reservation(guest, room)

    assert room.status == RoomStatus.BOOKED
    assert reservation.status.value == "active"

def test_check_in():
    hotel = Hotel("Test Hotel", "Address")
    room = Room(101, "deluxe")
    guest = Guest("Matheus", "Rua A")

    hotel.add_room(room)
    hotel.add_guest(guest)

    reservation = hotel.create_reservation(guest, room)
    hotel.check_in(reservation)

    assert room.status == RoomStatus.OCCUPIED

def test_check_out():
    hotel = Hotel("Test Hotel", "Address")
    room = Room(101, "deluxe")
    guest = Guest("Matheus", "Rua A")

    hotel.add_room(room)
    hotel.add_guest(guest)

    reservation = hotel.create_reservation(guest, room)
    hotel.check_in(reservation)
    hotel.check_out(reservation)

    assert room.status == RoomStatus.CLEANING
