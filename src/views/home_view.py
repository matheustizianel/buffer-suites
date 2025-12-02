import customtkinter as ctk

class HomeView(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master)

        title = ctk.CTkLabel(self, text="Home", font=ctk.CTkFont(size=26, weight="bold"))
        title.grid(row=0, column=0, padx=20, pady=(20, 10), sticky="w")

        subtitle = ctk.CTkLabel(
            self,
            text="Quick view dashboard",
            font=ctk.CTkFont(size=16)
        )
        subtitle.grid(row=1, column=0, padx=20, pady=(0, 20), sticky="w")

        self.build_cards()

    def build_cards(self):
        card_frame = ctk.CTkFrame(self, fg_color="transparent")
        card_frame.grid(row=2, column=0, padx=20, pady=(10, 20))

        card_specs = {
            "height": 120,
            "width": 220,
            "corner_radius": 15,
            "fg_color": None
        }

        cards_row1 = [
            ("Total Registered Guests", "lbl_total_guests"),
            ("Guests Staying Now", "lbl_guests_occupied"),
            ("Active Reservations", "lbl_res_active"),
        ]

        cards_row2 = [
            ("Rooms Available", "lbl_rooms_available"),
            ("Rooms Occupied", "lbl_rooms_occupied"),
            ("Cancelled Reservations", "lbl_res_cancelled"),
        ]

        for idx, (text, attr) in enumerate(cards_row1):
            card = ctk.CTkFrame(card_frame, **card_specs)
            card.grid(row=0, column=idx, padx=10, pady=10)

            ctk.CTkLabel(card, text=text, font=("Arial", 14)).place(relx=0.5, rely=0.25, anchor="center")
            lbl = ctk.CTkLabel(card, text="0", font=ctk.CTkFont(size=28, weight="bold"))
            lbl.place(relx=0.5, rely=0.65, anchor="center")
            setattr(self, attr, lbl)

        for idx, (text, attr) in enumerate(cards_row2):
            card = ctk.CTkFrame(card_frame, **card_specs)
            card.grid(row=1, column=idx, padx=10, pady=10)

            ctk.CTkLabel(card, text=text, font=("Arial", 14)).place(relx=0.5, rely=0.25, anchor="center")
            lbl = ctk.CTkLabel(card, text="0", font=ctk.CTkFont(size=28, weight="bold"))
            lbl.place(relx=0.5, rely=0.65, anchor="center")
            setattr(self, attr, lbl)

    def update_dashboard(self):
        from src.services.dashboard_service import DashboardService

        data = DashboardService.get_dashboard_stats()

        self.lbl_total_guests.configure(text=str(data["guests_total"]))
        self.lbl_guests_occupied.configure(text=str(data["guests_occupied"]))
        self.lbl_res_active.configure(text=str(data["reservations_active"]))
        self.lbl_rooms_available.configure(text=str(data["rooms_available"]))
        self.lbl_rooms_occupied.configure(text=str(data["rooms_occupied"]))
        self.lbl_res_cancelled.configure(text=str(data["reservations_cancelled"]))
