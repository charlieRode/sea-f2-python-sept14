import random
import pprint

while True:
    def mainPrompt():
        """Prints the main prompt"""
        s = """What would you like to do?

            -type 'p' to print report
            -type 's' to send a thank you
            -type 'q' to quit \n: """

        userresponse = raw_input(s)
        while userresponse != 'p' and userresponse != 's' and userresponse != 'q':
            userresponse = raw_input("Please type either p', 's', or 'q'")

        return userresponse

  
    def donor():
        donorName = raw_input("Would you like a list of current donors? (type 'list') or...\n\
        Enter a new donor name (full name) \n: ")
        if donorName == 'list':
            pp = pprint.PrettyPrinter(indent=4)
            pp.pprint(dreamDonors.keys())
        else:
            amount = raw_input("And for what amount?\n: ")
            while not amount.isalnum():
                amount = raw_input("Please enter a number amount")
            
            donation = int(amount)
            inlist = False
            for name in dreamDonors:
                if donorName == name:
                    dreamDonors.get(name).append(donation)
                    inlist = True
            if inlist == False:
                dreamDonors[donorName] = [donation]
                print dreamDonors

            answer = raw_input("Would you like to print a thank you? (type 'y'or 'n')\n: ")
            
            if  answer == 'y':
                printThankYou(donorName, donation)

    def printThankYou(name,amount):
        firstname, lastname = name.split(" ")

        letterformat = """
Dear {},
Our sincerest thanks for your contribution to our cause. Your donation of ${:,} will undoubtably be \
an integral part of our success in the coming year. We expect it to be a difficult road ahead, \
but we truly derive strength from, and are encouraged by the outpouring of generosity from donors \
like yourself. Feel free to subscribe to our mailing list, or check out our blog to follow our \
progress, and to see your dollars in action. Expect a gift from us in the mail soon- just a \
small token of our gratitude, and a way to show others your continued support of our efforts.
Thank you again, from all of us here.
"""

        print letterformat.format(firstname, amount)
        

    def report():
        statlist = []
        for i in dreamDonors:
            totaldonations = sum(dreamDonors.get(i))
            number = len(dreamDonors.get(i))
            average = totaldonations/number
            newentry = (i,totaldonations,number,average)
            statlist.append(newentry)
            statlist.sort(key=getKey, reverse=True)

        for person in range(len(statlist)):

            print "Name: {}\tCumulative: {:,}\tNumber of Donations: {:,}\tAverage: {:,}"\
            .format(statlist[person][0],statlist[person][1],statlist[person][2],statlist[person][3])
        
        print "\n"
    def getKey(item):
        return item[1]


    dreamDonors = {'Bill Gates':[random.randint(500000, 1000000)], 'Melinda Gates': [random.randint(500000, 1000000)],\
     'Leroy Hood': [random.randint(500000, 1000000)], 'Paul Allen': [random.randint(500000, 1000000)], 'Bill Ruckelshaus':\
      [random.randint(500000, 1000000), random.randint(500000, 1000000), random.randint(500000, 1000000)], 'Nathan Myhrvold':\
      [random.randint(500000, 1000000), random.randint(500000, 1000000)]}
    
    response = mainPrompt() 
    if response == 'q':
        break
    elif response == 's':
        donor()
    elif response == 'p':
        report()

        
