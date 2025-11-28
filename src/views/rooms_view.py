import customtkinter as ctk
from tkinter import ttk
from src.controllers.room_controller import RoomController
from src.enums.room_status import RoomStatus

ROOM_TYPES = ["Standard", "Deluxe", "Suite", "Economy"]

class RoomsView(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master)

        self.controller = RoomController()

        title = ctk.CTkLabel(self, text="Room", font=ctk.CTkFont(size=26, weight="bold"))
        title.pack(padx=20, pady=(20, 10), anchor="w")

        self.notification = ctk.CTkLabel(self, text="", font=("Arial", 13))
        self.notification.pack()

        form = ctk.CTkFrame(self, corner_radius=10)
        form.pack(fill="x", padx=20, pady=10)

        form.grid_columnconfigure(1, weight=1)

        ctk.CTkLabel(form, text="Room Number:").grid(row=0, column=0, padx=5, pady=8, sticky="w")
        self.room_number_entry = ctk.CTkEntry(form)
        self.room_number_entry.grid(row=0, column=1, padx=10, pady=8, sticky="ew")

        ctk.CTkLabel(form, text="Room Type:").grid(row=1, column=0, padx=5, pady=8, sticky="w")
        self.room_type_option = ctk.CTkOptionMenu(
            form,
            values=ROOM_TYPES,
        )
        self.room_type_option.grid(row=1, column=1, padx=10, pady=8, sticky="ew")

        ctk.CTkLabel(form, text="Status:").grid(row=2, column=0, padx=5, pady=8, sticky="w")
        self.status_option = ctk.CTkOptionMenu(
            form,
            values=[s.name for s in RoomStatus],
        )
        self.status_option.grid(row=2, column=1, padx=10, pady=8, sticky="ew")

        create_btn = ctk.CTkButton(form, text="Add Room", fg_color="#2E8B57", hover_color="#226b43", command=self.create_room)
        create_btn.grid(row=3, column=0, columnspan=2, pady=12, sticky="n")

        table_frame = ctk.CTkFrame(self, corner_radius=10)
        table_frame.pack(fill="both", expand=True, padx=20, pady=10)

        columns = ("id", "number", "type", "status")

        self.table = ttk.Treeview(
            table_frame,
            columns=columns,
            show="headings",
            height=10
        )

        self.table.heading("id", text="ID")
        self.table.heading("number", text="Room Number")
        self.table.heading("type", text="Room Type")
        self.table.heading("status", text="Status")

        self.table.column("id", width=50, anchor="center")
        self.table.column("number", width=120, anchor="center")
        self.table.column("type", width=150, anchor="center")
        self.table.column("status", width=120, anchor="center")

        scrollbar = ttk.Scrollbar(table_frame, orient="vertical", command=self.table.yview)
        self.table.configure(yscrollcommand=scrollbar.set)

        self.table.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")

        action_row = ctk.CTkFrame(self, corner_radius=10)
        action_row.pack(padx=20, pady=10, fill="x")

        ctk.CTkLabel(action_row, text="Room ID:", font=ctk.CTkFont(size=14)).grid(
            row=0, column=0, padx=8, pady=10
        )

        self.action_id_entry = ctk.CTkEntry(action_row, width=120)
        self.action_id_entry.grid(row=0, column=1, padx=8, pady=10)

        search_btn = ctk.CTkButton(
            action_row,
            text="Search",
            fg_color="#444444",
            hover_color="#333333",
            width=100,
            command=self.search_room
        )
        search_btn.grid(row=0, column=4, padx=10)

        show_all_btn = ctk.CTkButton(
            action_row,
            text="Show All",
            fg_color="#444444",
            hover_color="#333333",
            width=110,
            command=self.refresh_rooms
        )
        show_all_btn.grid(row=0, column=5, padx=10)

        delete_btn = ctk.CTkButton(
            action_row,
            text="Delete",
            fg_color="firebrick",
            hover_color="#8B0000",
            width=100,
            command=self.delete_room
        )
        delete_btn.grid(row=0, column=2, padx=10)

        update_btn = ctk.CTkButton(
            action_row,
            text="Update",
            fg_color="#4b8bc8",
            hover_color="#3a70a5",
            width=100,
            command=self.update_room
        )
        update_btn.grid(row=0, column=3, padx=10)

        self.refresh_rooms()

    def show_message(self, msg, success=True):
        color = "lightgreen" if success else "red"
        self.notification.configure(text=msg, text_color=color)

    def create_room(self):
        num = self.room_number_entry.get().strip()
        rtype = self.room_type_option.get()
        status = RoomStatus[self.status_option.get()]

        if not num.isdigit():
            self.show_message("Room number must be numeric", False)
            return

        room = self.controller.create_room(int(num), rtype, status)
        self.show_message(f"Room created (ID {room.id})")

        self.room_number_entry.delete(0, "end")

        self.refresh_rooms()

    def search_room(self):
        rid = self.action_id_entry.get().strip()

        if not rid.isdigit():
            self.show_message("Invalid ID.", False)
            return

        room = self.controller.get_room_by_id(int(rid))

        if not room:
            self.show_message("Room not found.", False)
            return

        for row in self.table.get_children():
            self.table.delete(row)

        self.table.insert("", "end", values=(
            room.id,
            room.room_number,
            room.room_type,
            room.status.name

        ))

        self.show_message(f"Showing room {room.id}.", True)

    def delete_room(self):
        rid = self.action_id_entry.get().strip()

        if not rid.isdigit():
            self.show_message("Invalid ID", False)
            return

        success = self.controller.delete_room(int(rid))

        if success:
            self.show_message("Room deleted")
        else:
            self.show_message("Room not found", False)

        self.action_id_entry.delete(0, "end")
        self.refresh_rooms()

    def update_room(self):
        rid = self.action_id_entry.get().strip()

        if not rid.isdigit():
            self.show_message("Invalid ID", False)
            return

        num = self.room_number_entry.get().strip()
        rtype = self.room_type_option.get()
        status = RoomStatus[self.status_option.get()]

        updated = self.controller.update_room(
            rid,
            room_number=int(num) if num else None,
            room_type=rtype,
            status=status
        )

        if updated:
            self.show_message("Room updated successfully")
        else:
            self.show_message("Room not found", False)

        self.refresh_rooms()

    def refresh_rooms(self):
        for row in self.table.get_children():
            self.table.delete(row)

        rooms = self.controller.list_rooms()

        for r in rooms:
            self.table.insert(
                "",
                "end",
                values=(r.id, r.room_number, r.room_type, r.status.name)
            )