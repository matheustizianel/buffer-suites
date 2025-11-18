from src import Guest, Room, Staff, Hotel

def main():
    hotel = Hotel("Buffer Suites", "12345 Memory Bus, Motherboard PC, Brand Serial#")

    print(f"Welcome to 🏨 {hotel.name} 🏨 - Here downtime becomes uptime")

    guest = Guest("Matheus Tizianel", "11305 Nano Ln Jacksonville FL 32256 US")
    cleaner = Staff("James Bond", "Cleaner", "45 Palm St, Miami FL 12345 US")
    receptionist = Staff("John", "Receptionist", "101 Ocean Dr, Miami FL 67891 US")

    room = Room(101, "Queen - Ocean View")

    print()
    room.show_details()
    print()

    guest.book_room(room)
    print()

    room.show_details()
    print()

    guest.cancel_booking(room)
    print()


    # while True:
    #     print("\n====Menu====")
    #     print("1. View Room Status")
    #     print("2. Book Room")
    #     print("3. Check In")
    #     print("4. Check Out")
    #     print("5. Exit")

    #     print()
    #     choice = int(input("Select an option (1-5): "))
    #     print()

    #     match choice:
    #         case 1:
    #             room.show_details()
            
    #         case 2:
    #             guest.book_room(room)
            
    #         case 3: 
    #             guest.check_in()
            
    #         case 4:
    #             guest.check_out()
            
    #         case 5:
    #             print("See you next time!👋")
    #             break

    #         case _:
    #             print("Invalid option")
    #             continue

if __name__ == "__main__":
    main()