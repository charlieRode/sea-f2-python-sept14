def fibonacci(n):
    """Compute Fibonacci's number from input value."""
    if n == 1 or n == 2:
        return n - 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)
