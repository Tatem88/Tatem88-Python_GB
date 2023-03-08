import random
n = int(input("Введите длинну массива: "))
a = []
res = list()
for i in range(0,n):
    a.append(random.randint(0, 9))
    if i % 2 == 0:
        res.append((i,i**2))
print(res)
