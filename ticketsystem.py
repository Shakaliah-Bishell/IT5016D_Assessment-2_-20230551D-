ticket_list = []
class Ticket:
    counter = 1

    def __init__(self, staffID, creatorName, contactEmail, description):

        self.staffID = staffID

        self.creatorName = creatorName 

        self.contactEmail = contactEmail

        self.description = description

        self.listingNum = Ticket.counter + 2000

        Ticket.counter += 1

        self.response = "Not Yet Provided"

        self.ticketStatus = "Active"

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
            print("Response:New password generated: JOJoh")
            print("Status:Closed")

ticket1 = Ticket("INNAM","Inna","inna@whitecliffe.co.nz","My monitor stopped working.")
ticket_list.append(ticket1)
Ticket.ticketprint(ticket1)

ticket2 = Ticket("MARIAH","Maria","maria@whitecliffe.co.nz","Request for a videocamera to conduct webinars.")
ticket_list.append(ticket2)
Ticket.ticketprint(ticket2)

ticket3 = Ticket("JOHNS","John","john@whitecliffe.co.nz", "Password Change")
ticket_list.append(ticket3)
Ticket.passwordchange(ticket3)
Ticket.ticketprint(ticket3)



s = "JOHNS"
first_two = s[:2]
print(first_two)
