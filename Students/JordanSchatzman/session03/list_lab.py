#!/usr/bin/env python
import sys



def fruitfun():
    """Execute Series 1"""
    global Fruits
    Fruits = ["Apples", "Pears", "Oranges", "Peaches"]
    print Fruits
    newfruit1 = raw_input('Add New Fruit :')
    Fruits.append(newfruit1)
    print Fruits
    fruitnum = int(raw_input('Which Fruit do you Want?'))
    print Fruits[fruitnum-1]
    Fruits = ['Starfruit'] + Fruits
    Fruits.insert(0, 'Banana')
    print Fruits
    for i in range(len(Fruits)):
        if Fruits[i][0].upper() == 'P':
            print Fruits[i]
    return Fruits

def fruitfun2():
    """Execute Series 2"""
    Fruits2 = Fruits
    print "Begin Series 2" 
    print Fruits2
    Fruits2.pop()
    print Fruits
    removefruit = raw_input('Remove Fruit :')
    Fruits2.remove(removefruit)
    print Fruits2


def fruitfun3():
    """Execute Series 3"""
    Fruits3 = Fruits[:]
    print "Begin Series 3"
    for i in Fruits3 :
        likefruit = raw_input("Do you like %s? :"%i.lower())
        while likefruit != u"yes" and likefruit !=u"no" :
            print u"You must give a yes or no answer \n"
            likefruit = raw_input("Do you like %s? :"%i.lower())
        if likefruit == u"no" :
            Fruits3.remove(i)
    print Fruits3

    
def fruitfun4():
    """Execute Series 4"""
    Fruits4 = Fruits[:]
    print "Begin Series 4"
    for i in range(len(Fruits4)):
        Fruits4[i] = Fruits4[i][::-1]
    print Fruits4
    print Fruits
    


if __name__ == "__main__":
    fruitfun()
    fruitfun2()
    fruitfun3()
    fruitfun4()