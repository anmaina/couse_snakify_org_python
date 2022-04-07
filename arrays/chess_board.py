n = 5
list_of_dots = [['.']*n for i in range(n)]
for a in range(n):
    for b in range(n):
        if abs(a-b)%2==0:
            list_of_dots[a][b] = '*'
for j in range(n): 
    print(' '.join(list_of_dots[j]))