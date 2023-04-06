    self.listingNum = Ticket.counter + 2000

        Ticket.counter += 1

        self.response = "Not Yet Provided"

        self.ticketStatus = ticketStatus
        
        if self.ticketStatus == "Open":
            solve += 1

        elif self.ticketStatus == "Closed":
            resolved += 1 

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

    def passwordchange(self):  
        if "Password Change" in (self.description):
            self.response = "New Password Generated: JoJoh"
            self.ticketStatus = "Closed"

ticket1 = Ticket("INNAM","Inna","inna@whitecliffe.co.nz","My monitor stopped working.", "Closed")
ticket_list.append(ticket1)
Ticket.ticketprint(ticket1)

ticket2 = Ticket("MARIAH","Maria","maria@whitecliffe.co.nz","Request for a videocamera to conduct webinars.", "Open")
ticket_list.append(ticket2)
print(ticket2.response)
Ticket.ticketprint(ticket2)

ticket3 = Ticket("JOHNS","John","john@whitecliffe.co.nz", "Password Change", "Closed")
Ticket.passwordchange(ticket3)
ticket_list.append(ticket3)
Ticket.ticketprint(ticket3)

#creating ticket

def create_new_ticket(): 
    userID = input("Please enter your Staff ID: ")
    name = input("Please enter your Name: ")
    email = input("Please enter your Email: ")
    description = input("Please Describe your Issue: ")
    ticket4 = Ticket(userID, name, email, description,"Open")
    ticket_list.append(ticket4)
    Ticket.ticketprint(ticket4)


def ticket_stats():
    global solve
    global resolved
    print("tickets to solve", solve)
    print("tickets resolved", resolved)
    print("tickets created", Ticket.counter)
    
def edit_ticket()
    whatticket = input("please enter the number of the ticket you'd like to edit")
    editingattribute = input("what would you like to edit") 
               
    










#s = "JOHNS"
#first_two = s[:2]
#print(first_two)

#b = "John"
#first_three = b [:3]
#print(first_three) 

#txt = "JOHNS"
#print(txt.rsplit('H',))

#txt2 = "John"
#print(txt2.rsplit('n'))

#join = b.join(s)
#print(join)
