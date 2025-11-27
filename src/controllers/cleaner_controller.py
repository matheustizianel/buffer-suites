from src.db.session import SessionLocal
from src.models.cleaner_model import CleanerModel
from src.enums.staff_shift import StaffShift


class CleanerController:
    def create_cleaner(self, staff_id, shift=StaffShift.DAY, is_on_shift=True):
        session = SessionLocal()
        try:
            cleaner = CleanerModel(
                staff_id=staff_id,
                shift=shift,
                is_on_shift=is_on_shift
            )
            session.add(cleaner)
            session.commit()
            session.refresh(cleaner)
            return cleaner
        finally:
            session.close()

    def get_cleaner_by_id(self, cleaner_id):
        session = SessionLocal()
        try:
            return session.get(CleanerModel, cleaner_id)
        finally:
            session.close()

    def list_cleaners(self):
        session = SessionLocal()
        try:
            return session.query(CleanerModel).all()
        finally:
            session.close()

    def update_cleaner(self, cleaner_id, **kwargs):
        session = SessionLocal()
        try:
            cleaner = session.get(CleanerModel, cleaner_id)
            if not cleaner:
                return None

            for key, value in kwargs.items():
                if hasattr(cleaner, key):
                    setattr(cleaner, key, value)

            session.commit()
            session.refresh(cleaner)
            return cleaner
        finally:
            session.close()

    def delete_cleaner(self, cleaner_id):
        session = SessionLocal()
        try:
            cleaner = session.get(CleanerModel, cleaner_id)
            if not cleaner:
                return False

            session.delete(cleaner)
            session.commit()
            return True
        finally:
            session.close()
