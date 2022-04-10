list_input = [1, 2, 5, 2, 6, 2, 9]
# list_input = input().split()
for i in range(len(list_input)):
    if list_input[i] in list_input[:i]:
        print('YES')
    else:
        print('NO')