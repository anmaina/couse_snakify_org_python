# Alice_cub, Bob_cub = [int(i) for i in input().split()]
# Alice_cub_set = set()
# Bob_cub_set = set() 
# for i in range(Alice_cub):
#     Alice_cub_set.add(input())
# for j in range(Bob_cub):
#     Bob_cub_set.add(input())
Alice_cub = 4
Bob_cub = 3
Alice_cub_set = {0, 1, 10, 9}
Bob_cub_set = {1, 3, 0 }
# Alice_cub_set = {0',1','10','9'}
# Bob_cub_set = {1,'3','0'}

print(len(Alice_cub_set&Bob_cub_set))
dif = list(Alice_cub_set&Bob_cub_set)
dif_sorted = sorted(int(i) for i in dif)
print('\n'.join(str(i) for i in dif_sorted))

print(len(Alice_cub_set-Bob_cub_set))
dif1 = list(Alice_cub_set-Bob_cub_set)
dif1_sorted = sorted(int(i) for i in dif1)
print('\n'.join(str(i) for i in dif1_sorted))

dif2 =Bob_cub_set - Alice_cub_set
print(len(Bob_cub_set-Alice_cub_set))
dif2_sorted = sorted(int(i) for i in dif2)
print('\n'.join(str(i) for i in dif2_sorted)) 

''''teacher solution more interesting with function 
def print_set(some_set):
    print(len(some_set))
    print(*[str(item) for item in sorted(some_set)])

N, M = [int(s) for s in input().split()]
A_colors, B_colors = set(), set()
for i in range(N):
    A_colors.add(int(input()))
for i in range(M):
    B_colors.add(int(input()))
    
print_set(A_colors & B_colors)
print_set(A_colors - B_colors)
print_set(B_colors - A_colors)'''