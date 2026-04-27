import customtkinter as ctk
from src.services.auth_service import AuthService

class RegisterView(ctk.CTkFrame):
    def __init__(self, master, on_register_success):
        super().__init__(master)

        self.on_register_success = on_register_success

        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)

        container = ctk.CTkFrame(self)
        container.grid(row=0, column=0)

        container.grid_columnconfigure(0, weight=1)

        title = ctk.CTkLabel(container, text="Register", font=ctk.CTkFont(size=26, weight="bold"))
        title.grid(row=0, column=0, padx=20, pady=(20, 10), sticky="w")

        subtitle = ctk.CTkLabel(container, text="Create a new account", font=ctk.CTkFont(size=16))
        subtitle.grid(row=1, column=0, padx=20, pady=(0, 20), sticky="w")

        form_frame = ctk.CTkFrame(container)
        form_frame.grid(row=2, column=0, padx=20, pady=10)

        lbl_username = ctk.CTkLabel(form_frame, text="Username")#.grid(row=0, column=0, sticky="w")
        lbl_username.grid(row=0, column=0, sticky="w", pady=(10, 5))

        self.entry_username = ctk.CTkEntry(form_frame, width=250)
        self.entry_username.grid(row=1, column=0, pady=(0, 10))

        lbl_password = ctk.CTkLabel(form_frame, text="Password")#.grid(row=2, column=0, sticky="w")
        lbl_password.grid(row=2, column=0, sticky="w", pady=(10, 5))

        self.entry_password = ctk.CTkEntry(form_frame, show="*", width=250)
        self.entry_password.grid(row=3, column=0, pady=(0, 10))

        btn_register = ctk.CTkButton(form_frame, text="Create Account", command=self.handle_register)
        btn_register.grid(row=4, column=0, pady=10)

        btn_back = ctk.CTkButton(form_frame, text="Back to Login", command=self.on_register_success)
        btn_back.grid(row=5, column=0, pady=(5, 20))

        self.lbl_message = ctk.CTkLabel(container, text="", text_color="red")
        self.lbl_message.grid(row=3, column=0, padx=20, pady=10, sticky="w")

    def handle_register(self):
        username = self.entry_username.get()
        password = self.entry_password.get()

        try:
            AuthService.register(username, password, role="guest")
            self.on_register_success()
        except Exception as e:
            self.lbl_message.configure(text=str(e))