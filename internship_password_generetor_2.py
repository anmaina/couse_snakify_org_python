import string
import random

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

min_length_of_password = 14

def check_length(password):
    if len(password) >= min_length_of_password:
        return True
    else:
        return False


def password_generator():
    all_possible_characters = list(string.ascii_letters + string.digits + string.punctuation)
    password = []
    for item in range(min_length_of_password+1):
        password.append(random.choice(all_possible_characters))
    return ''.join(password)


def password_output():
    new_password = password_generator()
    a = check_item_punctuation(new_password)
    b = check_item_digit(new_password)
    c = check_item_lowercase_and_uppercase(new_password)
    d = check_length(new_password)
    if a and b and c and d is False:
        return password_output()
    else:
        return new_password
if __name__ == '__main__':
    print(password_output())