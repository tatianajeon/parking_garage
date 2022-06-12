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

    def __init__(self,tickets,parkingSpaces,currentTicket):
        self.tickets = tickets # tickets available, correlates with parkingSpaces.
        self.parkingSpaces = parkingSpaces # paid/unpaid
        self.currentTicket = currentTicket # keys: tickets,

        self.tickets = [1,2,3,4,5]
        self.parkingSpaces = 5
        self.currentTicket = {1:'',2:'',3:'',4:'',5:''}    
    

    def takeTicket(self): # take a ticket and add to currentTicket, take out from tickets and parkingSpaces
        if self.parkingSpaces <= 0:
            print("This parking garage is full!")
        else:
            print(f"There is {self.parkingSpaces} parking spaces available")
            print(f"These are the availiable tickets:{self.tickets}")
            tix_choice = input("Choose a ticket number") 
            tix = self.tickets.remove(int(tix_choice))
            self.parkingSpaces -= 1
            print(f"Now there is only {self.parkingSpaces} parking spaces available")
            print(f"Now these are the available tickets: {self.tickets}")
            # print(f"Please take ticket: {tix}")
            # self.currentTicket[tix] = False 
            # print(f"Parking spots taken: {self.currentTicket}")
            # self.parkingSpaces.remove(tix)
            # print(f"Parking spaces available: {self.parkingSpaces}")




    def payForParking(self):  # check if ticket was paid, provide option to pay
        # print(f"Here is the parking Tickets: {self.currentTicket}")
        print(f"Here is the tickets you can pay for: {self.currentTicket.keys()}")
        select_ticket = (int(input("Which Ticket number do you want to Pay for? ")))       
        if self.currentTicket[select_ticket] == "":
            print(f"Your ticket: {self.currentTicket[select_ticket]} is not paid. ")
            pay_tix = input("Type pay to pay for your Ticket")
            paid_tix = pay_tix.lower()
            self.currentTicket[select_ticket] = 'paid'
            if self.currentTicket[select_ticket] != 'paid':
                print("You haven't paid for your ticket")

            else:
                 self.currentTicket[select_ticket] == 'paid'
                #  self.tickets.append(select_ticket)
                #  self.parkingSpaces.append(select_ticket)
                 print(f"Your ticket:{self.currentTicket[select_ticket]} is now paid and you have 15 mins to leave")
                 print(f"{self.currentTicket}") 
        



    def leaveGarage(self):  # check if ticket is paid and leave garage
        check_tix = int(input("What is your ticket number?"))
        if self.currentTicket[check_tix] != 'paid':
            print("You need to pay for your ticket")
            pay_tixx = input("Type pay to pay for your Ticket")
            paid_tix = pay_tixx.lower()
            self.currentTicket[check_tix] = 'paid'
            print(f"Your ticket:{self.currentTicket[check_tix]} is now paid")
            print("Your Ticket is paid.Thank You, have a nice day")
            self.parkingSpaces += 1
            print(f"Now there is {self.parkingSpaces} available parking spots now")
            update_tix = self.tickets.append(check_tix)
            self.tickets.sort()
            print(f"These are the available tickets now:{self.tickets}")
        else:
            print("Your Ticket is paid.Thank You, have a nice day")
            self.parkingSpaces += 1
            print(f"Now there is {self.parkingSpaces} available parking spots now")
            update_tix = self.tickets.append(check_tix)
            self.tickets.sort()
            print(f"These are the available tickets now:{self.tickets}")

            
            
            




        
        




    def run(self):
        while True:
            print("""

            Welcome to the parking garage. 
            What would you like to do?
            [1] park
            [2] pay
            [3] leave
            [4] quit
                
            """)

            response = int(input("Choose your option"))
            if response == 1:
                self.takeTicket()
            elif response == 2:
                self.payForParking()
            elif response == 3:
                self.leaveGarage()
            elif response == 4:
                break

            else:
                print("That is not a valid option: please choose 1, 2,3, or 4")
            

            

user = Garage(1,1,1)

Garage.run(user)