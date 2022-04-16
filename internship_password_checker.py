import string


def check_item_digit(password):
    sum_digit = sum(1 for i in password if i.isdigit())
    if sum_digit > 0:
        return True
    else:
        return False


def check_item_lowercase_and_uppercase(password):
    sum_lower = sum(1 for i in password if i.islower())
    sum_upper = sum(1 for i in password if i.isupper())
    if sum_lower > 0 and sum_upper > 0:
        return True
    else:
        return False


def check_item_punctuation(password):
    sum_punctuation = sum(1 for i in password if i in string.punctuation)
    if sum_punctuation > 0:
        return True
    else:
        return False


def check_length(password):
    if len(password) >= 14:
        return True
    else:
        return False


def print_conclusion():
    a = check_item_digit(password)
    b = check_item_lowercase_and_uppercase(password)
    c = check_item_punctuation(password)
    d = check_length(password)
    if a == True and b == True and c == True and d == True:
        print('Strong password')
    else:
        print('Weak password:')
        if a != True:
            print(' - The password must contain at least one digit')
        if b != True:
            print(' - The password must contain both lowercase and uppercase characters')
        if c != True:
            print(' - The password must contain at least one punctuation character ({})'.format(string.punctuation))
        if d != True:
            print(' - The password must be at least 14 characters long')


if __name__ == '__main__':
    password = input('Enter your password here: ')
    print(print_conclusion())



# initial code
# import string

# def password_checker(password):
#     sum_lowercase = 0
#     sum_uppercase = 0
#     sum_digit = 0
#     sum_punctuation = 0
#     for i in password:
#         if i.islower():
#             sum_lowercase += 1
#         elif i.isupper():
#             sum_uppercase += 1
#         elif i.isdigit():
#             sum_digit += 1
#         elif i in string.punctuation:
#             sum_punctuation += 1
#     #print(sum_punctuation, sum_uppercase, sum_lowercase, sum_digit, len(password))
#     #checking what is wrong
#     if sum_punctuation == 0 or sum_uppercase == 0 or sum_lowercase == 0 or sum_digit == 0 or len(password) < 14:
#         print('Weak password:')
#         if sum_lowercase == 0 or sum_uppercase == 0:
#             print(' - The password must contain both lowercase and uppercase characters')
#         if sum_punctuation == 0:
#             print(' - The password must contain at least one punctuation character ({})'.format(string.punctuation))
#         if sum_digit == 0:
#             print(' - The password must contain at least one digit')
#         if len(password) < 14:
#             print(' - The password must be at least 14 characters long')
#         return ''
#     else:
#         return 'Strong password'
# # passwords: 'koromyslonegnetsya', 'k1a2r4a5m6b8a', 'lllllllll111111111111111*', '98989899989898989899898989**', 
# #            'K3nds#a', 'mMmMa973)$Nlkja*'
# #password = '98989899989898989899898989**'
# password = input('Enter your password here: ')
# print(password_checker(password))