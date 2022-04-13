import operator
num = int(input())
list_1, list_2 = set(), list()
dic= {}
for i in range(num):
    text = input().split()
    for word in text:
        dic[word] = dic.get(word, 0) + 1
sorted_a = dict( sorted(dic.items(), key=operator.itemgetter(0)))
sorted_d = dict( sorted(sorted_a.items(), key=operator.itemgetter(1),reverse=True))
print(*sorted_d.keys(), sep ='\n')

#Model solution
#from collections import Counter
# words = []
# for _ in range(int(input())):
#     words.extend(input().split())

# counter = Counter(words)
# pairs = [(-pair[1], pair[0]) for pair in counter.most_common()]
# words = [pair[1] for pair in sorted(pairs)]
# print('\n'.join(words))

# You can also solve this problem without Counter:
# n = int(input())
# counts = {}
# for _ in range(n):
#     for word in input().split():
#         counts[word] = counts.get(word, 0) + 1
# freqs = [(-count, word) for (word, count) in counts.items()]
# for c, word in sorted(freqs):
#     print(word)