# Задача 16: Требуется вычислить, сколько раз встречается некоторое
# число X в массиве A[1..N]. Пользователь в первой строке вводит
# натуральное число N – количество элементов в массиве. В последующих
# строках записаны N целых чисел Ai
# . Последняя строка содержит число X
import random
from random import randint
start_pos = int (input('Введите начальное значение массива: '))
n = int (input('Введите число элементов массива: '))
count = 0

lst = [random.randint(start_pos,n) for _ in range(n)]

# for i in range (start_pos,n+1):
#     lst.append(i)

print(lst)

x = randint(start_pos,n)
print(x)

for i in range (len(lst)):
    if lst[i] == x:
        count +=1

print(count)




