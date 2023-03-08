
dict_1 = {'a':1, 'b':2, 'c':3}
key_1 = 'p'
value_1 = dict_1.get(key_1,0) #get позволяет добавлять ключ и значение (ключ из переменной key_1, значение 0 прописано)
if value_1 == 0:
    dict_1[key_1] = value_1
    print(value_1)
    print(dict_1)
    