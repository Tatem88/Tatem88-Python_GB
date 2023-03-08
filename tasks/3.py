'''превращение list строк в list список'''

data = '115 156 96 3 4 8 52 5'
print(data)



data = list(map(int, data.split()))
print(data)

