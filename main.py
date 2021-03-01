import oop


def main():
    jeweler = oop.Customer("Maggie May")
    # John Smith is going on the cruise with his family.
    cust1 = oop.Exclusive("John Smith", 'f')
    # Jane Jones is going on the cruise alone.
    cust2 = oop.PremiumPlus("Jane Jones", 's')
    # Ruth Sharp is going on the cruise with her spouse
    cust3 = oop.EconomyComfort("Ruth Sharp", 'c', 2)

    jeweler.add_ticket(cust1)
    jeweler.add_ticket(cust2)
    jeweler.add_ticket(cust3)

    print("Maggie's Jewelers List of Passengers")
    print("====================================\n")
    print("NOTE: 'c' -> couple; 'f' -> family; 's' -> single\n")

    tickets = jeweler.get_tickets()
    for ticket in tickets:
        print(f'{ticket.get_name():<17}{"("}{str(ticket.get_grade())}{")"}'
              f'{"   $"}{ticket.get_cost_of_ticket():>10,.2f}')
    print()
    print(f'{"Total cost of tickets: $"}{jeweler.get_total_cost_of_tickets():>10,.2f}')

    # Dempsey Dean is going on the cruise with her spouse
    cust4 = oop.Exclusive("Dempsey Dean", 'c')
    # John Smith is going on the cruise with his family of 5.
    cust5 = oop.EconomyComfort("Sophia Weather", 'f', 5)

    jeweler.add_ticket(cust4)
    jeweler.add_ticket(cust5)

    print()
    for ticket in tickets:
        print(
            f'{ticket.get_name():<17}{"("}{str(ticket.get_grade())}{")"}{"   $"}{ticket.get_cost_of_ticket():>10,.2f}')
    print()
    print(f'{"Total cost of tickets: $"}{jeweler.get_total_cost_of_tickets():>10,.2f}')


main()
