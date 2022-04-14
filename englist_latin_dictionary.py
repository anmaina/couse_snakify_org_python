import string
dic = dict()
l, k, list_1, sorted_list, print_list = list(), list(), list(), list(), list()
for i in range(int(input())):
    E_word = input()
    k.append(''.join(c for c in E_word if c not in string.punctuation))
    p = k[i].split()
    list_1.append(p)
    for j in range(1,len(p)):
        l.append(p[j])
sorted_list = list(set(sorted(l)))
print(len(sorted_list))
for i in range(len(sorted_list)):
    print(sorted_list[i], end = ' - ')
    print_list = list()
    for j in list_1:
        if sorted_list[i] in j[1:]:
           print_list.append(j[0])
    print(', '.join(print_list))


# Model solution
# from collections import defaultdict

# latin_to_english = defaultdict(list)
# for i in range(int(input())):
#     english_word, latin_translations_chunk = input().split(' - ')
#     latin_translations = latin_translations_chunk.split(', ')
#     for latin_word in latin_translations:
#         latin_to_english[latin_word].append(english_word)
    
# print(len(latin_to_english))
# for latin_word, english_translations in sorted(latin_to_english.items()):
#     print(latin_word + ' - ' + ', '.join(english_translations))

    
        

   
