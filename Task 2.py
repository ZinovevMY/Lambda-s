# Напишите программу, которая найдёт произведение пар чисел списка.
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.

import random

elem_number = int(input('Введите кол-во элементов списка: '))
my_list = [random.randint(-10, 10) for i in range(elem_number)]
revers_list = list(reversed(my_list))

mult = lambda a, b: a * b
step_count = len(my_list) / 2
res_list = list()
if step_count % 2 != 0:
    step_count += 1
for i in range(int(step_count)):
    if i+1 == int(step_count):
        res_list.append(my_list[i])
    else:
        res_list.append(mult(my_list[i], revers_list[i]))

print(my_list)
print(res_list)
