def count_fours_in_expression():

    result = 5 ** 36 + 5 ** 24 - 25

    base5_str = baseN(result, 5)

    count_4 = base5_str.count('4')

    return count_4

def baseN(num, base):
    digits = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    if num == 0:
        return '0'
    converted_num = ""
    while num > 0:
        digit = num % base
        converted_num = digits[digit] + converted_num
        num //= base
    return converted_num

if __name__ == "__main__":
    count = count_fours_in_expression()
    print(count)
