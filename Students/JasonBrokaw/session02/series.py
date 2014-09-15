def fibonacci(n):
    """Returns the nth number in the Fibonacci sequence (starting at 0, F_0 = 0, F_1 = 1)"""
    if n < 0:
        return None #bad input, throw error maybe
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)

def lucas(n):
    """Returns the nth number in the Lucas sequence (starting at 0, L_0 = 2, L_1 = 1)"""
    if n < 0:
        return None #bad input, throw error maybe
    if n == 0:
        return 2
    if n == 1:
        return 1
    return lucas(n - 1) + lucas(n - 2)



if __name__ == '__main__':
    assert fibonacci(0) == 0
    assert fibonacci(1) == 1
    assert fibonacci(2) == 1
    assert fibonacci(3) == 2
    assert fibonacci(4) == 3
    assert fibonacci(5) == 5
    assert fibonacci(6) == 8
    assert fibonacci(7) == 13

    assert lucas(0) == 2
    assert lucas(1) == 1
    assert lucas(2) == 3
    assert lucas(3) == 4
    assert lucas(4) == 7
    assert lucas(5) == 11
    assert lucas(6) == 18
    assert lucas(7) == 29
    assert lucas(8) == 47
    assert lucas(9) == 76
    assert lucas(10) == 123
    assert lucas(11) == 199
    assert lucas(12) == 322
    assert lucas(13) == 521
    assert lucas(14) == 843

    print "All Tests Pass"
