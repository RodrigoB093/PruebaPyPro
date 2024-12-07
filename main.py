meme_dict = {
            "BRO": "Se usa para referirse a un amigo o alguien de confianza.",
            "BUGUEADA": "Se usa para decir que algo no funciona como debería.",
            "BOOMER": "Se refiere a una persona desactualizada.",
            "CHETAO": "Es una expresión que viene del mundo gamer y se usa para decir que una habilidad o arma es muy buena",
            "GG": "Acrónimo de Good Game que se usa para reconocer una buena partida al adversario.",
            "SMURF": "Cuando un jugador experimentado crea una cuenta nueva para jugar contra jugadores de rango inferior.",
            "FARMEAR": "Realizar acciones repetitivas en el juego para obtener recursos o puntos.",
            }
print("¡Bienvenido al diccionario!")
for i in range(5):
    word = input("Escribe una palabra que no entiendas (¡con mayúsculas!): ")
    if word in meme_dict.keys():
        print(meme_dict[word])
    else:
        print("La palabra no se encuentra en el diccionario.")
