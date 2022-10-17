'''
1. Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.
Пример:
- [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12
'''
import random
x = int(input('Введите количество элементов списка: '))

rand_list=[]
for i in range(x):
    rand_list.append(random.randint(1,9))

print(rand_list)

def sum_odd_index(rand_list):
    s = 0
    for i in range(len(rand_list)):
        if i % 2 != 0:
            s += rand_list[i]
    print(f"Сумма равна: {s}")

sum_odd_index(rand_list)