'''
2. Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент, второй и предпоследний и т.д.
 Пример:
- [2, 3, 4, 5, 6] => [12, 15, 16];
- [2, 3, 5, 6] => [12, 15]
'''

import random
x = int(input('Введите количество элементов списка: '))

rand_list=[]
for i in range(x):
    rand_list.append(random.randint(1,99))
print(rand_list)

l = len(rand_list)//2 + 1 if len(rand_list) % 2 != 0 else len(rand_list)//2
new_lst = [rand_list[i]*rand_list[len(rand_list)-i-1] for i in range(l)]
print(new_lst)