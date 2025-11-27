import pytest
from src.controllers.staff_controller import StaffController
from src.models.staff_model import StaffModel
from src.db.session import SessionLocal


@pytest.fixture
def staff_controller():
    return StaffController()

@pytest.fixture(autouse=True)
def clear_db():
    session = SessionLocal()
    session.query(StaffModel).delete()
    session.commit()
    yield
    session.query(StaffModel).delete()
    session.commit()
    session.close()

def test_create_staff(staff_controller):
    staff = staff_controller.create_staff(
        name="Maria",
        role="manager",
        email="maria@test.com"
    )

    assert staff.id is not None
    assert staff.name == "Maria"
    assert staff.role == "manager"

def test_get_staff_by_id(staff_controller):
    created = staff_controller.create_staff("John", "clerk")
    found = staff_controller.get_staff_by_id(created.id)

    assert found is not None
    assert found.id == created.id

def test_list_staff(staff_controller):
    staff_controller.create_staff("A", "role1")
    staff_controller.create_staff("B", "role2")

    staff_members = staff_controller.list_staff()
    assert len(staff_members) == 2

def test_update_staff(staff_controller):
    created = staff_controller.create_staff("Mike", "cleaner")
    updated = staff_controller.update_staff(created.id, role="supervisor")

    assert updated.role == "supervisor"

def test_delete_staff(staff_controller):
    created = staff_controller.create_staff("Paul", "technician")
    success = staff_controller.delete_staff(created.id)

    assert success is True

    session = SessionLocal()
    deleted = session.get(StaffModel, created.id)
    assert deleted is None
    session.close()
