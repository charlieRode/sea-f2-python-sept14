#!/usr/local/bin/python

donor_history = [(u"Colonel Mustard", [100, 200, 300])]
donor_history.append((u"Mrs. White", [50, 10.95]))
donor_history.append((u"Professor Plum", [300, 300]))
donor_history.append((u"Mr. Green", [1000, 2000]))
donor_history.append((u"Miss Scarlet", [1000]))

option_indexes = [1, 2, 3]
options = [u"Send a Thank You", u"Create a Report", u"Exit"]

def initial_prompt():
    """Return an int representing the user's selection among the options"""
    print "Please select from the following options: "
    i = 0
    for index in option_indexes:
        print "%i) %s" % (index, options[i])
        i = i + 1
    selection = int(raw_input("Enter the number of your selection: "))
    while selection not in option_indexes:
        print "Invalid selection\n\a"
        selection = int(raw_input("Enter the number of your selection: "))
    return selection

def list_donors():
    """List full names of donors"""
    print "We have records for the following donors"
    for record in donor_history:
        print record[0]

def send_thankyou():
    """Generate a thank you note for an individual donor"""
    donor = raw_input("Enter the Full Name of the donor (or 'list' to list the donors): ")
    if donor == "list":
        list_donors()

def create_report():
    pass

if __name__ == '__main__':
    user_selection = initial_prompt()
    while user_selection != 3:
        if user_selection == 1:
            send_thankyou()
        if user_selection == 2:
            create_report()
        user_selection = initial_prompt()




