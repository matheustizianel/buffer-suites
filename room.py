class Room:
    def __init__(self, room_number, room_type):
        self.room_number = room_number
        self.room_type = room_type
        self.is_available = True
        self.is_booked = False
        self.is_occupied = False
        self.current_guest = None

    def mark_booked(self, guest_name):
        if self.is_available and not self.is_booked:
            self.is_booked = True
            self.current_guest = guest_name
            print(f"Room {self.room_number} is booked to {guest_name}")

        
        
    def assign_guest(self, guest_name):
        if self.is_occupied:
            print("Room is already occupied")

        self.is_available = False
        self.is_occupied = True
        self.is_booked = True
        self.current_guest = guest_name

        print(f"✅ {guest_name} checked into Room {self.room_number} ({self.room_type}).")

    def remove_guest(self):
        """
        Checks out the current guest and frees the room.
        """
        if self.is_occupied or self.is_booked:
            print(f"🔓 {self.current_guest} checked out from Room {self.room_number}.")
            self.is_available = True
            self.is_booked = False
            self.is_occupied = False
            self.current_guest = None
        else:
            print(f"⚠️ Room {self.room_number} is already available.")

    def show_details(self):
        """
        Displays the current room status in a readable format.
        """
        if self.is_occupied:
            status = f"Occupied by {self.current_guest} ❌"
        elif self.is_booked:
            status = f"Booked by {self.current_guest} 🕓"
        else:
            status = "Available ✅"

        print(f"Room {self.room_number} | Type: {self.room_type} | {status}")

    def __str__(self):
        if self.is_occupied:
            status = f"Occupied by {self.current_guest}"
        elif self.is_booked:
            status = f"Booked by {self.current_guest}"
        else:
            status = "Available"
        return f"Room {self.room_number} ({self.room_type}) - {status}"
        


