# logic/password_generator.py
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
