import random

def f():
    i = 1
    while True:
        yield i
        i += 1

chars = 'abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
number = int(input('Введите количество паролей:\n'))
length = int(input('Введите длину пароля:\n'))
num = int(input('Введите желаемое количество цифр в пароле:\n'))
special = int(input('Введите желаемое количество специальных символов:\n'))

for n in range(number):
    all_chars = (
        ''.join(random.choice('1234567890') for _ in range(num)) +
        ''.join(random.choice('+-/*!&$#?=@<>') for _ in range(special)) +
        ''.join(random.choice(chars) for _ in range(length - num - special))
    )

    # Shuffle all the characters
    shuffled_chars = list(all_chars)
    random.shuffle(shuffled_chars)

    # Join the shuffled characters to form the password
    password = ''.join(shuffled_chars)
    
    print(password)
