from sqlalchemy.orm import Session
from ..db.session import SessionLocal
from ..models.guest_model import GuestModel


class GuestController:
    def create_guest(self, name, email = None, phone_number = None, address = None):
        session = SessionLocal()
        try:
            guest = GuestModel(
                name=name,
                email=email,
                phone_number=phone_number,
                address=address
            )
            session.add(guest)
            session.commit()
            session.refresh(guest)
            return guest
        finally:
            session.close()

    def get_guest_by_id(self, guest_id):
        session = SessionLocal()
        try:
            guest = session.get(GuestModel, guest_id)
            return guest
        finally:
            session.close()

    def list_guests(self):
        session = SessionLocal()
        try:
            guests = session.query(GuestModel).all()
            return guests
        finally:
            session.close()

    def update_guest(self, guest_id, name=None, email=None, phone_number=None, address=None):
        session = SessionLocal()
        try:
            guest = session.get(GuestModel, guest_id)
            if not guest:
                return None

            if name is not None:
                guest.name = name

            if email is not None:
                guest.email = email

            if phone_number is not None:
                guest.phone_number = phone_number
                
            if address is not None:
                guest.address = address

            session.commit()
            session.refresh(guest)
            return guest
        finally:
            session.close()


    def delete_guest(self, guest_id):
        session = SessionLocal()
        try:
            guest = session.get(GuestModel, guest_id)
            if not guest:
                return False
            session.delete(guest)
            session.commit()
            return True
        finally:
            session.close()
