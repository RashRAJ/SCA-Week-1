import random
import string
import re

length = int(input('Enter password length: '))
if length < 6:
    print('weak password')

#assigning characters
capital_letters = string.ascii_lowercase
small_letters = string.ascii_uppercase
numbers = string.digits
character = string.punctuation

#password function
def password_generator(length):
    Generator = (character+numbers+small_letters+capital_letters)
    password = random.choices(Generator, k=length)
    password =  ''.join(password)

    return password

password_generator(length)

# password quality check    
'''
#To make sure there are alphabets, characters and numbers in the password
        pattern = '(\w) (\W)'
        match = re.search(pattern, password)


        if match:
            return password
        else:
            i += 1

'''
