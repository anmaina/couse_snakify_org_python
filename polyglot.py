num_of_student = int(input())
one_lan = set()
dif_lan, result = list(), set()
for i in range(num_of_student):
    num_of_languages = int(input())
    for j in range(num_of_languages):
        a = input()
        one_lan.add(a)
        dif_lan.append(a)
for i in range(len(dif_lan)):
    if dif_lan.count(dif_lan[i])==num_of_student:
        result.add(dif_lan[i])
result = sorted(result)
one_lan = sorted(one_lan)
print(len(result))
print('\n'.join(str(i) for i in result)) 
print(len(one_lan))
print('\n'.join(str(i) for i in one_lan))

# students = [{input() for j in range(int(input()))} for i in range(int(input()))]
# known_by_everyone, known_by_someone = set.intersection(*students), set.union(*students)
# print(len(known_by_everyone), *sorted(known_by_everyone), sep='\n')
# print(len(known_by_someone), *sorted(known_by_someone), sep='\n')