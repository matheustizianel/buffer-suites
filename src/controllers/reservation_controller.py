from datetime import datetime

from src.db.session import SessionLocal
from src.models.reservation_model import ReservationModel
from src.models.room_model import RoomModel
from src.enums.room_status import RoomStatus
from src.enums.reservation_status import ReservationStatus

class ReservationController:
    def create_reservation(self, guest_id, room_id):
        session = SessionLocal()
        try:
            room = session.get(RoomModel, room_id)

            if not room:
                raise ValueError("Room not found.")

            if room.status != RoomStatus.AVAILABLE:
                raise ValueError(f"Room {room.room_number} is not available.")

            reservation = ReservationModel(
                guest_id=guest_id,
                room_id=room_id,
                booking_time=datetime.now(),
                status=ReservationStatus.ACTIVE
            )

            room.status = RoomStatus.BOOKED

            session.add(reservation)
            session.commit()
            session.refresh(reservation)

            return reservation

        finally:
            session.close()

    def get_reservation_by_id(self, reservation_id):
        session = SessionLocal()
        try:
            return session.get(ReservationModel, reservation_id)
        finally:
            session.close()

    def list_reservations(self):
        session = SessionLocal()
        try:
            return session.query(ReservationModel).all()
        finally:
            session.close()

    def check_in(self, reservation_id):
        session = SessionLocal()
        try:
            reservation = session.get(ReservationModel, reservation_id)

            if not reservation:
                raise ValueError("Reservation not found.")

            if reservation.status != ReservationStatus.ACTIVE:
                raise ValueError("Reservation must be ACTIVE to check in.")

            reservation.status = ReservationStatus.CHECKED_IN
            reservation.checkin_time = datetime.now()

            room = session.get(RoomModel, reservation.room_id)
            room.status = RoomStatus.OCCUPIED

            session.commit()
            session.refresh(reservation)
            return reservation

        finally:
            session.close()

    def check_out(self, reservation_id):
        session = SessionLocal()
        try:
            reservation = session.get(ReservationModel, reservation_id)

            if not reservation:
                raise ValueError("Reservation not found.")

            if reservation.status != ReservationStatus.CHECKED_IN:
                raise ValueError("Reservation must be CHECKED_IN to check out.")

            reservation.status = ReservationStatus.COMPLETED
            reservation.checkout_time = datetime.now()

            room = session.get(RoomModel, reservation.room_id)
            room.status = RoomStatus.AVAILABLE

            session.commit()
            session.refresh(reservation)
            return reservation

        finally:
            session.close()

    def cancel(self, reservation_id):
        session = SessionLocal()
        try:
            reservation = session.get(ReservationModel, reservation_id)

            if not reservation:
                raise ValueError("Reservation not found.")

            if reservation.status != ReservationStatus.ACTIVE:
                raise ValueError("Only ACTIVE reservations can be cancelled.")

            reservation.status = ReservationStatus.CANCELLED
            reservation.cancellation_time = datetime.now()

            room = session.get(RoomModel, reservation.room_id)
            room.status = RoomStatus.AVAILABLE

            session.commit()
            session.refresh(reservation)
            return reservation

        finally:
            session.close()