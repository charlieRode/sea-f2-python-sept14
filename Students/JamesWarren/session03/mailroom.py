#!/usr/env/python

donor_list = [
    ("John Doner", [1000, 1500]),
    ("Mary Doner", [900, 1800, 2000]),
    ("Joe Smith", [100, 150, 175]),
    ("Bob Andrews", [250, 250]),
    ("Cindy Brown", [800, 900])
]

def thank_you(name):
    return """Dear %s,

    Thank you so much for your generous donation of $%i! Every dollar
    helps local families in need, and none of it would be possible without
    the generosity of loyal donors like you.

    Sincerely,
    Bob Smith""" % (donor, amount)

def report():
    pass

if __name__ == '__main__':
    menu = raw_input("Please select: (1) Send a thank you note; (2) Create a report > ")

    #SEND THANK YOU
    if menu == "1":
        
        user_inp = raw_input("Please enter donor's full name. > ")
        while user_inp == "list":
            print donor_list
            user_inp = raw_input("Please enter donor's full name. > ")
        if user_inp not in donor_list:
            donor_list.append(user_inp)
        

    #CREATE REPORT
    elif menu == "2":
        pass

