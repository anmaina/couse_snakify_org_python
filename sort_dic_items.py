dic = {}
suma = int()
for i in range(num):
    key, val = input().split()
    if key not in dic.keys():
        dic[key] = int(val)
    else:
        dic[key] +=int(val)
dic_sorted = sorted(dic.items())
for key,val in dic_sorted:
    print(key,val)

# Model solution
# num_votes = {}
# for _ in range(int(input())):
#     candidate, votes = input().split()
#     num_votes[candidate] = num_votes.get(candidate, 0) + int(votes)

# for candidate, votes in sorted(num_votes.items()):
#     print(candidate, votes)