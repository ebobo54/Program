import lab_9
import pytest
import string

def test_password_length():
    length = 12
    num = 3
    special = 2
    password = lab_9.generate_password(length, num, special)
    assert len(password) == length

def test_password_digits():
    length = 12
    num = 3
    special = 2
    password = lab_9.generate_password(length, num, special)
    assert sum(c.isdigit() for c in password) == num

def test_password_special_chars():
    length = 12
    num = 3
    special = 2
    password = lab_9.generate_password(length, num, special)
    assert sum(c in '+-/*!&$#?=@<>' for c in password) == special

def test_password_alphanumeric():
    length = 12
    num = 3
    special = 2
    password = lab_9.generate_password(length, num, special)
    assert all(c.isalnum() or c in '+-/*!&$#?=@<>' for c in password)

@pytest.mark.parametrize("length, num, special", [
    (8, 2, 1),
    (10, 4, 2),
    (16, 5, 3),
])
def test_password_generated(length, num, special):
    password = lab_9.generate_password(length, num, special)
    assert len(password) == length
    assert sum(c.isdigit() for c in password) == num
    assert sum(c in '+-/*!&$#?=@<>' for c in password) == special
    assert all(c.isalnum() or c in '+-/*!&$#?=@<>' for c in password)
