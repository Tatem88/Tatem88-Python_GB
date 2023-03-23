'''
Есть список a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89].
Выведите все элементы, которые меньше 5.
'''
# a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
# print(list(filter(lambda elem: elem < 5, a)))

'''
a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89];
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13].
Нужно вернуть список, который состоит из элементов, общих для этих двух списков.
'''
# a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
# b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
# result = list(filter(lambda elem: elem in b, a))
# print(result)


'''
Отсортируйте словарь по значению в порядке возрастания и убывания
'''
# import operator
# d = {1: 2, 3: 4, 4: 3, 2: 1, 0: 0}
# result = dict(sorted(d.items(), key=operator.itemgetter(1)))
# result = dict(sorted(d.items(), key=operator.itemgetter(1), reverse=True))
# print(result)