import random

def generate_password(number, length, num_count, special_count):
    chars = 'abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    passwords = []

for n in range(number):
    special_chars = ''.join(random.choice('+-/*!&$#?=@<>') for _ in range(special_count))
    num_chars = ''.join(random.choice('1234567890') for _ in range(num_count))
    other_chars = ''.join(random.choice(chars) for _ in range(length - num_count - special_count))
    password = ''.join(random.sample(special_chars + num_chars + other_chars, length))
    passwords.append(password)
    return passwords

if name == "main":
    number = int(input('Введите количество паролей:\n'))
    length = int(input('Введите длину пароля:\n'))
    num_count = int(input('Введите желаемое количество цифр в пароле:\n'))
    special_count = int(input('Введите желаемое количество специальных символов:\n'))

    generated_passwords = generate_password(number, length, num_count, special_count)

for password in generated_passwords:
    print(password)
yield
