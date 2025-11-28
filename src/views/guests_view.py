import customtkinter as ctk
from tkinter import ttk
from src.controllers.guest_controller import GuestController

class GuestsView(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master)

        self.controller = GuestController()

        title = ctk.CTkLabel(self, text="Guest", font=ctk.CTkFont(size=26, weight="bold"))
        title.pack(padx=20, pady=(20, 10), anchor="w")

        self.notification = ctk.CTkLabel(self, text="", font=("Arial", 13))
        self.notification.pack()

        form = ctk.CTkFrame(self, corner_radius=10)
        form.pack(fill="x", padx=20, pady=10)

        form.grid_columnconfigure(1, weight=1)

        ctk.CTkLabel(form, text="Name:").grid(row=0, column=0, padx=5, pady=8, sticky="w")
        self.name_entry = ctk.CTkEntry(form)
        self.name_entry.grid(row=0, column=1, padx=10, pady=8, sticky="ew")

        ctk.CTkLabel(form, text="Email:").grid(row=1, column=0, padx=5, pady=8, sticky="w")
        self.email_entry = ctk.CTkEntry(form)
        self.email_entry.grid(row=1, column=1, padx=10, pady=8, sticky="ew")

        ctk.CTkLabel(form, text="Phone:").grid(row=2, column=0, padx=5, pady=8, sticky="w")
        self.phone_entry = ctk.CTkEntry(form)
        self.phone_entry.grid(row=2, column=1, padx=10, pady=8, sticky="ew")

        ctk.CTkLabel(form, text="Address:").grid(row=3, column=0, padx=5, pady=8, sticky="w")
        self.address_entry = ctk.CTkEntry(form)
        self.address_entry.grid(row=3, column=1, padx=10, pady=8, sticky="ew")

        create_btn = ctk.CTkButton(form, text="Add Guest", fg_color="#2E8B57", hover_color="#226b43", command=self.create_guest)
        create_btn.grid(row=4, column=0, columnspan=2, pady=12, sticky="n")

        table_frame = ctk.CTkFrame(self, corner_radius=10)
        table_frame.pack(fill="both", expand=True, padx=20, pady=10)

        columns = ("id", "name", "email", "phone", "address")
        self.table = ttk.Treeview(table_frame, columns=columns, show="headings", height=10)

        self.table.heading("id", text="ID")
        self.table.heading("name", text="Name")
        self.table.heading("email", text="Email")
        self.table.heading("phone", text="Phone")
        self.table.heading("address", text="Address")

        self.table.column("id", width=50, anchor="center")
        self.table.column("name", width=160, anchor="center")
        self.table.column("email", width=180, anchor="center")
        self.table.column("phone", width=120, anchor="center")
        self.table.column("address", width=220, anchor="center")

        scrollbar = ttk.Scrollbar(table_frame, orient="vertical", command=self.table.yview)
        self.table.configure(yscrollcommand=scrollbar.set)

        self.table.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")

        action_row = ctk.CTkFrame(self, corner_radius=10)
        action_row.pack(padx=20, pady=10, fill="x")

        ctk.CTkLabel(action_row, text="Guest ID:", font=ctk.CTkFont(size=14)).grid(
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
            command=self.search_guest
        )
        search_btn.grid(row=0, column=4, padx=10)

        show_all_btn = ctk.CTkButton(
            action_row,
            text="Show All",
            fg_color="#444444",
            hover_color="#333333",
            width=110,
            command=self.refresh_guests
        )
        show_all_btn.grid(row=0, column=5, padx=10)

        update_btn = ctk.CTkButton(
            action_row,
            text="Update",
            fg_color="#4b8bc8",
            hover_color="#3a70a5",
            width=100,
            command=self.update_guest
        )
        update_btn.grid(row=0, column=3, padx=10)

        delete_btn = ctk.CTkButton(
            action_row,
            text="Delete",
            fg_color="firebrick",
            hover_color="#8B0000",
            width=100,
            command=self.delete_guest
        )
        delete_btn.grid(row=0, column=2, padx=10)


        self.after(200, self.refresh_guests)

    def show_message(self, msg, success=True):
        color = "lightgreen" if success else "red"
        self.notification.configure(text=msg, text_color=color)

    def create_guest(self):
        name = self.name_entry.get().strip()
        email = self.email_entry.get().strip()
        phone = self.phone_entry.get().strip()
        address = self.address_entry.get().strip()

        if not name:
            self.show_message("Name cannot be empty!", False)
            return

        guest = self.controller.create_guest(
            name=name,
            email=email,
            phone_number=phone,
            address=address
        )

        self.show_message(f"Guest created (ID {guest.id})")

        self.name_entry.delete(0, "end")
        self.email_entry.delete(0, "end")
        self.phone_entry.delete(0, "end")
        self.address_entry.delete(0, "end")

        self.refresh_guests()

    def search_guest(self):
        gid = self.action_id_entry.get().strip()

        if not gid.isdigit():
            self.show_message("Invalid ID.", False)
            return

        guest = self.controller.get_guest_by_id(int(gid))

        if not guest:
            self.show_message("Guest not found.", False)
            return

        for row in self.table.get_children():
            self.table.delete(row)

        self.table.insert("", "end", values=(
            guest.id,
            guest.name,
            guest.email or "-",
            guest.phone_number or "-",
            guest.address or "-"
        ))

        self.show_message(f"Showing guest {guest.id}.", True)

    def delete_guest(self):
        gid = self.action_id_entry.get().strip()

        if not gid.isdigit():
            self.show_message("Invalid ID", False)
            return

        success = self.controller.delete_guest(int(gid))

        if success:
            self.show_message("Guest deleted.")
        else:
            self.show_message("Guest not found!", False)

        self.action_id_entry.delete(0, "end")
        self.refresh_guests()

    def update_guest(self):
        gid = self.action_id_entry.get().strip()

        if not gid.isdigit():
            self.show_message("Invalid ID.", False)
            return

        name = self.name_entry.get().strip()
        email = self.email_entry.get().strip()
        phone = self.phone_entry.get().strip()
        address = self.address_entry.get().strip()

        updated = self.controller.update_guest(
            gid,
            name=name if name else None,
            email=email if email else None,
            phone_number=phone if phone else None,
            address=address if address else None
        )

        if not updated:
            self.show_message("Guest not found.", False)
            return

        self.show_message(f"Guest {gid} updated successfully!", True)
        self.refresh_guests()

    def refresh_guests(self):
        # clear table
        for row in self.table.get_children():
            self.table.delete(row)

        guests = self.controller.list_guests()

        for g in guests:
            self.table.insert("", "end", values=(
                g.id,
                g.name,
                g.email or "-",
                g.phone_number or "-",
                g.address or "-"
            ))
