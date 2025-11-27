import customtkinter as ctk

class Sidebar(ctk.CTkFrame):
    def __init__(self, master, switch_view_callback):
        super().__init__(master, width=200, corner_radius=0)
        self.switch_view = switch_view_callback

        title = ctk.CTkLabel(
            self, 
            text="Buffer Suites", 
            font=("Arial", 22, "bold")
        )
        title.pack(pady=20)

        self.add_button("Home", "home")
        self.add_button("Guests", "guests")
        self.add_button("Rooms", "rooms")
        self.add_button("Reservations", "reservations")
        self.add_button("Staff", "staff")
        self.add_button("Cleaners", "cleaners")

        appearance_label = ctk.CTkLabel(self, text="Appearance Mode:")
        appearance_label.pack(pady=(40, 5))

        appearance_option = ctk.CTkOptionMenu(
            self,
            values=["Dark", "Light", "System"],
            command=self.change_appearance
        )
        appearance_option.pack()

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
