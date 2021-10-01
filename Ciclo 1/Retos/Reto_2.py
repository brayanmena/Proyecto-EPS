def calcularNivelExigencia(nombre, edad: int, medida: int):
    lpm = 220 - edad
    lim1 = lpm * 0.50
    lim2 = lpm * 0.60
    lim3 = lpm * 0.80
    lim4 = lpm * 0.100
    exigencia = ""

    if medida < lim1:
        exigencia = "Reposo"
    elif medida < lim2:
        exigencia = "Exigencia baja"
    elif medida < lim3:
        exigencia = "Exigencia media"
    elif medida <= lim4:
        exigencia = "Exigencia máxima"

    deportista = {
        "nombre": nombre.upper(),
        "edad": edad,
        "medida": medida,
        "lpm": lpm,
        "exigencia": exigencia
    }
    return deportista
    
print(calcularNivelExigencia("carlos rengifo", 35, 100))