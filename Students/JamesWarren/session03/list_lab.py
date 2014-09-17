#!/usr/env/python

fruits = ["Apples", "Pears", "Oranges", "Peaches"]
print fruits

fruits.append(raw_input("What fruit would you like to add to the list? > "))
print fruits

#Ask user for number, return number and fruit at coresponding index
add_fruit = int(raw_input("Please enter a number. > "))
print "You entered: %i, %s" % (add_fruit, fruits[add_fruit-1])

#Add another fruit to beginning of list using +, then print list
add_fruit = [raw_input("Please enter a fruit to add to the list. > ")]
fruits = fruits + add_fruit
print fruits

#Add another fruit to the beginning of the list using insert(), then print list
fruits.insert(0, raw_input("Please enter a fruit to add to the list. > "))
print fruits

#Display all fruits that begin with P using a for loop
for fruit in fruits:
    if fruit[0] == "P":
        print fruit


#Using list above:

#Display list
print fruits

#Remove last fruit from list
print "I don't like %s." % fruits.pop(-1)

#Display new list
print fruits

#Ask user for a fruit to delete
fruits.remove(raw_input("What fruit would you like to remove? > "))
print fruits

#Bonus: Multiply list times two, Keep asking until match is found. Once found, delete all occurances
#fruits = fruits * 2
#while True:
#    break
#print fruits


#Ask user input displaying line like "Do you like apples?"
user_inp = raw_input("Do you like %s? > " % fruits[-1])

#For each fruit in the list, make all lowercase
for fruit in range(len(fruits)):
    fruits[fruit] = fruits[fruit].lower()

#For any answer other than yes or no, prompt user to answer with yes or no (while loop here)
while user_inp.lower() != "no" and user_inp.lower() != "yes":
    print "%s is an invalid answer." % user_inp
    user_inp = raw_input("Do you like %s? > " % fruits[-1])

#For "no", delete that fruit from list
if user_inp.lower() == "no":
    fruits.pop(-1)
elif user_inp.lower() == "yes":
    pass


#Display the list
print fruits
#Copy the list and reverse the letters in each fruit in the copy
fruits_copy = fruits[:]

#Delete the last item from the original list. Display the original list and copy.
