import random
print('Welocome to guess a nubmber! \nToday might just be your lucky day, Come on take a guess ;)')
print(          )
print('='*8,'start','='*8)

user_input = int(input('Enter a number between 0 - 20: '))
lucky_number = random.randint(0, 21)


def guess_a_num(user_input, lucky_number):
    for i in range(6):
        if lucky_number == user_input:
            print('Congratulations you got the right number !!')
            break
        elif lucky_number > user_input:
            print('Oops! Too low try again')
            user_input = int(input('Enter a number between 0 - 20: '))
        elif lucky_number < user_input:
            print('Oops! Too high try again')
            user_input = int(input('Enter a number between 0 - 20: '))
        else:
            print('oops!, you are out of turns :(')
            print('correct number was ', lucky_number)

       
guess_a_num(user_input, lucky_number)
