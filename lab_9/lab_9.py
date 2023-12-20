# import random

# def f():
#     i = 1
#     while True:
#         yield i
#         i += 1

# chars = 'abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
# number = int(input('Введите количество паролей:\n'))
# length = int(input('Введите длину пароля:\n'))
# num = int(input('Введите желаемое количество цифр в пароле:\n'))
# special = int(input('Введите желаемое количество специальных символов:\n'))

# for n in range(number):
#     all_chars = (
#         ''.join(random.choice('1234567890') for _ in range(num)) +
#         ''.join(random.choice('+-/*!&$#?=@<>') for _ in range(special)) +
#         ''.join(random.choice(chars) for _ in range(length - num - special))
#     )

#     shuffled_chars = list(all_chars)
#     random.shuffle(shuffled_chars)

#     password = ''.join(shuffled_chars)
    
#     print(password)

# import random

# def password_generator(number, length, num, special):
#     chars = 'abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
#     for n in range(number):
#         all_chars = (
#             ''.join(random.choice('1234567890') for _ in range(num)) +
#             ''.join(random.choice('+-/*!&$#?=@<>') for _ in range(special)) +
#             ''.join(random.choice(chars) for _ in range(length - num - special))
#         )

#         shuffled_chars = list(all_chars)
#         random.shuffle(shuffled_chars)

#         password = ''.join(shuffled_chars)
        
#         yield password

# # Пример использования:
# for password in password_generator(10, 8, 2, 2):
#     print(password)
 

# import random

# def f():
#     i = 1
#     while True:
#         yield i
#         i += 1

# chars = 'abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
# number = int(input('Введите количество паролей:\n'))
# length = int(input('Введите длину пароля:\n'))
# num = int(input('Введите желаемое количество цифр в пароле:\n'))
# special = int(input('Введите желаемое количество специальных символов:\n'))
# def password_generator(number, length, num, special):
#     chars = 'abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
#     for n in range(number):
#         all_chars = (
#             ''.join(random.choice('1234567890') for _ in range(num)) +
#             ''.join(random.choice('+-/*!&$#?=@<>') for _ in range(special)) +
#             ''.join(random.choice(chars) for _ in range(length - num - special))
#         )
#     shuffled_chars = list(all_chars)

#     random.shuffle(shuffled_chars)

#     password = ''.join(shuffled_chars)
    
#     print(password)

# import random
# import string

# def password_generator(number, length, num, special):
#     chars = string.ascii_letters
#     digits = string.digits
#     special_chars = '+-/*!&$#?=@<>'

#     for n in range(number):
#         # Генерация случайного количества цифр, специальных символов и букв
#         num_chars = ''.join(random.choice(digits) for _ in range(num))
#         special_chars = ''.join(random.choice(special_chars) for _ in range(special))
#         other_chars = ''.join(random.choice(chars) for _ in range(length - num - special))

#         # Объединение всех сгенерированных символов
#         all_chars = num_chars + special_chars + other_chars

#         # Перемешивание символов
#         shuffled_chars = list(all_chars)
#         random.shuffle(shuffled_chars)

#         # Формирование пароля
#         password = ''.join(shuffled_chars)
#         yield password

# number = int(input('Введите количество паролей:\n'))
# length = int(input('Введите длину пароля:\n'))
# num = int(input('Введите желаемое количество цифр в пароле:\n'))
# special = int(input('Введите желаемое количество специальных символов:\n'))

# for password in password_generator(number, length, num, special):
#     print(password)

import random

def password_generator(number, length, num, special):
    chars = 'abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    
    for n in range(number):
        all_chars = (
            ''.join(random.choice('1234567890') for _ in range(num)) +
            ''.join(random.choice('+-/*!&$#?=@<>') for _ in range(special)) +
            ''.join(random.choice(chars) for _ in range(length - num - special))
        )

        shuffled_chars = list(all_chars)
        random.shuffle(shuffled_chars)

        password = ''.join(shuffled_chars)
        yield password

number = int(input('Введите количество паролей:\n'))
length = int(input('Введите длину пароля:\n'))
num = int(input('Введите желаемое количество цифр в пароле:\n'))
special = int(input('Введите желаемое количество специальных символов:\n'))

for password in password_generator(number, length, num, special):
    print(password)
