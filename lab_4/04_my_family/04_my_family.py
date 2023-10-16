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
print(my_family_height[0],my_family_height[1],my_family_height[2],my_family_height[3])
# Выведите на консоль рост отца в формате
#   Рост отца - ХХ см

# Выведите на консоль общий рост вашей семьи как сумму ростов всех членов
#   Общий рост моей семьи - ХХ см
sum(my_family_height)