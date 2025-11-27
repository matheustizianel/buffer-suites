import pytest
from datetime import datetime

from src.controllers.guest_controller import GuestController
from src.controllers.room_controller import RoomController
from src.controllers.reservation_controller import ReservationController

from src.enums.reservation_status import ReservationStatus
from src.models.reservation_model import ReservationModel
from src.models.room_model import RoomModel
from src.models.guest_model import GuestModel
from src.db.session import SessionLocal


@pytest.fixture
def guest_controller():
    return GuestController()


@pytest.fixture
def room_controller():
    return RoomController()


@pytest.fixture
def reservation_controller():
    return ReservationController()


@pytest.fixture(autouse=True)
def clear_db():
    session = SessionLocal()
    session.query(ReservationModel).delete()
    session.query(RoomModel).delete()
    session.query(GuestModel).delete()
    session.commit()

    yield

    session.query(ReservationModel).delete()
    session.query(RoomModel).delete()
    session.query(GuestModel).delete()
    session.commit()
    session.close()


def test_create_reservation(guest_controller, room_controller, reservation_controller):
    guest = guest_controller.create_guest("Matheus")
    room = room_controller.create_room(101, "Deluxe")

    reservation = reservation_controller.create_reservation(
        guest.id, room.id, status=ReservationStatus.ACTIVE
    )

    assert reservation.id is not None
    assert reservation.status == ReservationStatus.ACTIVE
    assert reservation.guest_id == guest.id
    assert reservation.room_id == room.id


def test_get_reservation_by_id(guest_controller, room_controller, reservation_controller):
    guest = guest_controller.create_guest("Lucas")
    room = room_controller.create_room(102, "Suite")

    reservation = reservation_controller.create_reservation(
        guest.id, room.id, status=ReservationStatus.ACTIVE
    )

    found = reservation_controller.get_reservation_by_id(reservation.id)
    assert found is not None
    assert found.id == reservation.id


def test_list_reservations(guest_controller, room_controller, reservation_controller):
    guest = guest_controller.create_guest("Anna")
    room = room_controller.create_room(103, "Economy")

    reservation_controller.create_reservation(guest.id, room.id, ReservationStatus.ACTIVE)
    reservation_controller.create_reservation(guest.id, room.id, ReservationStatus.CHECKED_IN)

    reservations = reservation_controller.list_reservations()
    assert len(reservations) == 2


def test_update_reservation(guest_controller, room_controller, reservation_controller):
    guest = guest_controller.create_guest("Mike")
    room = room_controller.create_room(104, "Standard")

    reservation = reservation_controller.create_reservation(
        guest.id, room.id, status=ReservationStatus.ACTIVE
    )

    updated = reservation_controller.update_reservation(
        reservation.id,
        status=ReservationStatus.CANCELLED
    )

    assert updated.status == ReservationStatus.CANCELLED


def test_delete_reservation(guest_controller, room_controller, reservation_controller):
    guest = guest_controller.create_guest("Carla")
    room = room_controller.create_room(105, "Deluxe")

    reservation = reservation_controller.create_reservation(
        guest.id, room.id, status=ReservationStatus.ACTIVE
    )

    success = reservation_controller.delete_reservation(reservation.id)
    assert success is True

    not_found = reservation_controller.get_reservation_by_id(reservation.id)
    assert not_found is None
