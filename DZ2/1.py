'''
Задача 10: На столе лежат n монеток. Некоторые из них лежат вверх решкой, а некоторые – гербом. 
Определите минимальное число монеток, которые нужно перевернуть, 
чтобы все монетки были повернуты вверх одной и той же стороной. 
Выведите минимальное количество монет, которые нужно перевернуть
'''
import random
n = int(input("Введите количество монеток: "))
a = []
for i in range(0,n):
   a.append(random.randint(0, 1))
print(a)
print(a.count(1))
print(a.count(0))
if a.count(1) > a.count(0):
   print("Нужно перевернуть", a.count(0),  "монеток повернутых решкой") 
elif a.count(1) < a.count(0):
   print("Нужно перевернуть", a.count(1),  "монеток повернутых гербом")
else:
   print("Равное количество монеток с гербом и решкой. Переверните любые монетки")
