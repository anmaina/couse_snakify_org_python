def swap_columns(a, i, j):
    for b in range(int(num[0])):
        for c in range(int(num[1])):
            if c == j:
                a[b][i],a[b][j] = a[b][j],a[b][i]
    for g in range(int(num[0])):
        print(' '.join(a[g]))
num = input().split()
a = []
for b in range(int(num[0])):
    a.append(input().split())
columns = [int(s) for s in input().split()]
swap_columns(a, columns[0], columns[1])