#!/usr/env/python

fruits = ["Apples", "Pears", "Oranges", "Peaches"]
print fruits

fruits.append(raw_input("What fruit would you like to add to the list? > "))
print fruits

#Ask user for number, return number and fruit at coresponding index
add_fruit = int(raw_input("Please enter a number. > "))
print "You entered: %i, %s" % (add_fruit, fruits[add_fruit-1])

#Add another fruit to beginning of list using +, then print list
fruits = fruits + raw_input("Please enter a fruit to add to the list. > ")
print fruits

#Add another fruit to the beginning of the list using insert(), then print list
fruits.insert(0, raw_input("Please enter a fruit to add to the list. > "))
print fruits

#Display all fruits that begin with P using a for loop
for fruit in fruits:
    pass


#Using list above:

#Display list

#Remove last fruit from list

#Display new list

#Ask user for a fruit to delete

#Bonus: Multiply list times two, Keep asking until match is found. Once found, delete all occurances



#Ask user input displaying line like "Do you like apples?"

#For each fruit in the list, make all lowercase

#For each "no", delete that fruit from list

#For any answer other than yes or no, prompt user to answer with yes or no (while loop here)

#Display the list



#Copy the list and reverse the letters in each fruit in the copy

#Delete the last item from the original list. Display the original list and copy.
