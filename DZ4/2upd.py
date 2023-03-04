'''
В фермерском хозяйстве в Карелии выращивают чернику. Она растет на круглой грядке, причем кусты высажены только по окружности.
 Таким образом, у каждого куста есть ровно два соседних. Всего на грядке растет N кустов.
Эти кусты обладают разной урожайностью, поэтому ко времени сбора на них выросло различное число ягод – 
на i-ом кусте выросло РАНДОМНОЕ колличество ягод.
В этом фермерском хозяйстве внедрена система автоматического сбора черники.
 Эта система состоит из управляющего модуля и нескольких собирающих модулей. 
 Собирающий модуль за один заход, находясь непосредственно перед некоторым кустом, собирает ягоды с этого куста и с двух соседних с ним.
Напишите программу для нахождения максимального числа ягод, которое может собрать за один заход собирающий модуль, 
находясь перед некоторым кустом заданной во входном файле грядки.
'''
import random
n = int(input("Введите количество кустов: "))
a = []
for i in range(0,n):
    a.append(random.randint(0, 9))
print(a)
buff = 0
max = 0
index = 0
for i in range(0, n - 2):
    buff = a[i] + a[i+1] + a[i+2]
    buff2 = (a[-2] + a[-1] + a[0])
    if max < buff:
        max = buff
        index = i + 1
    if max < buff2:
        max = buff2
        index = i + 1
print("Подойди к кусту с индексом", index, "и ты соберешь", max, "ягод.")