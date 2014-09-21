#!/usr/bin/env python2.7

donors = [
'Harry', [1000, 5000, 10000],
'Franklin', [1000, 500, 750],
'George', [950, 760],
'Dwight', [1100, 3500],
'Dean', [8000]
]
#Mailroom Function
def main_menu(donors=donors):
    action = 0
    while (action != '1') or (action != '2') or (action != 'q'): #action not in ['1','2']
        print '''
        Mailroom Menu:
        1. Send a Thank You
        2. Create a Report
        Type "MM" at any prompt to return to this menu.
        Type "q" to exit script.
        '''
        action = raw_input('Enter the number from the menu above: ')
        if action == '1':
            thank_you(donors)
        elif action == '2':
            report(donors)
        elif action == 'q':
            break
            #import sys
            #sys.exit()
    return



#Exit out of any point in script to mailroom menu
#def main_exit(exit, donors):
#    if exit == 'MM':
#        main_menu(donors)
#    return

#Thank you letters for immediate donation
def thank_you(donors):
        while True:
            donation = ValueError #For first elif

            thank = raw_input('Enter "list" for donors, donor name, or name to be added: ')
            #main_exit(thank, donors)

            if thank == 'list':
                print donors[::2]
                continue
                #x = 2

            elif thank in donors[::2]: #If a valid name is entered
                while donation == ValueError: #to verify an integer is being entered
                    donation = raw_input("Please enter a valid donation amount ($): ")
                    if thank == 'MM':
                        return
                    try:
                        if int(donation): #Evaluates if donation is an integer. Goes to except if not.
                            break #If donatio#n is an integer, it breaks from the while donation == ValueError loop
                    except ValueError: #Overrides error
                        continue
                        # Goes back to while donation == ValueError
                        # .isdigit()
                donorhistoryloc = 1 + donors.index(thank) #FInds the index location of monetary list, which is one index after the name in the donors list
                donors[:][donorhistoryloc].append(int(donation)) #Add value in 'donation' to list (in donor list) location referenced in obove line
                print '''
                Thank you %s for you generous donation of $%i. These funds will
                provide George Nuesca with further chances to eat sushi,
                especially otoro. Your donation will also help establish a fund to
                bring additional guests to future otoro adventures. If you would
                like to donate otoro directly, please contact our stockhouse.
                We hope one day you too can enjoy otoro, possibly with us!
                ''' % (thank, int(donation))
                #Go back to the beginning of the while loop (x==1)
                continue

            elif thank == 'MM':
                return

            else: #if any other string is entered, ask the user if they want to it to the donor list
                verify = 'a'
                while (verify != 'n') or (verify != 'y'): #While verify isn't 'y' or 'n', keeps asking
                    if (verify == 'n') or (verify == 'y'):
                        break
                    elif verify == 'MM':
                        return
                    verify = raw_input('Add %s to the donor list (y, n)? ' % thank)
                if verify == 'y':  #if yes, add the name and a blank list to the donor list
                    donoradd = [thank, []]
                    donors += donoradd
                elif verify == 'n':
                    None
                continue

#Create a Report
def report(donors):
    person = donors[::2]
    don = donors[1::2]
    for i in range(len(person)):
        don[i].insert(0, person[i])
    don.sort(key = len)
    don.reverse()
    print '{0:<20}     {1:^13}     {2:^19}     {3:^20}'.format('Name','Total Donated',
        'Number of Donations', 'Average per Donation')
    print '-' * 91
    for i in range(len(don)):
        name = tuple(don[i])
        total = don[i]
        total.pop(0)
        print '{0:<20}     {1:^13}     {2:^19}     {3:^20}'.format(name[0],
            sum(total), len(total), sum(total)/len(total))
    return

if __name__ == '__main__':
    main_menu()