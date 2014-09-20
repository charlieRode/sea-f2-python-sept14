#PART 1
dict = {
    'name' : 'Chris',
    'city' : 'Seattle',
    'cake' : 'Chocolate'
}
print dict
del dict['cake']
print dict
dict['fruit'] = 'Mango'

print dict.keys()
print dict.values()

print 'cake' in dict
print 'Mango' in dict.values()

#PART 2
d = {}
d1 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
d2 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 'A', 'B', 'C', 'D', 'E', 'F']
for k, v in zip(d1, d2):
    d[k] = v