from src.db.session import SessionLocal
from src.models.staff_model import StaffModel


class StaffController:
    def create_staff(self, name, role, email=None, phone_number=None, address=None):
        session = SessionLocal()
        try:
            staff = StaffModel(
                name=name,
                role=role,
                email=email,
                phone_number=phone_number,
                address=address
            )
            session.add(staff)
            session.commit()
            session.refresh(staff)
            return staff
        finally:
            session.close()

    def get_staff_by_id(self, staff_id):
        session = SessionLocal()
        try:
            return session.get(StaffModel, staff_id)
        finally:
            session.close()

    def list_staff(self):
        session = SessionLocal()
        try:
            return session.query(StaffModel).all()
        finally:
            session.close()

    def update_staff(self, staff_id, **kwargs):
        session = SessionLocal()
        try:
            staff = session.get(StaffModel, staff_id)
            if not staff:
                return None

            for key, value in kwargs.items():
                if hasattr(staff, key):
                    setattr(staff, key, value)

            session.commit()
            session.refresh(staff)
            return staff
        finally:
            session.close()

    def delete_staff(self, staff_id):
        session = SessionLocal()
        try:
            staff = session.get(StaffModel, staff_id)
            if not staff:
                return False

            session.delete(staff)
            session.commit()
            return True
        finally:
            session.close()
