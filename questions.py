import random

# Preguntas para el juego
questions = [
    "Que funcion se usa para obtener la longitud de una cadena en Python?",
    "Cual de las siguientes opciones es un numero entero en Python?",
    "Como se solicita entrada del usuario en Python?",
    "Cual de las siguientes expresiones es un comentario valido en Python?",
    "Cual es el operador de comparacion para verificar si dos valores son iguales?",
]
# Respuestas posibles para cada pregunta, en el mismo orden que las preguntas
answers = [
    ("size()", "len()", "length()", "count()"),
    ("3.14", "'42'", "10", "True"),
    ("input()", "scan()", "read()", "ask()"),
    (
        "// Esto es un comentario",
        "/* Esto es un comentario */",
        "-- Esto es un comentario",
        "# Esto es un comentario",
    ),
    ("=", "==", "!=", "==="),
]
# Indice de la respuesta correcta para cada pregunta, el el mismo orden que las preguntas
correct_answers_index = [1, 2, 0, 3, 1]

#Se inicializa el puntaje del participante
puntaje=0

# Se seleccionan 3 preguntas aleatorias sin acceder por índice
# Ahora además, las preguntas selecionadas no se repiten
questions_to_ask = random.sample(list(zip(questions, answers, correct_answers_index)), k=3)

# El usuario deberá contestar 3 preguntas
for question, answer_options, correct_answer in questions_to_ask:
    # Se muestra la pregunta y las respuestas posibles
    print(question)
    for i, answer in enumerate(answer_options):
        print(f"{i + 1}. {answer}")
    errores=0
    # El usuario tiene 2 intentos para responder correctamente
    for intento in range(2):
        user_answer = input("Respuesta: ")

        # Se verifica si la entrada es un número
        if not user_answer.isdigit(): 
            print("Respuesta inválida")
            exit(1)
        
        user_answer = int(user_answer)-1

        # Se verifica si está dentro del rango de respuestas posibles
        if user_answer < 0 or user_answer >= len(answer_options):
            print("Respuesta inválida")
            exit(1)
    
        # Se verifica si la respuesta es correcta
        if user_answer == correct_answer:
            print("¡Correcto!")
            # El participante suma un punto si acierta
            puntaje += 1 
            break
        else:
            print("Incorrecto. Intenta de nuevo.")
            errores += 1
            
        # Si el usuario no responde correctamente después de 2 intentos,
        # se muestra la respuesta correcta
    if errores== 2: 
        print("Incorrecto. La respuesta correcta es:")
        print(answer_options[correct_answer])
    puntaje= puntaje - (0.5*errores)
    # Se imprime un blanco al final de la pregunta
    print()
# Se muestra el puntaje final

print(f"Tu puntaje final es: {puntaje}")