#!/usr/bin/env python
import io

donor_list = {
    "John Doner": [1500],
    "Mary Doner": [900, 1800, 2000],
    "Joe Smith": [100, 150, 175],
    "Bob Andrews": [250, 250],
    "Cindy Brown": [800]
}

def safe_input(question):
    try:
        return raw_input(question)
    except EOFError:
        return None
    except KeyboardInterrupt:
        return None

def main_menu():
    print "Type Exit to quit."
    menu_select = safe_input("Please select: (1) Send a thank you note; \
(2) Create a report > ")
    
    #SEND THANK YOU
    if menu_select == "1":
        print "To return to the main menu, type 'HOME'."
        user_inp = safe_input("Please enter donor's full name, or type \
'list' to see complete list of donors. > ")
        if user_inp == "HOME":
            main_menu()
        if user_inp == "list":
            for (key, value) in donor_list.items():
                print (key, value)
            user_inp = safe_input("Please enter donor's full name. > ")
        if user_inp not in donor_list:
            while True:
                donation = safe_input("Donation amount? > ")
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
    f = io.open('thank_you.txt', mode='w')
    f.write(u"""Dear %s, \
 \
Thank you so much for your generous donation of $%i! Every dollar \
helps local families in need, and none of it would be possible without \
the generosity of loyal donors like you. \
\
Sincerely, \
Bob Smith""" % (name, amount))
    f.close()
    print "Your thank you note has been saved to thank_you.txt"


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