import random
score=0


pregunta =random.choice(["¿La capital del departamento de Bolivar es?",
"¿Puerto Carreño es la capital de cuál departamento?", "¿La capital del departamento de Caquetá es?",
"¿Montería es la capital de cuál departamento?","¿La capital del departamento de Putumayo es?"])
print("                                                                     ")
print("LEVEL 1")
print("                                                                     ")
print(pregunta)

if pregunta == "¿La capital del departamento de Bolivar es?":
    print("1.Cartagena")
    print("2.Riohacha")
    print("3.Barranquilla")
    print("4.Valelldupar")
    answer = int(input("Ingrese el número de respuesta: "))
    if answer == 1:
        print("Respuesta correcta!!")
        score += 20
    else:
        print("Respuesta incorrecta reinicie el programa.")
        score=0

elif pregunta == "¿Puerto Carreño es la capital de cuál departamento?":
    print("1.Cordoba")
    print("2.Cauca")
    print("3.Vichada")
    print("4.Monteria")
    answer = int(input("Ingrese el número de respuesta: "))
    if answer == 3:
        print("Respuesta correcta!!")
        score += 20
    else:
        print("Respuesta incorrecta reinicie el programa.")
        score=0

elif pregunta == "¿La capital del departamento de Caquetá es?":
    print("1.Mocoa")
    print("2.Florencia")
    print("3.Leticia")
    print("4.Riohacha")
    answer = int(input("Ingrese el número de respuesta: "))
    if answer == 2:
        print("respuesta correcta")
        score += 20
    else:
        print("Respuesta incorrecta reinicie el programa.")
        score=0

elif pregunta == "¿Montería es la capital de cuál departamento?":
    print("1.Antoquia")
    print("2.Arauca")
    print("3.Vaupés")
    print("4.Cordoba")
    answer = int(input("Ingrese el número de respuesta: "))
    if answer == 4:
        print("Respuesta correcta!!")
        score += 20
    else:
        print("Respuesta incorrecta reinicie el programa.")
        score=0

elif pregunta == "¿La capital del departamento de Putumayo es?":
    print("1.Popayán")
    print("2.Mocoa")
    print("3.Yopal")
    print("4.Mitú")
    answer = int(input("Ingrese el número de respuesta: "))
    if answer == 2:
        print("Respuesta correcta!!")
        score += 20
    else:
        print("Respuesta incorrecta reinicie el programa.")
        score=0
else:
    print("Respuesta incorrecta reinicie el programa.")
        
print(f"Puntaje obtenido: {score}")

if score == 20:
    pregunta =random.choice(["¿Cuáles son las regiones naturales de Colombia?",
    "¿Cuáles de los departamentos mencionados a continuación pertenecen a la región Andina de Colombia?",
    "¿El departamento de Meta a que región natural de Colombia pertenece?", 
    "¿Cuáles de los departamentos mencionados a continuación pertenecen a la región Pacífica de Colombia?",
    "¿El departamento de Atlantico a que región natural de Colombia pertenece?"])
    print("                                                                     ")
    print("LEVEL 3")  
    print("                                                                     ")
    print(pregunta)

    if pregunta == "¿Cuáles son las regiones naturales de Colombia?":
        print("1.Andina, Amazonia, Caribe, Insular, Orinoquía, Pacífica")
        print("2.Andina, Amazonia, Caribe, Orinoquía")
        print("3.Andina,Central, Amazonia, Caribe, Orinoquía,")
        print("4.Andina, Amazonia, Caribe, Atlantica")
        answer = int(input("Ingrese el número de respuesta: "))
        if answer == 1:
            print("Respuesta correcta!!")
            score += 20
        else:
            print("Respuesta incorrecta reinicie el programa.")
            score=20
            
        print(f"Puntaje obtenido : {score}")

    elif pregunta == "¿Cuáles de los departamentos mencionados a continuación pertenecen a la región Andina de Colombia?":
        print("1.Amazonas, Caquetá, Guainía")
        print("2.Arauca, Casanare, Meta")
        print("3.Cauca, Valle del Cauca, Chocó")
        print("4.Boyacá, Chocó, Cundinamarca")
        answer = int(input("Ingrese el número de respuesta: "))
        if answer == 4:
            print("Respuesta correcta!!")
            score += 20
        else:
            print("Respuesta incorrecta reinicie el programa.")
            score=20
            
        print(f"Puntaje obtenido: {score}")

    elif pregunta == "¿El departamento de Meta a que región natural de Colombia pertenece?":
        print("1.Orinoquia")
        print("2.Insular")
        print("3.Pacifica")
        print("4.Andina")
        answer = int(input("Ingrese el número de respuesta: "))
        if answer == 1:
            print("respuesta correcta")
            score += 20
        else:
            print("Respuesta incorrecta reinicie el programa.")
            score=20
            
        print(f"Puntaje obtenido: {score}")

    elif pregunta == "¿Cuáles de los departamentos mencionados a continuación pertenecen a la región Pacífica de Colombia?":
        print("1.Antioquia, Boyacá, Caldas")
        print("2.Amazonas, Caquetá, Cauca y Valle del Cauca")
        print("3.Cauca, Chocó y Nariño")
        print("4.Amazonas, Caquetá, Guainía")
        answer = int(input("Ingrese el número de respuesta: "))
        if answer == 3:
            print("Respuesta correcta!!")
            score += 20
        else:
            print("Respuesta incorrecta reinicie el programa.")
            score=20
            
        print(f"Puntaje obtenido: {score}")

    elif pregunta == "¿El departamento de Atlantico a que región natural de Colombia pertenece?":
        print("1.Atlántico")
        print("2.Caribe")
        print("3.Amazonia")
        print("4.Andina")
        answer = int(input("Ingrese el número de respuesta: "))
        if answer == 2:
            print("Respuesta correcta!!")
            score += 20
        else:
            print("Respuesta incorrecta reinicie el programa.")
            score=20
                
            print(f"Puntaje obtenido: {score}")

    else:
        print("Respuesta incorrecta reinicie el programa.")
        
    print(f"Puntaje obtenido: {score}")




if score == 40:
    pregunta =random.choice(["¿Cuál es la capital de Canadá ?",
    "¿Asunción es la capital de..?", "¿Cuál es la capital de Ecuador?", 
    "¿Managua es la capital de.. ?", "¿Cuál es la capital de Bolivia?"])
    print("                                                                     ")
    print("LEVEL 2")  
    print("                                                                     ")
    print(pregunta)

    if pregunta == "¿Cuál es la capital de Canadá ?":
        print("1.Otawwa")
        print("2.Cambridge")
        print("3.Montreal")
        print("4.Quebec")
        answer = int(input("Ingrese el número de respuesta: "))
        if answer == 1:
                print("Respuesta correcta!!")
                score += 20
        else:
            print("Respuesta incorrecta reinicie el programa.")
            score=40

    elif pregunta == "¿Asunción es la capital de..?":
        print("1.Uruguay")
        print("2.Ecuador")
        print("3.Paraguay")
        print("4.Chile")
        answer = int(input("Ingrese el número de respuesta: "))
        if answer == 3:
            print("Respuesta correcta!!")
            score += 20
        else:
            print("Respuesta incorrecta reinicie el programa.")
            score=40

    elif pregunta == "¿Cuál es la capital de Ecuador?":
        print("1.Guayaquil")
        print("2.Salinas")
        print("3.La libertad")
        print("4.Quito")
        answer = int(input("Ingrese el número de respuesta: "))
        if answer == 4:
            print("respuesta correcta")
            score += 20
        else:
            print("Respuesta incorrecta reinicie el programa.")
            score=40

    elif pregunta == "¿Managua es la capital de.. ?":
        print("1.Nicaragua")
        print("2.Uruguay")
        print("3.Paraguay")
        print("4.Salvador")
        answer = int(input("Ingrese el número de respuesta: "))
        if answer == 1:
            print("Respuesta correcta!!")
            score += 20
        else:
            print("Respuesta incorrecta reinicie el programa.")
            score=40

    elif pregunta == "¿Cuál es la capital de Bolivia?":
        print("1.La paz")
        print("2.Santa Cruz de la Sierra")
        print("3.Sucre")
        print("4.Apolo")
        answer = int(input("Ingrese el número de respuesta: "))
        if answer == 3:
            print("Respuesta correcta!!")
            score += 20
        else:
            print("Respuesta incorrecta reinicie el programa.")
            score=40

    else:
        print("Respuesta incorrecta reinicie el programa.")
        
    print(f"Puntaje obtenido: {score}")

if score == 60:
    pregunta =random.choice(["¿Cuál es la moneda oficial de Dinamarca?",
    "¿El franco es la moneda oficial de que país?", "¿El sueco es el idioma oficial de que país?", 
    "¿En cuál de los siguientes países no se habla Frances?", "En que país de habla española, su moneda oficial es el dólar estadounidense"])
    print("                                                                     ")
    print("LEVEL 4")  
    print("                                                                     ")
    print(pregunta)                   

    if pregunta == "¿Cuál es la moneda oficial de Dinamarca?":
        print("1.Euro")
        print("2.Libra esterlina")
        print("3.Corona Danesa")
        print("4.Dólar")
        answer = int(input("Ingrese el número de respuesta: "))
        if answer == 3:
            print("Respuesta correcta!!")
            score += 20
        else:
            print("Respuesta incorrecta reinicie el programa.")
            score=60

    elif pregunta == "¿El franco es la moneda oficial de que país?":
        print("1.Francia")
        print("2.Suiza")
        print("3.Dinamarca")
        print("4.Noruega")
        answer = int(input("Ingrese el número de respuesta: "))
        if answer == 2:
            print("Respuesta correcta!!")
            score += 20
        else:
            print("Respuesta incorrecta reinicie el programa.")
            score=60

    elif pregunta == "¿El sueco es el idioma oficial de que país?":
        print("1.Suecia")
        print("2.Suiza")
        print("3.Checoslovaquia")
        print("4.Noruega")
        answer = int(input("Ingrese el número de respuesta: "))
        if answer == 1:
            print("respuesta correcta")
            score += 20
        else:
            print("Respuesta incorrecta reinicie el programa.")
            score=60

    elif pregunta == "¿En cuál de los siguientes países no se habla Frances?":
        print("1.Francia")
        print("2.Canadá")
        print("3.Costa de Marfil")
        print("4.Holanda")
        answer = int(input("Ingrese el número de respuesta: "))
        if answer == 4:
            print("Respuesta correcta!!")
            score += 20
        else:
            print("Respuesta incorrecta reinicie el programa.")
            score=60

    elif pregunta == "En que país de habla española, su moneda oficial es el dólar estadounidense":
        print("1.México")
        print("2.República dominicana")
        print("3.Ecuador")
        print("4.Paraguay")
        answer = int(input("Ingrese el número de respuesta: "))
        if answer == 3:
            print("Respuesta correcta!!")
            score += 20
        else:
            print("Respuesta incorrecta reinicie el programa.")
            score=60

    else:
        print("Respuesta incorrecta reinicie el programa.")
        
    print(f"Puntaje obtenido: {score}")


if score == 80:
    pregunta =random.choice(["¿Cuál es el rio más largo del mundo?",
    "¿Cuál es la ciudad con menos población del mundo?", "¿Qué acontecimiento importante sucedió el 2  de septiembre de 1945?", 
    "¿Qué acontecimiento importante sucedió el 12  de octubre de 1492?", 
    "¿Cuál de las siguientes NO es una de las 7 maravillas del mundo moderno?"])
    
    print("                                                                     ")
    print("LEVEL 5")  
    print("                                                                     ")
    print(pregunta)          

    if pregunta == "¿Cuál es el rio más largo del mundo?":
        print("1.Nilo")
        print("2.Amazonas")
        print("3.Misisipi")
        print("4.Bravo")
        answer = int(input("Ingrese el número de respuesta: "))
        if answer == 2:
            print("Respuesta correcta!!")
            score += 20
        else:
            print("Respuesta incorrecta reinicie el programa.")
            score=80                                                

    elif pregunta == "¿Cuál es la ciudad con menos población del mundo?":
        print("1.Monaco")
        print("2.Liechtenstein")
        print("3.Ciudad del vaticano")
        print("4.Dominica")
        answer = int(input("Ingrese el número de respuesta: "))
        if answer == 3:
            print("Respuesta correcta!!")
            score += 20
        else:
            print("Respuesta incorrecta reinicie el programa.")
            score=80

    elif pregunta == "¿Qué acontecimiento importante sucedió el 2  de septiembre de 1945?":
        print("1.Finaliza la segunda guerra mundial")
        print("2.Inicio de la segunda guerra mundial")
        print("3.Expulsión de los judios de España")
        print("4.Inicio de la guerra fria")
        answer = int(input("Ingrese el número de respuesta: "))
        if answer == 1:
            print("respuesta correcta")
            score += 20
        else:
            print("Respuesta incorrecta reinicie el programa.")
            score=80

    elif pregunta == "¿Qué acontecimiento importante sucedió el 12  de octubre de 1492?":
        print("1.Caida de constantinopla")
        print("2.Expulsión de los judios de España")
        print("3.Revolución Francesa")
        print("4.Descubrimiento de América")
        answer = int(input("Ingrese el número de respuesta: "))
        if answer == 4:
            print("Respuesta correcta!!")
            score += 20
        else:
            print("Respuesta incorrecta reinicie el programa.")
            score=80

    elif pregunta == "¿Cuál de las siguientes NO es una de las 7 maravillas del mundo moderno?":
        print("1.Gran Muralla China")
        print("2.Chichén Itzá")
        print("3.La torre Eiffel")
        print("4.Machu Picchu")
        answer = int(input("Ingrese el número de respuesta: "))
        if answer == 3:
            print("Respuesta correcta!!")
            score += 20
        else:
            print("Respuesta incorrecta reinicie el programa.")
            score=80

    else:
        print("Respuesta incorrecta reinicie el programa.")
        
    print(f"Puntaje obtenido: {score}")
    if score == 100:
        print("Ganaste!!. Felicitaciones!")


        
