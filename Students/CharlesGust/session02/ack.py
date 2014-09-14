def Ackermann(m, n):
    """return Ackermann function for demonstrating exponential recursive"""
    if (m < 0) or (n < 0):
        return None
    if m == 0:
        return n+1
    if n == 0:
        return Ackermann(m-1, 1)
    return Ackermann(m-1, Ackermann(m, n-1))

if __name__ == "__main__":
    for m in xrange(0, 4):
        for n in xrange(0, 5):
            print "Ackermann(", m, ",", n, ") = ", Ackermann(m, n)
