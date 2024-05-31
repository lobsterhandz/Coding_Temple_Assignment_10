# Initial service ticket structure
service_tickets = {
    "Ticket001": {"Customer": "Alice", "Issue": "Login problem", "Status": "open"},
    "Ticket002": {"Customer": "Bob", "Issue": "Payment issue", "Status": "closed"}
}

def open_ticket(ticket_id, customer_name, issue_description):
    service_tickets[ticket_id] = {"Customer": customer_name, "Issue": issue_description, "Status": "open"}
    print(f"Ticket {ticket_id} opened for {customer_name}.")

def update_ticket_status(ticket_id, new_status):
    if ticket_id in service_tickets:
        service_tickets[ticket_id]["Status"] = new_status
        print(f"Ticket {ticket_id} status updated to {new_status}.")
    else:
        print(f"Ticket {ticket_id} not found.")

def display_tickets(status_filter=None):
    for ticket_id, details in service_tickets.items():
        if status_filter is None or details["Status"] == status_filter:
            customer = details["Customer"]
            issue = details["Issue"]
            status = details["Status"]
            print(f"Ticket ID: {ticket_id}, Customer: {customer}, Issue: {issue}, Status: {status}")

def main():
    while True:
        print("\n1. Open a New Ticket\n2. Update Ticket Status\n3. Display Tickets\n4. Quit")
        choice = input("Choose an action: ")
        if choice == '1':
            ticket_id = input("Enter ticket ID: ")
            customer_name = input("Enter customer name: ")
            issue_description = input("Enter issue description: ")
            open_ticket(ticket_id, customer_name, issue_description)
        elif choice == '2':
            ticket_id = input("Enter ticket ID to update: ")
            new_status = input("Enter new status (open/closed): ")
            update_ticket_status(ticket_id, new_status)
        elif choice == '3':
            status_filter = input("Enter status to filter by (open/closed) or leave blank to show all: ")
            if status_filter == "":
                status_filter = None
            display_tickets(status_filter)
        elif choice == '4':
            print("Exiting the program.")
            break
        else:
            print("Invalid option, please choose again.")

if __name__ == '__main__':
    main()
