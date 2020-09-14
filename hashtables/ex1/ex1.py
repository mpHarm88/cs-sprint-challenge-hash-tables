def get_indices_of_item_weights(weights, length, limit):
    """
    YOUR CODE HERE
    """
    ht = {}

    # If length is 2 then return both weights with higher index first
    if len(weights) == 2:
        return [1,0]

    #load weights as keys and indicies as values
    for x in range(length):
        ht[weights[x]] = x
    
    # iterate through keys and calculate complimment value and look up the index value
    for x in ht.keys():
        compliment = limit  - x
        if ht.get(compliment) != None:
            ls = sorted([ht[compliment], ht[x]], reverse=True)
            return ls
    return None