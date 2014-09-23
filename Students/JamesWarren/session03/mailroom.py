#!/usr/bin/env python

donor_list = {
    "John Doner": [1500],
    "Mary Doner": [900, 1800, 2000],
    "Joe Smith": [100, 150, 175],
    "Bob Andrews": [250, 250],
    "Cindy Brown": [800]
}


def main_menu():
    print "Type Exit to quit."
    menu_select = raw_input("Please select: (1) Send a thank you note; \
(2) Create a report > ")
    
    #SEND THANK YOU
    if menu_select == "1":
        print "To return to the main menu at any point, type 'HOME'."
        user_inp = raw_input("Please enter donor's full name, or type \
'list' to see complete list of donors. > ")
        if user_inp == "HOME":
            main_menu()
        if user_inp == "list":
            for (key, value) in donor_list.items():
                print (key, value)
            user_inp = raw_input("Please enter donor's full name. > ")
        if user_inp not in donor_list:
            while True:
                donation = raw_input("Donation amount? > ")
                try:
                    donation = int(donation)
                    break
                except ValueError:
                    print "Please enter a valid number."
                    continue

            donor_list.setdefault(user_inp, []).append(donation)

        print thank_you(user_inp, donation)
        main_menu()


    #CREATE REPORT
    elif menu_select == "2":
        print report()

def thank_you(name,amount):
    return """Dear %s,

Thank you so much for your generous donation of $%i! Every dollar
helps local families in need, and none of it would be possible without
the generosity of loyal donors like you.

Sincerely,
Bob Smith""" % (name, amount)

def report():
#    return """
#    Name . . . Total Donated . . . No. Donations . . . Avg. Donation
#    %s         %i                  %i                  %i
#    %s         %i                  %i                  %i
#    %s         %i                  %i                  %i
#    %s         %i                  %i                  %i
#    %s         %i                  %i                  %i
#    """ % (donor_list[], tot, len(), (tot/len(donor_list.values())), \
#        donor_list[], tot, len(), (tot/len()), \
#        donor_list[], tot, len(), (tot/len()), \
#        donor_list[], tot, len(), (tot/len()), \
#        donor_list[], tot, len(), (tot/len()))
    print "Report here"
    main_menu()


if __name__ == '__main__':
    
    main_menu()
