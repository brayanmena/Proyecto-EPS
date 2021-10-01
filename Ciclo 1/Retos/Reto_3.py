def validar_persona(empleados:dict, lista_empleados:tuple)-> dict:
    
    for key in empleados.keys():
        if ((empleados[key] >= 3000000) and (key in lista_empleados)):
            empleados[key] = (empleados[key] * 20) / 100
        else:
            empleados = "Revisar datos"
            break
        
    return empleados

empleados= {
    '1085273528': 50000000,
    '1085245785': 10000000,
    '1789785475': 7000000}

lista_empleados=(
    '1789785475',
    '1085273528',
    '1085245785')


print(validar_persona(empleados, lista_empleados))