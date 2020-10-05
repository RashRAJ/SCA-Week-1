import random
import string
import re

length = int(input('Enter password length: '))
if length < 6:
    print('weak password')
    length = int(input('Enter password length: '))

uc= int(input('enter no of upper case alphabets: '))
lc= int(input('enter no of lower case alphabets: '))
num= int(input('enter no of numbers in the password: '))
char = int(input('enter no of charcaters in the password: '))


#assigning characters
capital_letters = string.ascii_lowercase
small_letters = string.ascii_uppercase
numbers = string.digits
character = string.punctuation

#password function
def password_generator(length):
    password1 = random.choices(capital_letters, k=uc)
    password2= random.choices(small_letters, k=lc)
    password3= random.choices(numbers, k=num)
    password4= random.choices(character, k=char)

    password =(password1+password2+password3+password4)
    random.shuffle(password)
    password = ''.join(password)
    print(password)

password_generator(length)
