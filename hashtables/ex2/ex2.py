#  Hint:  You may not need all of these.  Remove the unused functions.
class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


def reconstruct_trip(tickets, length):
    """
    YOUR CODE HERE
    """
    route = []
    flight_ht = {}

    # add all tickets to a hash table
    for x in range(length):
        flight_ht[tickets[x].source] = tickets[x].destination
    
    # Append seed location
    route.append(flight_ht.get("NONE"))
    
    # Append the next location using the seed entry in route
    for x in range(length-1):
        route.append(flight_ht.get(route[x]))

    return route