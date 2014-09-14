def fibonacci(n):
    """Compute Fibonacci's number from input value."""
    #0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89...
    if n == 1 or n == 2:
        return n - 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

def lucas(nth):
    """Compute Lucas's number from input value."""
    #2, 1, 3, 4, 7, 11, 18, 29, 47, 76...
    if nth == 1:
        return nth + 1
    if nth == 2:
        return nth - 1
    else:
        return lucas(nth - 1) + lucas(nth - 2)

def sum_series(x, fib1=0, fib2=1):
    """Compute value (X,y,z) in sum series with designated starting numbers (x,Y,Z)."""
    ###FIX ME
    if x == 1: return fib1
    elif x == 2: return fib2
    ###
    else:
        return sum_series(x - 1) + sum_series(x - 2)


if __name__ == "__main__":
    #Tests Fibonacci function to ensure accuracy in computations
    assert fibonacci(1) == 0
    assert fibonacci(5) == 3
    assert fibonacci(13) == 144
    #Tests Lucas function to ensure accuracy in computations
    assert lucas(1) == 2
    assert lucas(5) == 7
    assert lucas(11) == 123
    print "All tests pass."