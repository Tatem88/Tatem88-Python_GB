'''
Найдите сумму цифр трехзначного числа.
*Пример:*
123 -> 6 (1 + 2 + 3)
100 -> 1 (1 + 0 + 0) |
'''

n = input("Введите трехзначное число: ")
n = int(n)
a = n % 10
b = n % 100 // 10
c = n // 100
print("Сумма цифр числа:", a + b + c)