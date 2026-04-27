import customtkinter as ctk
from src.controllers.review_controller import ReviewController

class RoomDetailsView(ctk.CTkFrame):
    def __init__(self, master, room, on_back):
        super().__init__(master)

        self.room = room
        self.on_back = on_back

        btn_back = ctk.CTkButton(self, text="← Back", command=self.on_back)
        btn_back.pack(anchor="w", padx=20, pady=10)

        title = ctk.CTkLabel(self, text=f"Room {room.room_number}", font=ctk.CTkFont(size=26, weight="bold"))
        title.pack(pady=10)

        ctk.CTkLabel(self, text=f"Type: {room.room_type}").pack(pady=5)

        ctk.CTkLabel(self, text=f"Status: {room.status}").pack(pady=5)

        reviews_title = ctk.CTkLabel(self, text="Reviews", font=ctk.CTkFont(size=20, weight="bold"))
        reviews_title.pack(pady=(20, 10))

        self.reviews_frame = ctk.CTkFrame(self)
        self.reviews_frame.pack(fill="both", expand=False, padx=20)

        self.load_reviews()

        self.entry_review = ctk.CTkEntry(self, width=300)
        self.entry_review.pack(pady=10)

        btn_add_review = ctk.CTkButton(self, text="Add Review", command=self.add_review)
        btn_add_review.pack(pady=(0, 20))

    def load_reviews(self):
        for widget in self.reviews_frame.winfo_children():
            widget.destroy()

        reviews = ReviewController.get_reviews_by_room(self.room.id)

        if not reviews:
            ctk.CTkLabel(self.reviews_frame, text="No reviews yet.").pack()
            return
        
        for review in reviews:
            ctk.CTkLabel(
                self.reviews_frame,
                text=f"- {review.content}",
                anchor="w",
                justify="left"
            ).pack(fill="x", pady=2)

    def add_review(self):
        text = self.entry_review.get()

        if not text.strip():
            return
        
        ReviewController.create_review(self.room.id, text)

        self.entry_review.delete(0, "end")

        self.load_reviews()