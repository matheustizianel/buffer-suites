import customtkinter as ctk
from src.core.session import AppSession

class Sidebar(ctk.CTkFrame):
    def __init__(self, master, switch_view_callback, on_logout):
        super().__init__(master, width=200, corner_radius=0)
        self.switch_view = switch_view_callback
        self.on_logout = on_logout

        title = ctk.CTkLabel(
            self, 
            text="Buffer Suites",
            font=("Arial", 22, "bold")
        )
        title.pack(pady=20)

        user = AppSession.current_user

        lbl_user = ctk.CTkLabel(self, text=f"Logged in as:\n{user.username}", font=("Arial", 12))
        lbl_user.pack(pady=(0, 10))

        if user.role == "receptionist":
            self.add_button("Home", "home")
            self.add_button("Guests", "guests")
            self.add_button("Rooms", "rooms")
            self.add_button("Reservations", "reservations")
        else: 
            self.add_button("Browse Rooms", "browse_rooms")

        appearance_label = ctk.CTkLabel(self, text="Appearance Mode:")
        appearance_label.pack(pady=(40, 5))

        appearance_option = ctk.CTkOptionMenu(
            self,
            values=["Dark", "Light", "System"],
            command=self.change_appearance
        )

        appearance_option.pack()

        btn_logout = ctk.CTkButton(self, text="Logout", fg_color="red", hover_color="#a00", command=self.logout)
        btn_logout.pack(side="bottom", fill="x", padx=10, pady=10)

    def add_button(self, text, view_name):
        btn = ctk.CTkButton(
            self,
            text=text,
            command=lambda: self.switch_view(view_name)
        )
        btn.pack(fill="x", padx=10, pady=5)

    def change_appearance(self, mode):
        mode = mode.lower()
        if mode == "system":
            ctk.set_appearance_mode("system")
        else:
            ctk.set_appearance_mode(mode)

    def logout(self):
        AppSession.current_user = None
        self.on_logout()
