#NameError################
#Mary is undefined, causing Name Error (to fix, turn Mary into string)
def names(name):
    if name == Mary:
        print "Hi Mary!"

names("Linda")


#TypeError################
#Cannot combine int and string, causing Type Error
def types(a, b):
    if a < b:
        return a + b

types(7, "Fred")


#SyntaxError###############
def syntax(n):
    pass

syntax()


#AttributeError#############
def attributes(k):
    pass

attributes()
