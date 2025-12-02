import customtkinter as ctk
from .sidebar import Sidebar

class MainWIndow:
    def __init__(self):
        ctk.set_appearance_mode("system")
        ctk.set_default_color_theme("blue")

        self.root = ctk.CTk()
        self.root.title("Buffer Suites")
        self.root.geometry("1100x700")

        self.sidebar = Sidebar(self.root, self.switch_view)
        self.sidebar.pack(side="left", fill="y")

        self.view_container = ctk.CTkFrame(self.root, corner_radius=0)
        self.view_container.pack(side="right", expand=True, fill="both")

        self.active_view = None

        self.switch_view("home")

    def switch_view(self, view_name):
        if self.active_view is not None:
            self.active_view.destroy()

        match view_name:
            case "home":
                from ..views.home_view import HomeView
                self.active_view = HomeView(self.view_container)
                self.active_view.update_dashboard()
            
            case "guests":
                from ..views.guests_view import GuestsView
                self.active_view = GuestsView(self.view_container)

            case "rooms":
                from ..views.rooms_view import RoomsView
                self.active_view = RoomsView(self.view_container)
            
            case "reservations":
                from ..views.reservations_view import ReservationsView
                self.active_view = ReservationsView(self.view_container)

        self.active_view.pack(expand=True, fill="both")

    def run(self):
        self.root.mainloop()