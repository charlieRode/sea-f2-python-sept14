alist = ["Apples", "Pears", "Oranges", "Peaches"]
print alist
another_fruit = raw_input("What's another fruit?-->")
alist.append(another_fruit)
print alist
anumber = raw_input("What's a number?-->")
if anumber > 0 and anumber < len(alist):
    print alist[anumber-1]
alist = ["Tomato"] + alist
print alist
alist.insert(0, "Avocado")
print alist
for i in alist:
    if i[0] == "P":
        print i
