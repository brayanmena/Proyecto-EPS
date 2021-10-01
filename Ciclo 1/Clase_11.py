import pandas as pd

data = {'Nombres': ['Brayan', 'Julio', 'Stiwar','Yeison', 'Carlos', 'William', 'Jorge', 'Jorling'],
        'Apellidos': ['Mena', 'Perea', 'Martines', 'Parra', 'Cordoba', 'Moreno', 'Palomeque', 'Cano'],
        'Edad': [27, 31, 36, 53, 48, 36, 40, 34],
        'cantidad_1': [7.17, 1.90, 1.11, 1.41, 6.69, 4.62, 1.01, 4.88],
        'cantidad_2': [8.06,  "?", 5.90,  "?",  "?", 7.48, 4.37,  "?"]}

datosDataFrame = pd.DataFrame(data)

print(datosDataFrame)

datosDataFrame = pd.DataFrame(data, index= ["Jefe", "Aliado", "Empleado", "Lavador", "Rentador", "Cobrador", "Pagador", "Conductor"])

print(datosDataFrame)

#Acaba la implementacion

datosDataFrame.to_csv("C:/Users/57350/OneDrive/Desktop/example.csv")

datosDataFrame.to_csv('nombre_salida.csv', sep=';')

df = pd.read_csv('example.csv')

print(df)