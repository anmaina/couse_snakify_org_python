rows_colums = input().split()
n = int(rows_colums[0])
m = int(rows_colums[1])
list_of_dots = [['.']*m for i in range(n)]
for a in range(n):
    for b in range(m):
        if abs(a-b)%2!=0:
            list_of_dots[a][b] = '*'
for j in range(n): 
    print(' '.join(list_of_dots[j]))