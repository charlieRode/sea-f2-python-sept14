def ack(m, n):
    """Compute Ackermann's Function from input values."""
    if m == 0:
        return n+1
        return n
    if m > 0  and  n == 0:
        return ack(m-1, 1)
    if m > 0  and  n > 0:
        return ack(m-1, ack(m, n-1))
