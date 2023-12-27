import random

def generate_password(length, num, special):
    chars = 'abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'

    num_chars = ''.join(random.choice('1234567890') for _ in range(num))
    special_chars = ''.join(random.choice('+-/*!&$#?=@<>') for _ in range(special))
    other_chars = ''.join(random.choice(chars) for _ in range(length - num - special))

    all_chars = num_chars + special_chars + other_chars

    shuffled_chars = list(all_chars)
    random.shuffle(shuffled_chars)

    password = ''.join(shuffled_chars)
    
    return password

def main():
    number = int(input('Введите количество паролей:\n'))
    length = int(input('Введите длину пароля:\n'))
    num = int(input('Введите желаемое количество цифр в пароле:\n'))
    special = int(input('Введите желаемое количество специальных символов:\n'))

    for n in range(number):
        password = generate_password(length, num, special)
        print(password)

if __name__ == "__main__":
    main()
