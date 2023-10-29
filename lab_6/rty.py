def find_numbers():
    numbers = []
    current_number = 500001

    while len(numbers) < 5:
        divisors = []
        for i in range(8, current_number):
            if current_number % i == 0:
                divisors.append(i)
                if i % 10 == 8 and i != 8:
                    numbers.append((current_number, i, current_number // i))
                    break
        current_number += 1

    return numbers

if __name__ == "__main__":
    result = find_numbers()
    for number, divisor, quotient in result:
        print(f"{number} {divisor} {quotient}")

