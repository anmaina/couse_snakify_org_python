# num = input()
# stuff = input()
num = 20
stuff = {'2','5', '8', '10', '15', '14', '17'}
yes_set, no_set, full_set = set(), set(), set()
set_of_num = []

def yes_no(stuff):
    while stuff!='HELP':
        set_of_num = stuff.split()
        response = input()
        if response=='YES':
            for i in range(len(set_of_num)):
                yes_set.add(set_of_num[i])
                print (yes_set)
        elif response == 'NO':
            for i in range(len(set_of_num)):
                no_set.add(set_of_num[i])
                print (no_set)
    stuff = input()

for i in range(1,num+1):
    full_set.add(i)
yes_no(stuff)
result = yes_set&(full_set - no_set)
print(result)
        