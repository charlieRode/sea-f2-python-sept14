def series(n, seed1=0, seed2=1):
    """ return the nTH number of a series seeded with seed1 and seed2 """
    if n <= 2:
        if n == 1:
            return seed1
        elif n == 2:
            return seed2
        else:
            return None
    return series(n-1, seed1, seed2)+series(n-2, seed1, seed2)


def lucas(n):
    """ return the nTH Lucas number """
    return series(n, 2, 1)


def fibonacci(n):
    """ return the nTH Fibonacci number """
    return series(n)
