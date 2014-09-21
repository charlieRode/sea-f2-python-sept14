#!/usr/local/bin/python

fruits = [u"Apples", u"Pears", u"Oranges", u"Peaches"]

print fruits

new_fruit = raw_input(u"Type a fruit: ")

fruits.append(new_fruit)

print fruits

index = int(raw_input(u"Type an index from 1 through %i: " % len(fruits)))

print "The %ith item in the list is %s" % (index, fruits[index - 1])

fruits = [u"Cantaloupe"] + fruits

print fruits

fruits.insert(0, u"Banana")

print fruits

for fruit in fruits:
    if fruit[0] == "P":
        print fruit
