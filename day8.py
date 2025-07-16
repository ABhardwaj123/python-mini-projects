#password strength checker and random password suggester

import string
import random
import getpass #getpass helps you maintain privacy and security. like in this case while entering the password nobody can see that on the screen

def password_strength(password):
    weakness = []

    if len(password) < 8:
        weakness.append("password is small(must be of 12 characters)!")

    if not any(c.islower() for c in password):
        weakness.append("no lowercase letter is there!")

    if not any(c.isupper() for c in password):
        weakness.append("no uppercase letter is there!")

    if not any(c.isdigit() for c in password):
        weakness.append("no digits is there!")

    if not any(c in string.punctuation for c in password):
        weakness.append("no special character is there!")

    return weakness

def random_password():

    # lowercase_set = 'abcdefghijklmnopqrstuvwxyz'
    # uppercase_set = 'ABCDEFGHIJKLMNOPQRSTUVQXYZ'
    # digit_set = '0123456789'
    # punctuation_set= '#$%&*+,-/?/@~'

    # random_pass = ""
    
    # for i in range(1,5):
    #     random_pass += random.choice(lowercase_set)
    
    # for i in range(1,5):
    #     random_pass += random.choice(uppercase_set)

    # for i in range(1,5):
    #     random_pass = random.choice(digit_set)

    # for i in range(1,5):
    #     random_pass = random.choice(punctuation_set)

    # password_list = list(random_pass)
    # random.shuffle(password_list)
    # shuffled_password = "".join(password_list)
    
    # return shuffled_password

    all_chars = string.ascii_letters + string.digits + string.punctuation

    return "".join(random.choice(all_chars) for _ in range(12))



user_pass = getpass.getpass("enter your password: ")
weakness = password_strength(user_pass)

if weakness:
    print("you have a weak password!!\n")
    print("here are the flaws in your password")

    for weak in weakness:
        print(weak)

else:
    print("\nyou have a strong password")
    exit

print("\nsuggesting you a string password😀")

strong_pass = random_password()
print(strong_pass)
    
        






    
    
    