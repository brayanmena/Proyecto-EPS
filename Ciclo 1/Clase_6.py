'''
listas = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]]
for i in range(len(listas)):
    for j in range(len(listas[i])):
        print(listas[i][j])

#----------------------------------------------------

lista = []
for l in range(3, 22, 3):
    lista.append(l)
print(lista)
'''
# ---------------------------------------------------

print([x for x in range(10, 101, 10)])

print([x**2 for x in range(4, 31, 2) if x % 3 == 0])
