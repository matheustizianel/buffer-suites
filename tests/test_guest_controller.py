import pytest

from src.controllers.guest_controller import GuestController
from src.models.guest_model import GuestModel
from src.db.session import SessionLocal

@pytest.fixture
def controller():
    return GuestController()

@pytest.fixture(autouse=True)
def clear_db():
    session = SessionLocal()
    session.query(GuestModel).delete()
    session.commit()
    session.close()
    yield

def test_create_guest(controller):
    guest = controller.create_guest(
        name = "Matheus", 
        email = "matheus@test.com", 
        phone_number = "9048028750",
        address = "12345 Micro Lane Jacksonville FL 33333")
    
    assert guest.id is not None
    assert guest.name == "Matheus"
    assert guest.email == "matheus@test.com"

def test_list_guests(controller):
    controller.create_guest("Alice")
    controller.create_guest("Bob")

    guests = controller.list_guests()

    assert len(guests) == 2
    names = [g.name for g in guests]
    assert "Alice" in names
    assert "Bob" in names

def test_get_guest_by_id(controller):
    new_guest = controller.create_guest("Charlie")

    guest = controller.get_guest_by_id(new_guest.id)

    assert guest is not None
    assert guest.name == "Charlie"

def test_delete_guest(controller):
    guest = controller.create_guest("Delete Me")

    success = controller.delete_guest(guest.id)

    assert success is True

    deleted = controller.get_guest_by_id(guest.id)
    assert deleted is None

def test_delete_non_existent_guest(controller):
    result = controller.delete_guest(99999)

    assert result is False
