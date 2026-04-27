from src.services.auth_service import AuthService

try:
    AuthService.register("admin", "admin123", role="receptionist")
    print("Receptionist created")
except Exception as e:
    print("Already exists or error:", e)