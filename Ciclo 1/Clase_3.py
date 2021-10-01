#Diccionarios
'''
nombrediccionario = {
    "clave":valor
}
'''


cuentas_banco={
    "tipo_cuenta": {
        "empresarial": "Cuenta corriente",
        "personal": "Cuenta de ahorros"
    },
    "numero_cuenta": 10908734,
    "saldo": 120000
}
'''
print("Su tipo de cuenta es: " + cuentas_banco["tipo_cuenta"]["empresarial"])
print(cuentas_banco["numero_cuenta"])
print(cuentas_banco["saldo"])

if cuentas_banco["saldo"] > 100000:
    print("Cuenta empresarial")
else:
    print("Cuenta personal")
'''

#---------------------------------------------------------
if cuentas_banco["saldo"] > 100000:
    banco={"cuenta":cuentas_banco["tipo_cuenta"]["empresarial"], "deposito":cuentas_banco["numero_cuenta"]}
else:
    banco={"cuenta":cuentas_banco["tipo_cuenta"]["personal"], "deposito":cuentas_banco["numero_cuenta"]}

print(banco)