def fibonacci(n):
    """Returns the nth number in the Fibonacci sequence (starting at 0, F_0 = 0, F_1 = 1)"""
    if n < 0:
        return None #bad input, throw error maybe
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)





if __name__ == '__main__':
    assert fibonacci(0) == 0
    assert fibonacci(1) == 1
    assert fibonacci(2) == 1
    assert fibonacci(3) == 2
    assert fibonacci(4) == 3
    assert fibonacci(5) == 5
    assert fibonacci(6) == 8
    assert fibonacci(7) == 13

    print "All Tests Pass"
