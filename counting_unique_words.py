num = int(input())
text_is = list()
set_is = set()
count_num = 0
for i in range(num):
    l = input()
    text_is.append(l.split())
for i in range(num):
    for j in range(len(text_is[i])):
        set_is.add(text_is[i][j])
print(len(set_is))