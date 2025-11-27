from datetime import datetime
from src.db.session import SessionLocal
from src.models.reservation_model import ReservationModel


class ReservationController:

    def create_reservation(self, guest_id, room_id, status, booking_time=None):
        session = SessionLocal()
        try:
            reservation = ReservationModel(
                guest_id=guest_id,
                room_id=room_id,
                booking_time=booking_time or datetime.now(),
                status=status
            )
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

    def update_reservation(self, reservation_id, **kwargs):
        session = SessionLocal()
        try:
            reservation = session.get(ReservationModel, reservation_id)
            if not reservation:
                return None

            for key, value in kwargs.items():
                if hasattr(reservation, key):
                    setattr(reservation, key, value)

            session.commit()
            session.refresh(reservation)
            return reservation
        finally:
            session.close()

    def delete_reservation(self, reservation_id):
        session = SessionLocal()
        try:
            reservation = session.get(ReservationModel, reservation_id)
            if not reservation:
                return False

            session.delete(reservation)
            session.commit()
            return True
        finally:
            session.close()
