num = int(input())
val = 1
dic, dic_sorted =dict(), dict()
for i in range(num):
    text = input().split()
    for j in range(len(text)):
        p = text[j]
        if text[j] not in dic.keys():
            dic[p] = val
        else:
            dic[p] += 1
dic_sorted = dict(sorted(dic.items()))
#print(dic_sorted)
list_of_val = list(dic_sorted.values())
#print(list_of_val)
list_of_keys = list(dic_sorted.keys())
#print(list_of_keys)
max_value = list_of_val.index(max(list_of_val))
print(list_of_keys[max_value])

# Model solution
# counter = {}
# for i in range(int(input())):
#     line = input().split()
#     for word in line:
#         counter[word] = counter.get(word, 0) + 1
        
# max_count = max(counter.values())
# most_frequent = [k for k, v in counter.items() if v == max_count]
# print(min(most_frequent))