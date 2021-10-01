'''
n = 5
while n > 0:
    print(n)
    n = n - 1
print("Despegue!")

#----------------------------------------------

n = 0
while n <= 10:
    print(n)
    n = n + 1
print("Ciclo terminado!")

#----------------------------------------------

numero = int(input("Digite el numero para la tabla de multiplicar: "))
n = 0
while n <= 10:
    r = numero*n
    print("{} x {} = {}".format(numero, n, r))
    n = n + 1

#----------------------------------------------

def tabla_multiplicar(numero:int, var:int):
    n = 1
    while n <= var:
        r = numero*n
        print("{} x {} = {}".format(numero, n, r))
        n = n + 1
tabla_multiplicar(6, 10)
'''
#----------------------------------------------

while True:
    try:
        a = int(input("Tabla de multiplicar del: "))
        n = 1
        while n <= 10:
            r = int(a)*n
            print("{} x {} = {}".format(a, n, r))
            n = n + 1
        break
    except ValueError:
        print("Lo que digitó no es un número, intentelo nuevamente")