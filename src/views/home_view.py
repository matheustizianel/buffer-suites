import customtkinter as ctk


class HomeView(ctk.CTkFrame):

    def __init__(self, master):
        super().__init__(master)

        label = ctk.CTkLabel(
            self,
            text="🏨 Welcome to Buffer Suites Hotel",
            font=("Arial", 26, "bold")
        )
        label.pack(pady=40)

        desc = ctk.CTkLabel(
            self,
            text="Select an option from the left menu to begin.",
            font=("Arial", 18)
        )
        desc.pack()
