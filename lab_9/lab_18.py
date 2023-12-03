import random

def generate_password(length, num, special):
    # Символы для генерации пароля
    chars = 'abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'

    # Генерация цифр, специальных символов и остальных символов
    num_chars = ''.join(random.choice('1234567890') for _ in range(num))
    special_chars = ''.join(random.choice('+-/*!&$#?=@<>') for _ in range(special))
    other_chars = ''.join(random.choice(chars) for _ in range(length - num - special))

    # Сбор всех символов
    all_chars = num_chars + special_chars + other_chars

    # Перемешивание символов
    shuffled_chars = list(all_chars)
    random.shuffle(shuffled_chars)

    # Сбор символов в пароль
    password = ''.join(shuffled_chars)
    
    return password

def main():
    # Запрос параметров у пользователя
    number = int(input('Введите количество паролей:\n'))
    length = int(input('Введите длину пароля:\n'))
    num = int(input('Введите желаемое количество цифр в пароле:\n'))
    special = int(input('Введите желаемое количество специальных символов:\n'))

    # Создание и вывод паролей
    for n in range(number):
        password = generate_password(length, num, special)
        print(password)

if __name__ == "__main__":
    main()
