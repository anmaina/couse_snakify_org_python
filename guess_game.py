def yes_no_help(stuff):
    if stuff == 'YES':
        for i in range(len(set_of_num)):
                yes_set.add(set_of_num[i])
                print(yes_set)
    elif stuff == 'NO':
        for i in range(len(set_of_num)):
                no_set.add(set_of_num[i])
                print(no_set)
    elif stuff == 'HELP':
        full_set = [i for i in range(num)]
        print(full_set-(yes_set&no_set))
    else:
        set_of_num = [int(i) for i in stuff.split()]
        

num = input()
yes_set, no_set, full_set = set(), set(), set()
set_of_num = [int(i) for i in input().split()]
stuff = input()
while stuff!='HELP':
    yes_no_help(stuff)
    stuff = input()

