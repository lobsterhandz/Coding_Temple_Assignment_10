hotel_rooms = {
    "101": {"status": "available", "customer": ""},
    "102": {"status": "booked", "customer": "John Doe"}
}

def book_room(room_id, customer_name):
    if room_id in hotel_rooms:
        if hotel_rooms[room_id]['status'] == 'available':
            hotel_rooms[room_id]['status'] = 'booked'
            hotel_rooms[room_id]['customer'] = customer_name
            print(f"Room {room_id} is now booked by {customer_name}.")
        else:
            print(f"Room {room_id} is not available for booking.")
    else:
        print(f"Room {room_id} does not exist.")

def checkout_room(room_id):
    if hotel_rooms[room_id]['status'] == 'booked':
        hotel_rooms[room_id]['status'] = 'available'
        hotel_rooms[room_id]['customer'] = ""
        print(f"Room {room_id} is now available.")
    else:
        print(f"Room {room_id} is already available.")

def display_room_status():
    print("Hotel Room Status:")
    for room_id, details in hotel_rooms.items():
        customer = details['customer'] if details['customer'] else "None"
        print(f"Room {room_id} - Status: {details['status']}, Customer: {customer}")

def main():
    while True:
        print("\n1. Book a Room\n2. Checkout from a Room\n3. Display Room Status\n4. Quit")
        choice = input("Choose an action: ")
        if choice == '1':
            room_id = input("Enter room ID: ")
            customer_name = input("Enter customer name: ")
            book_room(room_id, customer_name)
        elif choice == '2':
            room_id = input("Enter room ID for checkout: ")
            checkout_room(room_id)
        elif choice == '3':
            display_room_status()
        elif choice == '4':
            print("Exiting the program.")
            break
        else:
            print("Invalid option, please choose again.")

if __name__ == '__main__':
    main()
