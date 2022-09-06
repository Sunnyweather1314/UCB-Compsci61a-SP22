#List

def trade(first, second):
    """Exchange the smallest prefixes of first and second that have equal sum.
    >>> a = [1, 1, 3, 2, 1, 1, 4]
    >>> b = [4, 3, 2, 7]
    >>> trade(a, b) # Trades 1+1+3+2=7 for 4+3=7
    'Deal!'
    >>> a
    [4, 3, 1, 1, 4]
    >>> b
    [1, 1, 3, 2, 2, 7]
    >>> c = [3, 3, 2, 4, 1]
    >>> trade(b, c)
    'No deal!'
    >>> b
    [1, 1, 3, 2, 2, 7]
    >>> c
    [3, 3, 2, 4, 1]
    >>> trade(a, c)
    'Deal!'
    >>> a
    [3, 3, 2, 1, 4]
    >>> b
    [1, 1, 3, 2, 2, 7]
    >>> c
    [4, 3, 1, 4, 1]
    """
    m, n = 1, 1

    "*** YOUR CODE HERE ***"
# Sol 1, better one

    deal = False
    while not deal and m <= len(first) and n <= len(second):
        if sum(first[:m]) == sum(second[:n]):
            deal = True
        elif sum(first[:m]) < sum(second[:n]):
            m += 1
        elif sum(first[:m]) > sum(second[:n]):
            n += 1
    if deal:
        first[:m], second[:n] = second[:n], first[:m]
        return 'Deal!'
    else:
        return 'No deal!'



# Sol 2

    m, n = 1, 1
    while m <= len(first):
        n = 1  # make sure the second list counts from the first element
        while n <= len(second):
            if sum(first[:m]) == sum(second[:n]):
                first[:m], second[:n] = second[:n], first[:m]
                return 'Deal!'
            n += 1
        m += 1
    else:
        return 'No deal!'
