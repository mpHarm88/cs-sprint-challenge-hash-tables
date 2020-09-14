
# Your code here



def finder(files, queries):
    """
    YOUR CODE HERE
    """
    ht = {}
    results = []

    for x in range(len(files)):
        for y in range(len(files[x])):
            if files[x][-y] == "/":
                ht[files[x][-y+1:]] = files[x]
    
    for x in queries:
        if ht.get(x) != None:
            results.append(ht.get(x))

    return results


if __name__ == "__main__":
    files = [
        '/bin/foo',
        '/bin/bar',
        '/usr/bin/baz'
    ]
    queries = [
        "foo",
        "qux",
        "baz"
    ]
    print(finder(files, queries))