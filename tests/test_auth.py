from src.services.auth_service import AuthService
from src.db.session import SessionLocal
from src.models.user_model import UserModel

def test_register_login():
    db = SessionLocal()

    db.query(UserModel).filter_by(username="test_user").delete()
    db.commit()
    db.close()

    AuthService.register("test_user", "1234", role="guest")
    user = AuthService.login("test_user", "1234")

    assert user is not None
    assert user.username == "test_user"
    assert user.role == "guest"