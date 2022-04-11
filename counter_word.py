txt = input().split()
for i in range(len(txt)):
    print(txt[:i].count(txt[i]), end = ' ')

# counter = {}
# for word in input().split():
#     counter[word] = counter.get(word, 0) + 1
#     print(counter[word] - 1, end=' ')