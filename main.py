from room import Room
from guest import Guest

def main():
    room = Room("101", "queen - beach view")
    guest = Guest("Matheus")

    print("Welcome to 🏨Buffer Suites🏨 - Here downtime becomes uptime")

    while True:
        print("\n====Menu====")
        print("1. View Room Status")
        print("2. Book Room")
        print("3. Check In")
        print("4. Check Out")
        print("5. Exit")

        print()
        choice = int(input("Select an option (1-5): "))
        print()

        match choice:
            case 1:
                room.show_details()
            
            case 2:
                guest.book_room(room)
            
            case 3: 
                guest.check_in()
            
            case 4:
                guest.check_out()
            
            case 5:
                print("See you next time!👋")
                break

            case _:
                print("Invalid option")
                continue

if __name__ == "__main__":
    main()