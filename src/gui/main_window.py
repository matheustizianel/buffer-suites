import customtkinter as ctk
from src.gui.sidebar import Sidebar
from src.views.login_view import LoginView
from src.views.register_view import RegisterView
from src.core.session import AppSession


class MainWIndow:
    def __init__(self):
        ctk.set_appearance_mode("system")
        ctk.set_default_color_theme("blue")

        self.root = ctk.CTk()
        self.root.title("Buffer Suites")
        self.root.geometry("1100x700")

        self.view_container = ctk.CTkFrame(self.root, corner_radius=0)
        self.view_container.pack(side="right", expand=True, fill="both")

        self.sidebar = None
        self.active_view = None

        self.show_login()

    def show_login(self):
        if self.active_view:
            self.active_view.destroy()

        if self.sidebar:
            self.sidebar.destroy()
            self.sidebar = None

        self.active_view = LoginView(self.view_container, self.after_login, self.show_register)
        self.active_view.pack(expand=True, fill="both")

    def switch_view(self, view_name, data=None):
        user = AppSession.current_user

        if user.role != "receptionist" and view_name in ["guests", "reservations"]:
            return
        
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

            case "browse_rooms":
                from ..views.browse_rooms_view import BrowseRoomsView
                self.active_view = BrowseRoomsView(self.view_container, self.open_room_details)

            case "room_details":
                from ..views.room_details_view import RoomDetailsView
                self.active_view = RoomDetailsView(self.view_container, data, lambda: self.switch_view("browse_rooms"))
            
            case "reservations":
                from ..views.reservations_view import ReservationsView
                self.active_view = ReservationsView(self.view_container)

        self.active_view.pack(expand=True, fill="both")

    def after_login(self):
        if self.active_view:
            self.active_view.destroy()

        if self.sidebar:
            self.sidebar.destroy()
            self.sidebar = None

        self.sidebar = Sidebar(self.root, self.switch_view, self.show_login)
        self.sidebar.pack(side="left", fill="y")

        self.view_container.pack_forget()
        self.view_container = ctk.CTkFrame(self.root, corner_radius=0)
        self.view_container.pack(side="right", expand=True, fill="both")

        user = AppSession.current_user

        if user.role == "receptionist":
            self.switch_view("home")
        else:
            self.switch_view("browse_rooms")

    def show_register(self):
        if self.active_view:
            self.active_view.destroy()

        self.active_view = RegisterView(self.view_container, self.show_login)
        self.active_view.pack(expand=True, fill="both")

    def open_room_details(self, room):
        self.switch_view("room_details", room)

    def run(self):
        self.root.mainloop()