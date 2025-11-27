import customtkinter as ctk


class GuestsView(ctk.CTkFrame):

    def __init__(self, master):
        super().__init__(master)

        title = ctk.CTkLabel(self, text="Guests Management", font=("Arial", 22, "bold"))
        title.pack(pady=20)
