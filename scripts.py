
#Count partitions

def count_partition1(m,n):
    if m == 0:
        return 1
    elif m < 0:
        return 0
    elif n == 0:
        return 0
    else:
        return count_partition1(m-n,n)+count_partition1(m,n-1)

def count_partition2(m,n):
    if m < 0 or n == 0:
        return 0
    else:
        exact_match = 0
        if n == m:
            exact_match = 1
        return exact_match + count_partition2(m-n,n) + count_partition2(m,n-1)

def count_partition3(m,n):
    if m > 0 and n > 0:
        if m == n:
            yield str(n)
        for p in count_partition3(m-n,n):
            yield p + "+" + str(n)
        yield from count_partition3(m,n-1)