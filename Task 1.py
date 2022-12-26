# Задайте список из нескольких чисел.
# Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной идексах.

import random

elem_number = int(input("Введите кол-во элементов списка: "))
res = 0
my_list = [random.randint(-10, 10) for i in range(elem_number)]
for i in range(1, len(my_list), 2):
        res += my_list[i]
print(my_list)
print(res)