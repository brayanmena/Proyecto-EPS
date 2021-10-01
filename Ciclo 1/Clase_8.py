'''
def suma(val1 = 0, val2 = 0):
    return val1 + val2

def operacion(funcion, val1 = 0, val2 = 0):
    return funcion(val1, val2)

funcion_suma = suma
resultado = operacion(funcion_suma, 10, 20)
print(resultado)
'''
#----------------------------------------------------

#print(elevar_al_cubo(3))
elevar_al_cubo = lambda n: n**3


# map --> "Transformar"
# Creamos la lista
lista_numeros: list = [2, 3, 4, 5, 6, 7, 8, 9]
#map(funcion_a_aplicar, un_iterable)
print(list(map(elevar_al_cubo, lista_numeros)))

def filtrar(dato):
    if dato=="á":
        return "a"
    elif dato=="é":
        return "e"
    elif dato=="í":
        return 'i'
    elif dato=='ó':
        return 'o'
    elif dato=='ú':
        return 'u'
    else: 
        return dato

#Función anónima
caracteres = lambda letras : list( map(filtrar,letras) )

#Palabra a procesar
palabra = "olímpica"
#Llama la función lambda con la palabra casteada a lista
#Y obtiene una nueva lista con los caracteres sin tilde
resultado = caracteres( list(palabra) )
print( ''.join(resultado))
#----------------------------------------------------

fruit = {"01":"aple", "02":"orange"}
#fruit = ["Apple", "Banana", "Pear", "Apricot", "Orange"]
map_object = map(lambda s: s[0] == "A", fruit.values)
lista = list(map_object) #[True, False]
print(lista)
#----------------------------------------------------

numeros = [1,2,3,4,5,6,7,8,9,10]
resultado = filter(lambda x: x%2 == 0, numeros) #condicional en los elementos de la lista
print(list(resultado))

resultado = [x for x in numeros if x%2 == 0]
print(resultado)
#----------------------------------------------------

from functools import reduce

lista = [1,2,3,4]
def acumulador(acumulador = 0,elemento = 0):
    return acumulador + elemento

resultado = reduce(acumulador, lista)
print(resultado)

resultado = reduce(lambda acumulador = 0, elemento = 0: acumulador + elemento, lista)
print(resultado)
#----------------------------------------------------

nombres = ["Raul", "Pedro", "Sofia"]
apellidos = ["López Briega", "Perez", "Gonzalez"]

nombreApellido = zip(nombres, apellidos)
print(list(nombreApellido))
#----------------------------------------------------

#Operador Ternario
resultado = "True" if 1 == 2 else "False"
print(resultado)

lista = [1==1, 2==2, True, True, True]
if all(lista):
    print("Todos son True")
else:
    print("Al menos uno no es True")


lista = [1==3, 2==3, True, False, True]
if any(lista):
    print("Algunos son True")
else:
    print("Ninguno es verdadero")

#Cantidad indefinida de argumentos-> *args

"""
De forma análoga funcionan los keyword arguments, 
que son representados con dos asteriscos (**) y el nombre kwargs. 
Cabe destacar que los nombres de estos parámetros son indiferentes; 
args y kwargs son utilizados simplemente por convención.
"""