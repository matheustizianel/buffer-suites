from src.classes.hotel import Hotel
from src.classes.room import Room, RoomStatus
from src.classes.guest import Guest
from src.classes.cleaner import Cleaner
from src.classes.staff import StaffShift

# ----------------------------------------------------------
# Test 1 — Cleaner receives a task
# ----------------------------------------------------------
def test_cleaner_task_assignment():
    cleaner = Cleaner("Mario", "mario@email.com")
    room = Room(101, "deluxe")

    cleaner.add_cleaning_task(room)

    assert room in cleaner.pending_cleaning_tasks

# ----------------------------------------------------------
# Test 2 — Cleaner cleans a room he was assigned
# ----------------------------------------------------------
def test_cleaner_executes_cleaning():
    cleaner = Cleaner("Mario", "mario@email.com")
    room = Room(101, "deluxe")

    cleaner.add_cleaning_task(room)
    cleaner.clean_room(room)

    assert room in cleaner.cleaning_history
    assert room not in cleaner.pending_cleaning_tasks

# ----------------------------------------------------------
# Test 3 — Cleaning integrated with Hotel
# ----------------------------------------------------------
def test_cleaning_flow_with_hotel():
    # hotel setup
    hotel = Hotel("Buffer Suites", "Jacksonville")
    room = Room(101, "deluxe")
    guest = Guest("Matheus", "Rua A")
    cleaner = Cleaner("Mario", "mario@email.com")

    # register
    hotel.add_room(room)
    hotel.add_guest(guest)
    hotel.add_staff(cleaner)

    # reservation + checkin + checkout
    res = hotel.create_reservation(guest, room)
    hotel.check_in(res)
    hotel.check_out(res)

    # room should now be CLEANING
    assert room.status == RoomStatus.CLEANING

    # assign cleaning
    hotel.assign_cleaning_task(room, cleaner)
    assert room in cleaner.pending_cleaning_tasks

    # cleaner performs cleaning
    hotel.clean_room(room, cleaner)

    # room should now be AVAILABLE
    assert room.status == RoomStatus.AVAILABLE
    assert room in cleaner.cleaning_history
