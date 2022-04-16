import string
import random

def password_generator():
    all_possible_characters = list(string.printable)
    password = []
    for item in range(15):
        password.append(random.choice(all_possible_characters))
    sum_lowercase = 0
    sum_uppercase = 0
    sum_digit = 0
    sum_punctuation = 0
    sum_whitespace = 0
    for i in password:
        if i.islower():
            sum_lowercase += 1
        elif i.isupper():
            sum_uppercase += 1
        elif i.isdigit():
            sum_digit += 1
        elif i in string.punctuation:
            sum_punctuation += 1
        elif i == ' ':
            sum_whitespace += 1
    if sum_punctuation == 0 or sum_uppercase == 0 or sum_lowercase == 0 or sum_digit == 0 or sum_whitespace >=1:
        return password_generator()
    else:
        return ''.join(password)

print(password_generator())

