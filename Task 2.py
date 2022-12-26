# Напишите программу, которая найдёт произведение пар чисел списка.
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.

import random

elem_number = int(input('Введите кол-во элементов списка: '))
my_list = [random.randint(-10, 10) for i in range(elem_number)]

# mult = lambda a, b: a * b
step_count = len(my_list) / 2
# res_list = list()
if step_count % 2 != 0:
   step_count += 1
# for i in range(int(step_count)):
#     if i == step_count and neg:
#         res_list.append(my_list[i])
#     else:
#         res_list.append(mult(my_list[i], my_list[-1 - i]))
res_list = [a*b for a, b in zip(my_list, my_list[-1::-1])]
print(my_list)
print(res_list)


