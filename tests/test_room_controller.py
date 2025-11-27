import pytest

from src.controllers.room_controller import RoomController
from src.models.room_model import RoomModel
from src.db.session import SessionLocal
from src.enums.room_status import RoomStatus


@pytest.fixture
def controller():
    return RoomController()


@pytest.fixture(autouse=True)
def clear_db():
    session = SessionLocal()
    session.query(RoomModel).delete()
    session.commit()
    session.close()
    yield

def test_create_room(controller):
    room = controller.create_room(room_number=101, room_type="Deluxe")

    assert room.id is not None
    assert room.room_number == 101
    assert room.room_type == "Deluxe"
    assert room.status == RoomStatus.AVAILABLE

def test_list_rooms(controller):
    controller.create_room(101, "Deluxe")
    controller.create_room(102, "Suite")

    rooms = controller.list_rooms()

    assert len(rooms) == 2
    numbers = [r.room_number for r in rooms]
    assert 101 in numbers
    assert 102 in numbers

def test_get_room_by_id(controller):
    created_room = controller.create_room(201, "Standard")

    room = controller.get_room_by_id(created_room.id)

    assert room is not None
    assert room.room_number == 201

def test_delete_room(controller):
    room = controller.create_room(301, "Penthouse")

    success = controller.delete_room(room.id)
    assert success is True

    deleted = controller.get_room_by_id(room.id)
    assert deleted is None

def test_delete_non_existent_room(controller):
    result = controller.delete_room(99999)

    assert result is False
