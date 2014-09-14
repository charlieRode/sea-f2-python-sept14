def fibonacci(n):
    """Compute Fibonacci's number from input value."""
    if n == 1 or n == 2:
        return n - 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

if __name__ == "__main__":
    assert fibonacci(1) == 0
    assert fibonacci(5) == 3
    assert fibonacci(13) == 144
    print "All tests pass."