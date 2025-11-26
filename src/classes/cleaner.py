from src.classes.staff import Staff
from .enums.staff_shift import StaffShift

class Cleaner(Staff):
    def __init__(self, name, email, phone_number = None, address = None):
        super().__init__(name, email, phone_number, address)
        self.cleaning_history = []
        self.pending_cleaning_tasks = []
        self.shift = StaffShift.DAY
        self.is_on_shift = True

    def add_cleaning_task(self, room):
        if room not in self.pending_cleaning_tasks:
            self.pending_cleaning_tasks.append(room)
            print(f"Cleaning task assigned to {self.name}:  Clean room {room.room_number}.")
        else:
            print(f"Room {room.room_number} is already assigned to {self.name}.")

    def clean_room(self, room):
        if room not in self.pending_cleaning_tasks:
            raise Exception(f"Room {room.room_number} is not assigned to {self.name}.")

        self.pending_cleaning_tasks.remove(room)
        self.cleaning_history.append(room)

        print(f"{self.name} cleaned room {room.room_number}.")


