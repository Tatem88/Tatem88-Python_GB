'''
Требуется найти в массиве A[1..N] самый близкий по величине элемент к заданному числу X. 
Пользователь в первой строке вводит натуральное число N – количество элементов в массиве. 
В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X
'''
import random
n = int(input("Введите длинну массива: "))
a = []
for i in range(0,n):
    a.append(random.randint(0, 100))
print(a)
x = int(input("Введите число: "))
for el in a:
    if el == x - 1 in a:
        print(el)
        break
    elif el == x + 1 in a:
        print(el)
        break


