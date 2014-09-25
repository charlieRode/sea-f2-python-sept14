#!/usr/bin/env python

def is_a_num(string):
    """Determines if a string represents an int or a float"""
    string = string.decode("utf-8")
    for c in string:
        if c in [',', '.']:
            continue
        else:
            if not c.isnumeric(): return False
    return True

def thankyou_mail(name, donation):
    letter = "\n\nDear %s,\n\nThank you for your generous donation of $%.2f. The Society for Gerbils with Skin Cancer depends\nupon the support of caring individuals like yourself and is grateful for your contribution. \n\nSincerely,\nFat Patty\n______________________________\n\nSGSC\nSaving the World One Gerbil at a Time" % (name, donation)
    return letter + "\n\n"

def doner_stats(name):
    total = sum(doners[name])
    num_donations = len(doners[name])
    average = total / num_donations
    return "{:22s} {:<16.2f} {:<20d} {:<20.2f}".format(name, total, num_donations, average)

def add_donation(record, person, don):
    if person in record:
        record[person] += don,
    else:
        record[person] = don,

def display_report():
    print "{:22s} {:16s} {:20s} {:20s}\n".format("Name", "Total Donations", "Number of Donations", "Average Donation")
    for person in doners.keys():
        print doner_stats(person)
    print "\n\n"


doners = {}
doners["Abraham Lincoln"] = (100.00, 150.00)
doners["He-Man"] = (50.00,)
doners["Batman"] = (2000.00,)
doners["Billy Mays"] = (100.00, 50.00)
doners["Lochness Monster"] = (3.50,)
doners["Papa Smurf"] = (1000.00, 750.00, 1000.00)


if __name__ == "__main__":

    while True:
        main_menu = raw_input(u"[1] Send a 'Thank You' \n[2] Create a Report\n[Q]uit\n ").title()

        if main_menu == u'Q':
            break

        elif main_menu == u'1':
            while True:
                name = raw_input(u"Enter the name of the doner:\n[Q] Go Back\n ").title()
                if name == u"List":
                    for doner in doners.keys():
                        print doner
                elif name == u'Q': break
                else:
                    while True:
                        try:
                            donation = float(raw_input(u"How much has %s donated?\n " % name))
                        except ValueError:
                            continue
                        else:
                            if donation <= 0:
                                print u"Donations must be greater than $0.00\n"
                                continue
                            break

                    add_donation(doners, name, donation)

                    print thankyou_mail(name, doners[name][len(doners[name]) - 1])
                    break

        elif main_menu == u'2':
            display_report()