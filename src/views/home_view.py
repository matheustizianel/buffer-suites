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

        self.build_kpi_cards()

        graph_placeholder = ctk.CTkFrame(
            self,
            height=260,
            width=700,
            corner_radius=15,
            fg_color=None
        )
        graph_placeholder.grid(row=3, column=0, padx=20, pady=20, sticky="nsew")
        graph_placeholder.grid_propagate(False)

        graph_label = ctk.CTkLabel(
            graph_placeholder,
            text="(Graph Area Placeholder)\nFuture Charts & Insights",
            font=ctk.CTkFont(size=14, weight="normal")
        )
        graph_label.place(relx=0.5, rely=0.5, anchor="center")

        self.grid_columnconfigure(0, weight=1)

    def build_kpi_cards(self):
        card_frame = ctk.CTkFrame(self, fg_color="transparent")
        card_frame.grid(row=2, column=0, padx=20, pady=(10, 20), sticky="w")

        card_specs = {
            "height": 120,
            "width": 220,
            "corner_radius": 15,
            "fg_color": None
        }

        card1 = ctk.CTkFrame(card_frame, **card_specs)
        card1.grid(row=0, column=0, padx=10, pady=10)
        ctk.CTkLabel(
            card1,
            text="Guests",
            font=ctk.CTkFont(size=14)
        ).place(relx=0.5, rely=0.25, anchor="center")
        self.lbl_guests = ctk.CTkLabel(
            card1,
            text="0",
            font=ctk.CTkFont(size=28, weight="bold")
        )
        self.lbl_guests.place(relx=0.5, rely=0.65, anchor="center")

        card2 = ctk.CTkFrame(card_frame, **card_specs)
        card2.grid(row=0, column=1, padx=10, pady=10)
        ctk.CTkLabel(
            card2,
            text="Available Rooms",
            font=ctk.CTkFont(size=14)
        ).place(relx=0.5, rely=0.25, anchor="center")
        self.lbl_rooms_available = ctk.CTkLabel(
            card2,
            text="0",
            font=ctk.CTkFont(size=28, weight="bold")
        )
        self.lbl_rooms_available.place(relx=0.5, rely=0.65, anchor="center")

        card3 = ctk.CTkFrame(card_frame, **card_specs)
        card3.grid(row=0, column=2, padx=10, pady=10)
        ctk.CTkLabel(
            card3,
            text="Active Reservations",
            font=ctk.CTkFont(size=14)
        ).place(relx=0.5, rely=0.25, anchor="center")
        self.lbl_reservations_active = ctk.CTkLabel(
            card3,
            text="0",
            font=ctk.CTkFont(size=28, weight="bold")
        )
        self.lbl_reservations_active.place(relx=0.5, rely=0.65, anchor="center")