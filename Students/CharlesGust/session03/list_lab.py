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
    s2_list = alist[:]
    print s2_list

    s2_list = s2_list[:-1]
    print s2_list

    fruit_to_delete = raw_input("Fruit to delete?")
    for fruit in s2_list:
        if fruit == fruit_to_delete:
            s2_list.remove(fruit_to_delete)


def series2a(alist):
    s2_list = alist[:]
    s2_list *= 2
    print s2_list

    s2_list_static = s2_list[:]
    ask_delete = True
    while ask_delete:
        fruit_to_delete = raw_input("Fruit to delete?")

        for fruit in s2_list_static:
            if fruit == fruit_to_delete:
                ask_delete = False
                s2_list.remove(fruit_to_delete)
    print s2_list
    return s2_list


def series3(alist):
    new_list = []
    for fruit in alist:
        ask_like = True
        while ask_like:
            like_fruit = raw_input("Do you like %s? (yes/no):" % fruit.lower())
            if like_fruit == "no":
                ask_like = False
            elif like_fruit == "yes":
                new_list.append(fruit)
                ask_like = False
    print new_list
    return new_list


def series4(alist):
    pass


if __name__ == "__main__":
    alist = []
    alist = series1(alist)
    series2(alist)
    series2a(alist)
    series3(alist)
    series4(alist)


