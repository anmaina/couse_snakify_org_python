def get_key(val):
    for key, value in country_dic.items():
        for i in range(len(value)):
            if val == value[i]:
                return key
num = int(input())
country_dic = {}
for i in range(num):
    country, *city = input().split()
    country_dic[country] = list(city)
#print(country_dic.items())
num2 = int(input())
for i in range(num2):
    p = input()
    print(get_key(p))

# model solution
# motherland = {}
# for i in range(int(input())):
#     country, *cities = input().split()
#     for city in cities:
#         motherland[city] = country
        
# for i in range(int(input())):
#     print(motherland[input()])