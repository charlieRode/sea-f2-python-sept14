def ack(m, n):
    """Return the value of the Ackerman function A(m,n)"""
    if m < 0 or n < 0:
        return None #Probably should throw a ValueError here too, but I don't know how
    if m == 0:
        return n + 1
    if m > 0 and n == 0:
        return ack(m - 1, 1)
    if m > 0 and n > 0:
        return ack(m - 1, ack(m, n - 1))

