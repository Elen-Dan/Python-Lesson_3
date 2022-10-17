'''
3. Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между максимальным и 
минимальным значением дробной части элементов.
 Пример:
- [1.1, 1.2, 3.1, 5, 10.01] => 0.19
'''
import random
x = int(input('Введите количество элементов списка: '))

rand_list=[]
for i in range(x):
    rand_list.append(random.uniform(1,99))
print(rand_list)

min = 1
max = 0
for i in rand_list:
    if (i - int(i)) <= min:
        min = i - int(i)
    if (i - int(i)) >= max:
        max = i - int(i)  
print(max-min)