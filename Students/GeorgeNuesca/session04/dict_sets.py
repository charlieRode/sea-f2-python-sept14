

# Part 1
dessert = {u'name' : u'Chris', u'city' : u'Seattle', u'Cake' : u'chocolate'}
print dessert

dessert.pop(u'Cake', None)
print dessert

dessert[u'fruit'] = u'Mango'
print dessert

print dessert.keys()
print dessert.values()

print u'cake' in dessert.keys()
print u'Mango' in dessert.values()

# Part 2: Zipping making a dictionary from two lists.
numbers = range(0, 16)
hexades = range(0, 16)
for i, hexade in enumerate(hexades):
    hexades[i] = hex(hexade)
numhexs = dict(zip(numbers, hexades))
print numhexs

# Part 3: Counting a specific item in values of a key
for key in dessert:
    dessert[key] = dessert[key].count(u'a')
print dessert

# Part 4
s2 = list(range(0,20))
for s in s2[:]:
    if s % 2 == 0:
        continue
    else:
        s2.remove(s)
s2 = set(s2)


s3 = list(range(0,20))
for s in s3[:]:
    if s % 3 == 0:
        continue
    else:
        s3.remove(s)
s3 = set(s3)


s4 = list(range(0,20))
for s in s4[:]:
    if s % 4 == 0:
        continue
    else:
        s4.remove(s)
s4 = set(s4)

print s2
print s3
print s4

print 'Is s3 a subset of s2: ', s3.issubset(s2)
print 'Is s4 a subset of s2: ', s4.issubset(s2)