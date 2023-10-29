import itertools

letters = "ГЕПАРД"

count_valid_words = 0

combinations = itertools.product(letters, repeat=5)

for combo in combinations:
    if combo.count("Г") == 1 and combo[0] != "А" and combo[-1] != "Е":
        count_valid_words += 1

print(f"Количество допустимых слов: {count_valid_words}")
