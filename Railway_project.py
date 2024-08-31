
import random
import datetime

class Train:
    def __init__(self, train_num, source, destination, seats):
        self.train_num = train_num
        self.source = source
        self.destination = destination
        self.seats = seats

    def display_details(self):
        print('Train number: {}'.format(self.train_num))
        print('Source: {}'.format(self.source))
        print('Destination: {}'.format(self.destination))
        print('Available seats: {}'.format(self.seats))

    def book_tickets(self, num_tickets):
        if num_tickets > self.seats:
            return None
        pnr_list = []
        for i in range(num_tickets):
            pnr_list.append(random.randint(1000000, 9999999))
        self.seats -= num_tickets
        return pnr_list
        

class Passenger:
    def __init__(self, name, age, gender, phone, address):
        self.name = name
        self.age = age
        self.gender = gender
        self.phone = phone
        self.address = address

    def display_details(self):
        print('Name: {}'.format(self.name))
        print('Age: {}'.format(self.age))
        print('Gender: {}'.format(self.gender))
        print('Phone Number: {}'.format(self.phone))
        print('Address: {}'.format(self.address))

class Ticket:
    def __init__(self, train, source, destination, passengers, pnr, amount, payment_method, payment_status):
        self.date = datetime.datetime.now().strftime("%d-%m-%Y %H:%M:%S")
        self.train = train
        self.source = source
        self.destination = destination
        self.passengers = passengers
        self.pnr = pnr
        self.amount = amount
        self.payment_method = payment_method
        self.payment_status = payment_status

    def display_details(self):
        print('Train Number: {}'.format(self.train.train_num))
        print('Source: {}'.format(self.source))
        print('Destination: {}'.format(self.destination))
        print('PNR: {}'.format(self.pnr))
        print('Date of Booking: {}'.format(self.date))
        print('Amount: {}'.format(self.amount))
        print('Payment Method: {}'.format(self.payment_method))
        print('Payment Status: {}'.format(self.payment_status))
        for passenger in self.passengers:
            passenger.display_details()
        print()

class Account:
    def __init__(self, username, password, Security):
        self.username = username
        self.password = password
        self.Security = Security

    def check_password(self, password, Security):
        return (self.password == password and
                self.Security == Security)
                

accounts = [
    Account("user1", "password1",  "FavoritePet"),
    Account("user2", "password2",  "FavoritePet")
]

logged_in_account = None
while True:
    print("\n1. Create an account\n2. Login\n")
    choice = input("Enter choice: ")
    if choice == "1":
        username = input("Enter username: ")
        password = input("Enter password: ")
        Security = input("Security Question: (What is your favorite pet's name?) ")
        accounts.append(Account(username, password, Security))
        print("Account created successfully!")

    elif choice == "2":
        username = input("Enter username: ")
        password = input("Enter password: ")
        Security = input("Security Question: (What is your favorite pet's name?)")
        for account in accounts:
            if (account.username == username and
                account.check_password(password, Security)):
                logged_in_account = account
                break
        if logged_in_account is None:
            print("Invalid username, password, or security answers.")
        else:
            print("Logged in as {}\n\n-----Available Train details-----".format(logged_in_account.username))
            break
    else:
        print("Invalid choice.")

if logged_in_account is not None:
    trains = [
        Train("18520", "Bhimavaram", "Visakhapatnam",20),
        Train("17209", "Bhimavaram", "Samalkot", 15),
        Train("17479", "Rajahmundry", "Tirupati",40),
        Train("12728", "Tadepalligudem", "Visakhapatnam", 30),
        Train("22863", "Vijayawada", "Bangalore", 5),
    ]

    for train in trains:
        train.display_details()

    while True:
        try:
            train_num = input("Enter Train Number: ")
            num_tickets = int(input("Enter Number of Tickets: "))
            if num_tickets <= 0:
                raise ValueError("Number of tickets should be greater than 0")
            for train in trains:
                if train.train_num == train_num:
                    if num_tickets > train.seats:
                        raise ValueError("Selected more tickets than available seats")
                    break
            else:
                raise ValueError("Invalid Train Number.")
            break
        except ValueError as e:
            print("Invalid Input: {}".format(e))

    train = None
    for t in trains:
        if t.train_num == train_num:
            train = t
            break

    if train is None:
        print("Invalid Train Number.")
    else:
        passengers = []
        for i in range(num_tickets):
            print("Enter details for Passenger {}".format(i + 1))
            while True:
                try:
                    name = input("Name: ")
                    if not name:
                        raise ValueError("Name cannot be empty")
                    age = int(input("Age: "))
                    if age <= 0 or age > 120:
                        raise ValueError("Invalid Age")
                    gender = input("Gender: ")
                    phone = input("Phone Number: ")
                    if not phone or len(phone) != 10 or not phone.isdigit():
                        raise ValueError("Invalid Phone Number")
                    address = input("Address: ")
                    passenger = Passenger(name, age, gender, phone, address)
                    passengers.append(passenger)
                    break
                except ValueError as e:
                    print("Invalid Input: {}".format(e))

        pnr_list = train.book_tickets(num_tickets)
        if pnr_list is None:
            print("Tickets not available.")
        else:
            amount = num_tickets * 100  
            print("Available Payment Methods: ")
            print("1. Credit Card")
            print("2. Debit Card")
            print("3. Net Banking")
            payment_choice = input("Select Payment Method (1 or 2 or 3): ")
            payment_methods = {
                "1": "Credit Card",
                "2": "Debit Card",
                "3": "Net Banking"
            }
            if payment_choice in payment_methods:
                payment_method = payment_methods[payment_choice]
                payment_status = "Paid"
            else:
                print("Invalid Payment Method selected")
                payment_method = "Unknown"
                payment_status = "Pending"
            
            print("\n--------------Booking Successful!------------\n\nYour Ticket Details: \n")

            for i in range(num_tickets):
                ticket = Ticket(train, train.source, train.destination, [
                            passengers[i]], pnr_list[i], amount, payment_method,payment_status)
                ticket.display_details()
            print("\n--------Thank You------- \n------- Happy Journey------")
