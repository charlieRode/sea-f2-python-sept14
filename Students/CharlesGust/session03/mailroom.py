donation_db = [["Alice", [500, 100, 100]],
               ["Betty", [50]],
               ["Carol", [1000, 10, 10]],
               ["Debbie", [25, 25, 25]],
               ["Ellie", [200, 200]]]
action = raw_input("Choose: 1. Send a Thank You, 2. Create a Report: ")

if int(action) == 1:
    full_name = raw_input("What is the Full Name?")
    if full_name == "list":
        for donor in donation_db:
            print donor[0]

