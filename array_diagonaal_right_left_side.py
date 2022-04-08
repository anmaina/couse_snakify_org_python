#num = int(input())
num = 6
list_of_num = [['.']*num for i in range(num)]
n = num-1
for a in range(num):
    for b in range(num):
        if a+b < n:
            list_of_num[a][b]='0'
        elif a+b > n:
            list_of_num[a][b]='2'
        else:
            list_of_num[a][b]='1'
for c in range(num):
    print(' '.join(list_of_num[c]))