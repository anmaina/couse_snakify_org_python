num = int(input())
dic= dict()
for i in range(num):
    key, val = input().split()
    dic[key] = val
key_list = list(dic.keys())
val_list = list(dic.values())
syn = input()
if syn in val_list:
    position = val_list.index(syn)
    print(key_list[position])
else:
    position = key_list.index(syn)
    print(val_list[position])

# Model solution
#     n = int(input())
# d = {}
# for i in range(n):
#     first, second = input().split()
#     d[first] = second
#     d[second] = first
# print(d[input()])