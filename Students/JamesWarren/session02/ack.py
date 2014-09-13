def ack(m, n):
    if m == 0: n+1
    if m > 0  and  n == 0: ack(m-1, 1)
    if m > 0  and  n > 0: ack(m-1, ack(m, n-1))
    print locals()