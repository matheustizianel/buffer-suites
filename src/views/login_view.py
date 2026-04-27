import customtkinter as ctk
from src.services.auth_service import AuthService
from src.core.session import AppSession

class LoginView(ctk.CTkFrame):
    def __init__(self, master, on_login_success, on_register_click):
        super().__init__(master)
        self.on_login_success = on_login_success
        self.on_register_click = on_register_click

        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)

        container = ctk.CTkFrame(self)
        container.grid(row=0, column=0)

        container.grid_columnconfigure(0, weight=1)

        title = ctk.CTkLabel(container, text="Login", font=ctk.CTkFont(size=26, weight="bold"))
        title.grid(row=0, column=0, padx=20, pady=(20, 10), sticky="w")

        subtitle = ctk.CTkLabel(container, text="Access your account", font=ctk.CTkFont(size=16))
        subtitle.grid(row=1, column=0, padx=20, pady=(0, 20), sticky="w")

        form_frame = ctk.CTkFrame(container)
        form_frame.grid(row=2, column=0, padx=20, pady=10, sticky="w")

        form_frame.grid_columnconfigure(0, weight=1)

        lbl_username = ctk.CTkLabel(form_frame, text="Username")
        lbl_username.grid(row=0, column=0, sticky="w", pady=(10, 5))

        self.entry_username = ctk.CTkEntry(form_frame, width=250)
        self.entry_username.grid(row=1, column=0, pady=(0, 10))

        lbl_password = ctk.CTkLabel(form_frame, text="Password")
        lbl_password.grid(row=2, column=0, sticky="w", pady=(10, 5))

        self.entry_password = ctk.CTkEntry(form_frame, show="*", width=250)
        self.entry_password.grid(row=3, column=0, pady=(0, 10))

        btn_login = ctk.CTkButton(form_frame, text="Login", command=self.handle_login, width=250)
        btn_login.grid(row=4, column=0, pady=(10, 5))

        btn_register = ctk.CTkButton(form_frame, text="Create account", command=self.on_register_click, width=250)
        btn_register.grid(row=5, column=0, pady=(5, 10))

        self.lbl_message = ctk.CTkLabel(self, text="", text_color="red")
        self.lbl_message.grid(row=3, column=0, padx=20, pady=(10, 10), sticky="w")

    def handle_login(self):
        username = self.entry_username.get()
        password = self.entry_password.get()

        user = AuthService.login(username, password)

        if user:
            AppSession.current_user = user
            self.on_login_success()
        else:
            self.lbl_message.configure(text="Invalid username or password")