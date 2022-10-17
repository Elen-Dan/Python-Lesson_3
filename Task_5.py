'''
5. Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.
Пример:
- для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21]
[Негафибоначчи] https://ru.wikipedix.org/wiki/Негафибоначчи
'''

num = int(input('Введите число: '))

fibo_nums = []
x, y = 1, 1
for i in range(num-1):
    fibo_nums.append(x)
    x, y = y, x + y
x, y = 0, 1
for i in range(num):
    fibo_nums.insert(0, x)
    x, y = y, x - y

print(fibo_nums)
