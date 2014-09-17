#!/usr/bin/env python

fruitlist = ["Apples","Pears","Orange","Peaches"]
print fruitlist

addfruit1 = raw_input('Please add another fruit to the list: ')
fruitlist.append(addfruit1)
print fruitlist

number = int(raw_input('Please enter a number: '))
print fruitlist[number - 1]

addfruit2 = [raw_input('Please add a second fruit to the list: ')]
print addfruit2 + fruitlist

addfruit3 = raw_input('Please add a third fruit to the list: ')
fruitlist.insert(0, addfruit3)
print fruitlist

for i in range(len(fruitlist)):
	startP = fruitlist[i]
	if startP[0] == 'p' or 'P':
		print fruitlist[i]

