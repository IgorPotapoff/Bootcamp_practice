# Задача 18: Требуется найти в массиве A[1..N] самый близкий по
# величине элемент к заданному числу X. Пользователь в первой строке
# вводит натуральное число N – количество элементов в массиве. В
# последующих строках записаны N целых чисел Ai
# . Последняя строка содержит число X
import random
from random import randint
def nearest(lst, y):
    return min(lst, key=lambda x: abs(x-y))

start_pos = int (input('Введите начальное значение массива: '))
n = int (input('Введите число элементов массива: '))
count = 0

lst = [random.randint(start_pos,n) for _ in range(n)]

print(lst)

x = int (input('Введите число X: '))
print(x)


print(nearest(lst, x))