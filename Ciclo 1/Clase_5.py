'''
for x in range(1, 11):
    r = 5 * x
    print("5 X {} = {}".format(x, r))
'''
#-------------------------------------------------

datos_basicos = {
    "nombres":"Brayan Estiven",
    "apellidos":"Mena Moreno",
    "cedula":"26938401",
    "fecha_nacimiento":"05/11/1998",
    "lugar_nacimiento":"Antioquia, Medellín, Colombia",
    "nacionalidad":"Colombiano",
    "estado_civil":"Soltero"
}

clave = datos_basicos.keys()
valor = datos_basicos.values()
cantidad_datos = datos_basicos.items()

for clave, valor in cantidad_datos:
    print(clave + ": " + valor)



