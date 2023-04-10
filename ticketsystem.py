ticket_list = []
used_ID = []
solve = 0
resolved = 0

class Ticket:
    counter = 1

    
    def __init__(self, staffID, creatorName, contactEmail, description, ticketStatus):
        global solve
        global resolved
        global used_ID
        self.staffID = staffID

        self.creatorName = creatorName 

        self.contactEmail = contactEmail

        self.description = description

        self.listingNum = Ticket.counter + 2000

        Ticket.counter += 1

        self.response = "Not Yet Provided"

        self.ticketStatus = ticketStatus
        
        if self.ticketStatus == "Open":
            solve += 1

        elif self.ticketStatus == "Closed":
            resolved += 1

        used_ID.append(self.listingNum)

    def password_change(self):
        global solve
        global resolved
        if "Password Change" in self.description:
            changedpwp1 = self.staffID[0:2]
            changedpwp2 = self.creatorName[0:3]
            changedpw = changedpwp1 + changedpwp2
            self.ticketStatus = "Closed"
            resolved += 1
            solve -= 1
            self.response = ("New Password is:", changedpw)
            print("New password in response")
        else:
            pass

    def ticketprint(self):
        global ticket_list
        print("---------------")
        print("Ticket Number:",self.listingNum)
        print("Creator Name:",self.creatorName)
        print("Staff ID:", self.staffID)
        print("Contact Email:",self.contactEmail)
        print("Description:",self.description)
        print("Response:",self.response)
        print("Status:",self.ticketStatus) 

ticket1 = Ticket("INNAM","Inna","inna@whitecliffe.co.nz","My monitor stopped working.", "Closed")
ticket_list.append(ticket1)


ticket2 = Ticket("MARIAH","Maria","maria@whitecliffe.co.nz","Request for a videocamera to conduct webinars.", "Open")
ticket_list.append(ticket2)


ticket3 = Ticket("JOHNS","John","john@whitecliffe.co.nz", "Password Change", "Open")
ticket_list.append(ticket3)
Ticket.password_change(ticket3)

def view_tickets():
    print("---------------")
    for i in ticket_list:
        Ticket.ticketprint(i)
    main()


#for i in used_ID:
    #print(i)

#creating ticket

def create_new_ticket():
    print("---------------")
    userID = input("Please enter your Staff ID: ")
    name = input("Please enter your Name: ")
    email = input("Please enter your Email: ")
    description = input("Please Describe your Issue: ")
    ticket4 = Ticket(userID, name, email, description,"Open")
    ticket_list.append(ticket4)
    Ticket.ticketprint(ticket4)
    Ticket.password_change(ticket4)
    main()


def ticket_stats():
    global solve
    global resolved
    ticket_count = Ticket.counter - 1
    print("---------------")
    print("tickets to solve", solve)
    print("tickets resolved", resolved)
    print("tickets created", ticket_count)

def edit_ticket():
    global solve
    global resolved
    global ticket_list
    print("---------------")
    userinput = int (input("Enter Ticket Number")) 
    tid = userinput - 2001
    Ticket.ticketprint(ticket_list[tid])
    editing = input("would you like to (O)pen or (C)locse the ticket?") 
    if editing == "O":
        ticket_list[tid].ticketStatus = "Reopend"
        solve +=1
        resolved -=1 
    elif editing == "C":
        ticket_list[tid].ticketStatus = "Closed"
        solve -=1
        resolved +=1 
        user_response = input("Please enter a response")  
        ticket_list[tid].response = user_response
    Ticket.ticketprint(ticket_list[tid])
    main()
def main():
    ticket_stats()
    print("---------------")
    main_input = input("Would you like to (V)iew Tickets, (E)dit Tickets or (M)ake a new Ticket?")
    if main_input == "V":
        view_tickets()
    elif main_input == "M":
        create_new_ticket()
    elif main_input == "E":
        edit_ticket() 
        
main()       
