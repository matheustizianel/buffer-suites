import customtkinter as ctk


class StaffView(ctk.CTkFrame):

    def __init__(self, master):
        super().__init__(master)

        title = ctk.CTkLabel(self, text="Staff Management", font=("Arial", 22, "bold"))
        title.pack(pady=20)
