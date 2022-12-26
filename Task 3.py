# Задайте список из N элементов, заполненных числами из промежутка [-N, N].
# Найдите произведение элементов на указанных индексах. Индексы вводятся одной строкой, через пробел.

elem_count = int(input("Введите кол-во элементов: "))
index_numbers = input("Введите номера индексов через пробел: ").split()
index_numbers = [int(i) for i in index_numbers]
result = 1

num_list = [i for i in range(-elem_count, elem_count+1)]
mult = lambda a, b: a*b

for i in range(len(index_numbers)):
    if index_numbers[i] < len(num_list):
        result = mult(result, num_list[index_numbers[i]])
    else:
        print(f"В списке нет элемента с индексом {index_numbers[j]}!")

print(num_list)
print(result)
