import bcrypt
from src.models.user_model import UserModel
from src.db.session import SessionLocal

class AuthService:
    def hash_password(password):
        return bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode()
    
    def verify_password(password, hashed):
        return bcrypt.checkpw(password.encode(), hashed.encode())
    
    def register(username, password, role="guest"):
        db = SessionLocal()

        existing_user = db.query(UserModel).filter_by(username=username).first()
        if existing_user:
            db.close()
            raise Exception("Username already exists!")
        
        user = UserModel(username=username, password_hash=AuthService.hash_password(password), role=role)

        db.add(user)
        db.commit()
        db.close()

    def login(username, password):
        db = SessionLocal()

        user = db.query(UserModel).filter_by(username=username).first()
        db.close()

        if not user:
            return None
        
        if AuthService.verify_password(password, user.password_hash):
            return user
        
        return None