#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Создайте списки:

# моя семья (минимум 3 элемента, есть еще дедушки и бабушки, если что)
my_family = ['mama', 'papa', 'babushka', 'dedushka']


# список списков приблизителного роста членов вашей семьи
my_family_height = [
    # ['имя', рост],
    ['mama',190],['papa', 110],['babushka',10],['dedushka', 200]
]
# Выведите на консоль рост отца в формате
#   Рост отца - ХХ см
for member in my_family_height:
    if member[0] == 'papa':
        print(f"Рост отца - {member[1]} см")
# Выведите на консоль общий рост вашей семьи как сумму ростов всех членов
#   Общий рост моей семьи - ХХ см
total_height = sum([member[1] for member in my_family_height])
print(f"Общий рост моей семьи - {total_height} см")