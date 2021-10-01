print("Juego MisiónTIC")

total_preguntas=4 #Cantidad de preguntas que tiene el juego
puntaje=0 #Variable que almacena las opciones correctas del juego

#Primera pregunta
respuesta=input("1. Cuál es el nombre de la plataforma de MisiónTIC 2022: ")
if respuesta.lower()=="imaster":
    print("Correcto")
    puntaje=puntaje+1 #Puntaje += 1
else:
    print("Incorrecto")

#Segunda pregunta
respuesta=input("2. En qué año estamos? ")
if respuesta=="2021":
    print("Correcto")
    puntaje=puntaje+1
else:
    print("Incorrecto")

#Tercera pregunta
respuesta=input("3. Cuánto es 8 + 4 + 1 - 4 - 2? ")
if respuesta=="7" or respuesta.lower()=="siete":
    print("Correcto")
    puntaje=puntaje+1
else:
    print("Incorrecto")

#Cuarta pregunta
respuesta=input("4. Cuál es el mejor lenguaje de programación? ")
if respuesta.lower()=="python":
    print("Correcto")
    puntaje=puntaje+1
else:
    print("Incorrecto")

#Resultado almacena el porcentaje de acierto
resultado=(puntaje/total_preguntas)*100
print("Resultado final fue {} de {} con un porcentaje de {}%".format(puntaje, total_preguntas, resultado))
