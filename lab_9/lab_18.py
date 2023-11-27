import random

chars = 'abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
number = int(input('Введите количество паролей:\n'))
len = int(input('Введите длину пароля:\n'))
num = int(input('Введите желаемое количество цифр в пароле:\n'))
special = int(input('Введите желаемое количство специальных символов:\n'))
for n in range(number):
    special_chars = ''.join(random.choice('+-/*!&$#?=@<>') for _ in range(special))
    num_chars = ''.join(random.choice('1234567890') for _ in range(num))
    other_chars = ''.join(random.choice(chars) for _ in range(len - num))
    password = ''.join(random.sample(special_chars + num_chars + other_chars, len))
    
    print(password)