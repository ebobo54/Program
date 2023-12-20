# import itertools

# letters = "ГЕПАРД"

# count = 0

# combinations = itertools.product(letters, repeat=5)

# for combo in combinations:
#     if combo.count("Г") == 1 and combo[0] != "А" and combo[-1] != "Е":
#         count += 1

# print(f"Количество допустимых слов: {count}")


# print(f"Количество допустимых слов: {count}")
# import itertools

# def A() : #  определяем функцию A(), которая будет считать количество допустимых слов
#     S = ['Г','Е', 'П', 'А', 'Р', 'Д']
#     count = 0 # счетчик слов
#     for i in itertools.product(S, repeat=5) : # 6-буквенные слова
#         if  i.count('Г') <= 1 and i[0] != 'А' and i[3] != 'Е': # условие задачи
#             count += 1 # счетчик слов
#     return count # возвращение значения(количество слов)
# word_count = A() # сохраняем результат в переменной
# print("№1. КОЛИЧЕСТВО СЛОВ:", word_count)
# import itertools

# letters = "ГЕПАРД"

# count = 0

# combinations = itertools.product(letters, repeat=5)

# for combo in combinations:
#     if combo.count("Г") == 1:
#         continue
#     if combo[0] == "А":
#         continue
#     if combo[-1] == "Е":
#         continue
#     count += 1

# print(f"Количество допустимых слов: {count}")

import itertools

letters = "ГЕПАРД"

count = 0

combinations = itertools.product(letters, repeat=5)

for combo in combinations:
    if combo.count("Г") != 1:
        continue
    if combo[0] == "А":
        continue
    if combo[-1] == "Е":
        continue
    count += 1

print(f"Количество допустимых слов: {count}")

# from itertools import permutations

# letters = "ГЕПАРД"
# count = 0

# for combo in permutations(letters, 5):
#     if combo.count("Г") != 1:
#         continue
#     if combo[0] == "А":
#         continue
#     if combo[-1] == "Е":
#         continue
#     count += 1

# print("Количество слов:", count)

