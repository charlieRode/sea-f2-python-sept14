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
