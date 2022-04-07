#num = int(input())
num = 5
list_of_num = [[num]*num for i in range(num)]
for a in range(num):
    for b in range(num):
        list_of_num[a][b] = str(abs(b-a))
for c in range(num):
    print(' '.join(list_of_num[c]))