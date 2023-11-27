import random
import string
import pytest

def generate_password(length, num_digits, num_special_chars):
    if length <= 0:
        raise ValueError("Password length must be greater than 0")
    if num_digits < 0:
        raise ValueError("Number of digits must be non-negative")
    if num_special_chars < 0:
        raise ValueError("Number of special characters must be non-negative")

    chars = 'abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    special_chars = ''.join(random.choice('+-/*!&$#?=@<>') for _ in range(num_special_chars))
    num_chars = ''.join(random.choice('1234567890') for _ in range(num_digits))
    other_chars = ''.join(random.choice(chars) for _ in range(length - num_digits - num_special_chars))
    
    password = ''.join(random.sample(special_chars + num_chars + other_chars, length))
    return password

def test_generate_password():
    assert len(generate_password(12, 3, 2)) == 12
    assert len(generate_password(16, 4, 3)) == 16
    assert len(generate_password(8, 2, 1)) == 8

    with pytest.raises(ValueError, match="Password length must be greater than 0"):
        generate_password(0, 2, 1)

    with pytest.raises(ValueError, match="Number of digits must be non-negative"):
        generate_password(10, -2, 1)
    with pytest.raises(ValueError, match="Number of special characters must be non-negative"):
        generate_password(14, 3, -1)

if __name__ == '__main__':
    pytest.main([__file__])

