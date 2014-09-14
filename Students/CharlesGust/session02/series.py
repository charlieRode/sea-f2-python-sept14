def series(n, seed1=0, seed2=1):
    if n <= 2:
        if n == 1:
            return seed1
        elif n == 2:
            return seed2
        else:
            return None
    return series(n-1, seed1, seed2)+series(n-2, seed1, seed2)


def lucas(n):
    return series(n, 2, 1)


def fibonacci(n):
    return series(n)
