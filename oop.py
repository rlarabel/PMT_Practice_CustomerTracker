class Ticket:
    def __init__(self, name, grade, cost_of_tickets):
        self.__name = name
        self.__grade = grade
        self.__cost_of_tickets = cost_of_tickets

    # Return this customer's name.
    def get_name(self):
        return self.__name

    # Return the grade for this ticket ('f' for "family", 's' for "single", 'c' for "group").
    def get_grade(self):
        return self.__grade

    # Calculate and return the cost of this ticket.
    def get_cost_of_ticket(self):
        return int(self.__cost_of_tickets)


class Exclusive(Ticket):
    def __init__(self, name, grade):
        if grade == 's':
            cost_of_tickets = 10000
        elif grade == 'c':
            cost_of_tickets = 12000
        elif grade == 'f':
            cost_of_tickets = 13000
        else:
            cost_of_tickets = 9999999

        Ticket.__init__(self, name, grade, cost_of_tickets)


class PremiumPlus(Ticket):
    def __init__(self, name, grade):
        if grade == 's':
            cost_of_tickets = 6000
        elif grade == 'f':
            cost_of_tickets = 9500
        elif grade == 'c':
            cost_of_tickets = 8500
        else:
            cost_of_tickets = 9999999

        Ticket.__init__(self, name, grade, cost_of_tickets)


class EconomyComfort(Ticket):
    def __init__(self, name, grade, num_of_tickets):
        cost_of_tickets = 1200 * num_of_tickets
        Ticket.__init__(self, name, grade, cost_of_tickets)


class Customer:
    def __init__(self, name, ticket=None):
        self.__name = name
        self.__total_cost_of_tickets = 0
        if ticket is None:
            self.__ticket = []
        else:
            self.__ticket = ticket

    # Return the name of this customer
    def get_name(self):
        return self.__name

    # Return a list of tickets for this customer
    def get_tickets(self):
        return self.__ticket

    # Add a ticket object to the list of tickets for this customer
    def add_ticket(self, ticket):
        self.__ticket.append(ticket)
    # Determine and return the total cost of all the tickets bought by this customer

    def get_total_cost_of_tickets(self):
        self.__total_cost_of_tickets = 0
        tickets = self.__ticket
        for ticket in tickets:
            self.__total_cost_of_tickets += ticket.get_cost_of_ticket()

        return self.__total_cost_of_tickets
