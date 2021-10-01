'''
def pago_trabajadores():
    salario=float(input("Ingrese su salario: "))
    descuento=salario*0.40
    eps=descuento*0.125
    pension=descuento*0.16
    arl=descuento*0.1
    print("El trabajador debe pagar por EPS: "+str(eps))
    print("El trabajador debe pagar por pension: "+str(pension))
    print("El trabajador debe pagar por arl: "+str(arl))
pago_trabajadores()
'''

def pagosTrabajador(salario: float)->str:
    descuento=salario*0.40
    eps=descuento*0.125
    pension=descuento*0.16
    arl=descuento*0.1
    print("El trabajador debe pagar por EPS: $" + str(eps) + ", por Pensión: $" + str(pension) + " y por ARL: $" + str(arl))
pagosTrabajador(1700000)
