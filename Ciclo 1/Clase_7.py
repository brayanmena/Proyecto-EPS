# Cadenas a listas y viceversa
'''
cadena = "Programando"
lista = list(cadena)

print(cadena)
print(lista)

# De lista a cadena
print(''.join(lista))

# ---------------------------------------------------

conjuntoIdentificador = set({"1", "2", "3", "4"})
if "1" in conjuntoIdentificador:
    print("True")
else:
    print("False")

# ---------------------------------------------------
# Diccionario a lista paso a paso
diccionario = {
    "01": "Tarea",
    "02": "Tarea2"
}
print(diccionario)
print(list(diccionario))
print(list(diccionario.keys()))
print(list(diccionario.values()))
print(diccionario.items())
print(list(diccionario.items()))
print(list(diccionario.items())[0])
print(list(diccionario.items())[1])

c = list(diccionario.items())[1]
print(' '.join(list(c)))
'''
# ---------------------------------------------------
# Funciones lambda
suma_numeros = lambda n1, n2: n1 + n2
print(suma_numeros(4, 7))

promedio = lambda v1, v2, v3: (v1 + v2 + v3)/3
print(promedio(5, 10, 15))

elevar_al_cubo = lambda x: x**3
print(elevar_al_cubo(6))
