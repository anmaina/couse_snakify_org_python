def multiplication_mtx(a, b):
    m = len(a)
    n = len(a[0])
    r = len(b[0])
    c = [[0]*r for i in range(m)]
    for i in range(m):
        for j in range(r):
            for k in range(n):
                c[i][j] += a[i][k] * b[k][j] 
    return c           

m,n,r = 2, 2, 2
array_1 = [[1,2], [3,4]]
array_2 = [[5,4], [3,2]]
for b in range(m):
    array_1.append(input().split())
for l in range(n):
    array_2.append(input().split())
c = multiplication_mtx(array_1, array_2)
c_string = [[str(j) for j in range(r)] for i in range(m)]
# for i in range(m):
#     for j in range(r):
#         c[i][j] = str(c[i][j])
for p in len(c_string):
    print(' '.join(c_string[p]))