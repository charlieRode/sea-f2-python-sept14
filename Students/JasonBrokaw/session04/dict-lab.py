biography = {u"name": u"Chris", u"city": u"Seattle", u"cake": u"Chocolate"}

print biography

biography.pop(u"cake")

print biography

biography.setdefault(u"fruit", u"Mango")

print biography

print biography.keys()

print biography.values()

print biography.has_key(u"cake")

print u"Mango" in biography.values()

# Part 2
decimals = range(16)
hexes = decimals[:]
for index, num in zip(decimals,hexes):
    hexes[index] = hex(num)

print dict(zip(decimals, hexes))

# Part 3
biography_acount = {}
for key in biography:
    biography_acount[key] = biography[key].count(u"a")

print biography, biography_acount

