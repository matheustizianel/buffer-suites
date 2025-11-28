import customtkinter as ctk
from tkinter import ttk
from datetime import datetime

from src.controllers.reservation_controller import ReservationController
from src.controllers.room_controller import RoomController
from src.controllers.guest_controller import GuestController
from src.enums.reservation_status import ReservationStatus


class ReservationsView(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master)

        self.res_controller = ReservationController()
        self.room_controller = RoomController()
        self.guest_controller = GuestController()

        title = ctk.CTkLabel(self, text="Reservation", font=ctk.CTkFont(size=26, weight="bold"))
        title.pack(pady=10)

        self.notification = ctk.CTkLabel(self, text="", font=("Arial", 13))
        title.pack(padx=20, pady=(20, 10), anchor="w")

        form = ctk.CTkFrame(self, corner_radius=10)
        form.pack(fill="x", padx=20, pady=10)
        form.grid_columnconfigure(1, weight=1)

        ctk.CTkLabel(form, text="Guest ID:").grid(row=0, column=0, padx=5, pady=8, sticky="w")
        self.guest_entry = ctk.CTkEntry(form)
        self.guest_entry.grid(row=0, column=1, padx=10, pady=8, sticky="ew")

        ctk.CTkLabel(form, text="Room ID:").grid(row=1, column=0, padx=5, pady=8, sticky="w")
        self.room_entry = ctk.CTkEntry(form)
        self.room_entry.grid(row=1, column=1, padx=10, pady=8, sticky="ew")

        create_btn = ctk.CTkButton(form, text="Create Reservation",
                                   fg_color="#2E8B57", hover_color="#226b43", command=self.create_reservation)
        create_btn.grid(row=3, column=0, columnspan=2, pady=12, sticky="n")

        table_frame = ctk.CTkFrame(self, corner_radius=10)
        table_frame.pack(fill="both", expand=True, padx=20, pady=10)

        columns = ("id", "guest", "room", "status", "booking", "checkin", "checkout", "cancel")
        self.table = ttk.Treeview(table_frame, columns=columns, show="headings", height=10)

        self.table.heading("id", text="ID")
        self.table.heading("guest", text="Guest")
        self.table.heading("room", text="Room")
        self.table.heading("status", text="Status")
        self.table.heading("booking", text="Booking Time")
        self.table.heading("checkin", text="Check-in")
        self.table.heading("checkout", text="Check-out")
        self.table.heading("cancel", text="Cancellation Time")

        self.table.column("id", width=50, anchor="center")
        self.table.column("guest", width=80, anchor="center")
        self.table.column("room", width=80, anchor="center")
        self.table.column("status", width=100, anchor="center")
        self.table.column("booking", width=150, anchor="center")
        self.table.column("checkin", width=150, anchor="center")
        self.table.column("checkout", width=150, anchor="center")
        self.table.column("cancel", width=150, anchor="center")

        scrollbar = ttk.Scrollbar(table_frame, orient="vertical", command=self.table.yview)
        self.table.configure(yscrollcommand=scrollbar.set)

        self.table.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")

        action_row = ctk.CTkFrame(self, corner_radius=10)
        action_row.pack(fill="x", padx=20, pady=10)

        ctk.CTkLabel(action_row, text="Reservation ID:",
                     font=ctk.CTkFont(size=14)).grid(row=0, column=0, padx=8, pady=10)

        self.action_id_entry = ctk.CTkEntry(action_row, width=120)
        self.action_id_entry.grid(row=0, column=1, padx=8, pady=10)

        checkin_btn = ctk.CTkButton(action_row, text="Check-In",
                                    fg_color="#2E8B57", hover_color="#226b43",
                                    width=100, command=self.do_check_in)
        checkin_btn.grid(row=0, column=2, padx=10)

        checkout_btn = ctk.CTkButton(action_row, text="Check-Out",
                                     fg_color="#b8860b", hover_color="#8c6a08",
                                     width=110, command=self.do_check_out)
        checkout_btn.grid(row=0, column=3, padx=10)

        cancel_btn = ctk.CTkButton(action_row, text="Cancel",
                                   fg_color="firebrick", hover_color="#8B0000",
                                   width=100, command=self.do_cancel)
        cancel_btn.grid(row=0, column=4, padx=10)

        search_btn = ctk.CTkButton(action_row, text="Search", fg_color="#444444", hover_color="#333333", width=100, command=self.search_reservation)
        search_btn.grid(row=0, column=5, padx=10)

        show_all_btn = ctk.CTkButton(action_row, text="Show All", fg_color="#444444", hover_color="#333333", width=110, command=self.refresh_reservations)
        show_all_btn.grid(row=0, column=6, padx=10)

        self.refresh_reservations()

    def show_message(self, msg, success=True):
        color = "lightgreen" if success else "red"
        self.notification.configure(text=msg, text_color=color)

    def format_dt(self, dt):
        if not dt:
            return "-"
        return dt.strftime("%m/%d/%Y - %H:%M")

    def create_reservation(self):
        gid = self.guest_entry.get().strip()
        rid = self.room_entry.get().strip()

        if not (gid.isdigit() and rid.isdigit()):
            self.show_message("Guest ID and Room ID must be numeric.", False)
            return

        try:
            reservation = self.res_controller.create_reservation(int(gid), int(rid))
            self.show_message(f"Reservation created (ID {reservation.id})", True)
            self.refresh_reservations()
        except Exception as e:
            self.show_message(str(e), False)

    def search_reservation(self):
        rvid = self.action_id_entry.get().strip()

        if not rvid.isdigit():
            self.show_message("Invalid ID.", False)
            return

        reservation = self.res_controller.get_reservation_by_id(int(rvid))

        if not reservation:
            self.show_message("Reservation not found.", False)
            return

        for row in self.table.get_children():
            self.table.delete(row)

        self.table.insert("", "end", values=(
            reservation.id,
            reservation.guest_id,
            reservation.room_id,
            reservation.status.name,
            self.format_dt(reservation.booking_time),
            self.format_dt(reservation.checkin_time),
            self.format_dt(reservation.checkout_time),
            self.format_dt(reservation.cancellation_time),
        ))

        self.show_message(f"Showing room {reservation.id}.", True)

    def do_check_in(self):
        rid = self.action_id_entry.get().strip()
        if not rid.isdigit():
            self.show_message("Invalid ID.", False)
            return

        try:
            self.res_controller.check_in(int(rid))
            self.show_message(f"Checked in reservation {rid}.", True)
            self.refresh_reservations()
        except Exception as e:
            self.show_message(str(e), False)

    def do_check_out(self):
        rid = self.action_id_entry.get().strip()
        if not rid.isdigit():
            self.show_message("Invalid ID.", False)
            return

        try:
            self.res_controller.check_out(int(rid))
            self.show_message(f"Checked out reservation {rid}.", True)
            self.refresh_reservations()
        except Exception as e:
            self.show_message(str(e), False)

    def do_cancel(self):
        rid = self.action_id_entry.get().strip()
        if not rid.isdigit():
            self.show_message("Invalid ID.", False)
            return

        try:
            self.res_controller.cancel(int(rid))
            self.show_message(f"Reservation {rid} cancelled.", True)
            self.refresh_reservations()
        except Exception as e:
            self.show_message(str(e), False)

    def refresh_reservations(self):
        for row in self.table.get_children():
            self.table.delete(row)

        reservations = self.res_controller.list_reservations()

        for r in reservations:
            self.table.insert("", "end", values=(
                r.id,
                r.guest_id,
                r.room_id,
                r.status.name,
                self.format_dt(r.booking_time),
                self.format_dt(r.checkin_time),
                self.format_dt(r.checkout_time),
                self.format_dt(r.cancellation_time),
            ))
