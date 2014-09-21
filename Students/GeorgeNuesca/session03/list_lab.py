#!/usr/bin/env python2.7

# PART 1
fruitlist1 = ["Apples","Pears","Orange","Peaches"]
print fruitlist1

# Add a fruit to the end of the list.
addfruit1 = raw_input('Please add another fruit to the list: ')
fruitlist1.append(addfruit1)
print fruitlist1

# Locate fruit from index.
locfruit = int(raw_input('Please enter a number: '))
print fruitlist1[locfruit - 1]

# Converts user input to list, then adds it to the beginning of list.
addfruit2 = [raw_input('Please add a second fruit to the list: ')]
fruitlist1 = addfruit2 + fruitlist1
print fruitlist1

# Inserts user input at index 0 to list.
addfruit3 = raw_input('Please add a third fruit to the list: ')
fruitlist1.insert(0, addfruit3)
print fruitlist1

# Looks for fruits starting with p and prints them.
for i in range(len(fruitlist1)):  #####for fruit in fruitlist: #####usually don't want to do something with index, usually objects
    startP = fruitlist1[i]
    if startP[0] in ['p', 'P']:  #Evaluates first letter in pP list.
        print fruitlist1[i]

fruitlist1 = tuple(fruitlist1)  # Convert fruitlist1 to immutable tuple to avoid changes.


# PART2
fruitlist2 = list(fruitlist1)
##### Does converting to a list do anything in this case? Needs to be a list to change - mutable?
print fruitlist2
fruitlist2.pop()  # Default argument removes last element from list (can put alternative value).
print fruitlist2
fruitremoval = raw_input('Specify a fruit to remove from the list: ')
fruitlist2.remove(fruitremoval)  # Removes specified string from list.
print fruitlist2


# PART3
fruitlist3 = list(fruitlist1)
print fruitlist3
for i, fruit in enumerate(fruitlist2):# in range(len(fruitlist3)):  # Converts everything in the list to lower case.
    fruitlist3[i] = fruit.lower()
    #makelower = fruitlist3[i]  #####Use enumerate
    #fruitlist3[i] = makelower.lower()

# Asks if the user likes an item and removes it if they don't.
for fruit in fruitlist3[:]:  # "item" is the element starting from index 0 (not index number).
    response = raw_input('Do you like %s? (yes or no)' % item)
    ##### How do you avoid case sensitivity for boolean operation? (.lower).
    while (not response) in ['yes', ' no']:
        if response == 'yes' or response == 'no':
            break
        response = raw_input('Type yes or no: ')
    if response == 'no':
        fruitlist3.remove(item)
print fruitlist3


#PART4
# Assigns a string at index i to an object, then reverses the object.
fruitlist4 = list(fruitlist1)
for fruit in fruitlist4:
    print fruitlist4[i]
    letterreverse = fruitlist4[i]  #Can you put the slice in here
    # Slices the entire object and returns items in reverse starting at the last item.
    fruitlist4[i] = letterreverse[::-1]
fruitlist4.pop()
print fruitlist1
print fruitlist4