num = int(input())
l = list()
for i in range(num):
    l.append(input().split())
#print(l)
num_ex = int(input())
for i in range(num_ex):
   check, file = input().split() 
   for j in range(num):
        if file in l[j]:
            if check=='read' and 'R' in l[j] or check == 'write' and 'W' in l[j] or check== 'execute' and 'X' in l[j]:
                print('OK')
            else:
                print('Access denied')

# Model solution
# OPERATION_PERMISSION = {'read': 'R','write': 'W','execute': 'X'}

# file_permissions = {}
# for i in range(int(input())):
#     file, *permissions = input().split()
#     file_permissions[file] = set(permissions)

# for i in range(int(input())):
#     operation, file = input().split()
#     if OPERATION_PERMISSION[operation] in file_permissions[file]:
#         print('OK')
#     else:
#         print('Access denied')