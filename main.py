from src import Guest, Room, Staff, Hotel
from src.room import RoomStatus

def main():
    hotel = Hotel("Buffer Suites", "12345 Memory Bus, Motherboard PC, Brand Serial#")

    print(f"Welcome to 🏨 {hotel.name} 🏨 - Here downtime becomes uptime")

    # guest = Guest("Matheus Tizianel", "matheus9.mts@gmail.com")
    # cleaner = Staff("James Bond", "Cleaner", "cleaner@staff.com", "9999999999", "45 Palm St, Miami FL 12345 US")
    # receptionist = Staff("John", "Receptionist", "receptionist@staff.com")
    #
    # room = Room(101, "Queen - Ocean View")
    # hotel.add_room(room)
    # hotel.add_guest(guest)
    # reservation = hotel.create_reservation(guest, room)
    # reservation.check_in()
    # reservation.check_out()

    # IMPORTANTE:
    # Certifique-se de importar Reservation dentro do Hotel (já implementado)

    # Criar hotel
    hotel = Hotel("Blue Falcon", "Jacksonville")

    # Criar quartos
    room101 = Room(101, "deluxe")
    room102 = Room(102, "standard")

    # Adicionar quartos ao hotel
    hotel.add_room(room101)
    hotel.add_room(room102)

    # Criar hóspedes
    guest1 = Guest("Matheus", "matheus@email.com", "999-9999", "Rua A, 123")
    guest2 = Guest("Lucas", "lucas@email.com")

    # Adicionar hóspedes ao hotel
    hotel.add_guest(guest1)
    hotel.add_guest(guest2)

    print("\n=== TESTE 1: Criar reserva ===")
    reservation1 = hotel.create_reservation(guest1, room101)

    print("\n=== TESTE 2: Listar reservas ===")
    hotel.list_reservations()

    print("\n=== TESTE 3: Check-in ===")
    hotel.check_in(reservation1)

    print("\n=== TESTE 4: Check-out ===")
    hotel.check_out(reservation1)

    print("\n=== TESTE 5: Quarto deve estar em limpeza ===")
    print(room101)

    print("\n=== TESTE 6: Buscar reserva por hóspede ===")
    reservas_do_matheus = hotel.find_reservations_by_guest(guest1)
    print(reservas_do_matheus)

    print("\n=== TESTE 7: Listar hóspedes ===")
    hotel.list_guests()

    print("\n=== TESTE 8: Buscar quartos disponíveis por tipo ===")
    available_standard = hotel.find_available_rooms_by_type("standard")
    print("Standard Rooms: ", available_standard)

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