def series1(alist):
    # print lists from session03, series 1
    alist = ["Apples", "Pears", "Oranges", "Peaches"]
    print alist

    another_fruit = raw_input("What's another fruit?-->")
    alist.append(another_fruit)
    print alist

    anumber = raw_input("What's a number?-->")
    if int(anumber) > 0 and int(anumber) < len(alist):
        print alist[int(anumber)-1]

    alist = ["Tomato"] + alist
    print alist

    alist.insert(0, "Avocado")
    print alist

    for i in alist:
        if i[0] == "P":
            print i

    return alist


def series2(alist):
    for i in range(0, len(alist)):
        ask_like = True
        while ask_like:
            like_fruit = raw_input("Do you like %s?" % alist[i].lower())
            if like_fruit == "no":
                ask_like = False

                alist = alist[:i] + alist[i+1:]
            elif like_fruit == "yes":
                ask_like = False
    print alist
    return alist

if __name__ == "__main__":
    alist = []
    alist = series1(alist)
    alist = series2(alist)


