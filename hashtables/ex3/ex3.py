
def intersection(arrays):
    """
    YOUR CODE HERE
    """
    ht = {}
    results = []

    # Add all array elements at first index to hash table to compare
    for x in range(len(arrays[0])):
        ht[arrays[0][x]] = x
    
    # Check to see if the keys exist in the next list and if it does append value to results
    for x in range(1, len(arrays)):

        # Compare 1st list to second list and append intersection values to results
        if x == 1:
            for y in range(len(arrays[x])):
                val = arrays[x][y]
                if ht.get(val) != None:
                    if val not in results:
                        results.append(val)
            
            # If results dont exist in other lists then remove the value
            else:
                for z in range(len(results)):
                    if results[z] not in arrays[x]:
                        del results[z]
                    else:
                        continue
            
    return results


if __name__ == "__main__":
    arrays = []

    arrays.append(list(range(1000000, 2000000)) + [1, 2, 3])
    arrays.append(list(range(2000000, 3000000)) + [1, 2, 3])
    arrays.append(list(range(3000000, 4000000)) + [1, 2, 3])

    print(intersection(arrays))