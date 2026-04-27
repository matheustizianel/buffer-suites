import customtkinter as ctk
from src.controllers.room_controller import RoomController

class BrowseRoomsView(ctk.CTkFrame):
    def __init__(self, master, on_open_room):
        super().__init__(master)

        self.on_open_room = on_open_room

        title = ctk.CTkLabel(self, text="Available Rooms", font=ctk.CTkFont(size=26, weight="bold"))
        title.pack(pady=20)

        self.rooms_frame = ctk.CTkFrame(self)
        self.rooms_frame.pack(fill="both", expand=True, padx=20, pady=10)

        self.load_rooms()

    def load_rooms(self):
        rooms = RoomController.list_rooms()

        for room in rooms:
            card = ctk.CTkFrame(self.rooms_frame)
            card.pack(fill="x", pady=5)

            ctk.CTkLabel(card, text=f"Room {room.room_number}").pack(side="left", padx=10)

            btn = ctk.CTkButton(card, text="View", command=lambda r=room: self.on_open_room(r))
            btn.pack(side="right", padx=10)
