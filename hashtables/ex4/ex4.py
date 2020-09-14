
def has_negatives(a):
    """
    YOUR CODE HERE
    """
    ht = {}
    results = []

    # If absolute value of a[x] is not in ht then add it, otherwise append value to results
    for x in range(len(a)):
        if ht.get(abs(a[x])) == None:
            ht[abs(a[x])] = x
        else:
            results.append(abs(a[x]))
    
    return results


if __name__ == "__main__":
    print(has_negatives([-1, -2, 1, 2, 3, 4, -4]))