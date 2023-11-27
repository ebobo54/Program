import random

chars = '+-/*!&$#?=@<>abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890'
number = input('количество паролей:\n')
len = input('длина пароля:\n')
number = int(number)
len = int(len)
for n in range(number):
    password =''
    for i in range(len):
        password += random.choice(chars)
    print(password)