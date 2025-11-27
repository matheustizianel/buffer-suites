import pytest
from src.controllers.staff_controller import StaffController
from src.controllers.cleaner_controller import CleanerController

from src.models.cleaner_model import CleanerModel
from src.models.staff_model import StaffModel
from src.db.session import SessionLocal

from src.enums.staff_shift import StaffShift


@pytest.fixture
def staff_controller():
    return StaffController()

@pytest.fixture
def cleaner_controller():
    return CleanerController()

@pytest.fixture(autouse=True)
def clear_db():
    session = SessionLocal()
    session.query(CleanerModel).delete()
    session.query(StaffModel).delete()
    session.commit()
    yield
    session.query(CleanerModel).delete()
    session.query(StaffModel).delete()
    session.commit()
    session.close()

def test_create_cleaner(staff_controller, cleaner_controller):
    staff = staff_controller.create_staff("Mario", "cleaner")

    cleaner = cleaner_controller.create_cleaner(
        staff_id=staff.id,
        shift=StaffShift.NIGHT
    )

    assert cleaner.id is not None
    assert cleaner.staff_id == staff.id
    assert cleaner.shift == StaffShift.NIGHT

def test_list_cleaners(staff_controller, cleaner_controller):
    s1 = staff_controller.create_staff("John", "cleaner")
    s2 = staff_controller.create_staff("Bob", "cleaner")

    cleaner_controller.create_cleaner(s1.id)
    cleaner_controller.create_cleaner(s2.id)

    cleaners = cleaner_controller.list_cleaners()
    assert len(cleaners) == 2

def test_update_cleaner(staff_controller, cleaner_controller):
    staff = staff_controller.create_staff("Mike", "cleaner")
    cleaner = cleaner_controller.create_cleaner(staff.id)

    updated = cleaner_controller.update_cleaner(
        cleaner.id,
        shift=StaffShift.EVENING,
        is_on_shift=False
    )

    assert updated.shift == StaffShift.EVENING
    assert updated.is_on_shift is False

def test_delete_cleaner(staff_controller, cleaner_controller):
    staff = staff_controller.create_staff("Julia", "cleaner")
    cleaner = cleaner_controller.create_cleaner(staff.id)

    success = cleaner_controller.delete_cleaner(cleaner.id)
    assert success is True

    session = SessionLocal()
    deleted = session.get(CleanerModel, cleaner.id)
    assert deleted is None
    session.close()
