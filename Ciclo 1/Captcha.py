from os import system
import random

system("cls")

longitud: int = 5

abecedario: str = "1234567890abcdefghijklmopqrstuvwxyz"
# Elije aleatoriamente 5 elementos del abecedario
desordenar: list = random.sample(abecedario, longitud)
# join crea cadenas a partir de objetos iterables
palabra: str = ''.join(desordenar)

print(palabra)
x: str = input("Ingresa el código que ves en pantalla: ")
if x == palabra:
    print("El código es correcto.")
else:
    print("El código es incorrecto.")

input("Presiona enter para salir.")


conjuntoIdentificador = set({"1", "2", "3", "4"})
if "10" in conjuntoIdentificador:
    print("True")
else:
    print("False")
