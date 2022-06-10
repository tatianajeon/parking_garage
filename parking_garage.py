# this is tatiana

# Your parking gargage class should have the following methods:

# - tickets -> list
# - parkingSpaces -> list
# - currentTicket -> dictionary

# - takeTicket
# - This should decrease the amount of tickets available by 1
# - This should decrease the amount of parkingSpaces available by 1

# - payForParking
# - Display an input that waits for an amount from the user and store it in a variable
# - If the payment variable is not empty then (meaning the ticket has been paid) -> display a message to the user that their ticket has been paid and they have 15mins to leave
# - This should update the "currentTicket" dictionary key "paid" to True

# -leaveGarage
# - If the ticket has been paid, display a message of "Thank You, have a nice day"
# - If the ticket has not been paid, display an input prompt for payment
# - Once paid, display message "Thank you, have a nice day!"
# - Update parkingSpaces list to increase by 1 (meaning add to the parkingSpaces list)
# - Update tickets list to increase by 1 (meaning add to the tickets list)


class Garage():

    def __init__(self):
        self.tickets = [] # tickets available, correlates with parkingSpaces.
        self.parkingSpaces = [] # paid/unpaid
        self.currentTicket = {} # keys: tickets,
    
    

    def takeTicket(self): # take a ticket and add to currentTicket, take out from tickets and parkingSpaces
        if self.tickets <= 0:
            print("This parking garage is full!")
        else:
            tix = self.tickets.remove[0]
            print(f"Please take ticket: {tix}")
            self.currentTicket[tix] = False 
            print(f"Parking spots taken: {self.currentTicket}")
            self.parkingSpaces.remove(tix)
            print(f"Parking spaces available: {self.parkingSpaces}")




    def payForParking(self):  # check if ticket was paid, provide option to pay
        print(f"Here is the parking Tickets: {self.currentTicket.keys()}")
        select_ticket = int(input("Which Ticket number do you want to Pay for? "))
        if self.currentTicket(select_ticket) == False:
            print(f"Your ticket: {self.currentTicket.keys(select_ticket)} is not paid. ")
            pay_tix = input("Type pay to pay for your Ticket")
            paid_tix = pay_tix.lower()
            if paid_tix != 'pay':
                print("You haven't paid for your ticket, type pay to pay for your ticket")

            else:
                 self.currentTicket(select_ticket) == True
                 self.tickets.append(select_ticket)
                 self.parkingSpaces.append(select_ticket)
                 print(f"Your ticket:{self.currentTicket(select_ticket)} is now paid")
                 print(f"{self.currentTicket}") 
        



    def leaveGarage(self):  # check if ticket is paid and leave garage
        
        




    def run(self)
    while True:
        print("""
        
        Welcome to the parking garage. 
        What would you like to do?
        [1] park
        [2] pay
        [3] leave
         
        """)

        response = int(input("Choose your option"))
        if response == '1':
            self.takeTicket()
        elif response == '2':
            self.payForParking()
        elif response == '3':
            self.leaveGarage()

        else: 
            print("That is not a valid option: please choose 1, 2, or 3")

