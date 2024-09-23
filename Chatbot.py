import json

# Base de conocimiento inicial precargada
base_conocimiento = {
    "Hola": "¡Hola! ¿Cómo estás?",
    "¿Cómo estás?": "Estoy bien, gracias. ¿Y tú?",
    "¿De qué te gustaría hablar?": "Podemos hablar de lo que quieras, dime.",
}

# Función para guardar la base de conocimiento en un archivo
def guardar_conocimiento(base_conocimiento):
    with open("base_conocimiento.json", "w") as archivo:
        json.dump(base_conocimiento, archivo)

# Función para cargar la base de conocimiento desde un archivo
def cargar_conocimiento():
    try:
        with open("base_conocimiento.json", "r") as archivo:
            return json.load(archivo)
    except FileNotFoundError:
        return base_conocimiento

# Función para el módulo de adquisición de conocimiento
def adquirir_conocimiento(pregunta, base_conocimiento):
    print("No conozco la respuesta a eso.")
    nueva_respuesta = input("¿Cómo debería responder a eso en el futuro? ")
    base_conocimiento[pregunta] = nueva_respuesta
    guardar_conocimiento(base_conocimiento)
    print("¡Gracias! He aprendido algo nuevo.")

# Función principal del chat
def iniciar_chat():
    print("¡Bienvenido al sistema experto!")
    base_conocimiento = cargar_conocimiento()

    # Pregunta inicial precargada
    pregunta_inicial = "Hola"
    print(f"Sistema: {base_conocimiento[pregunta_inicial]}")
    
    while True:
        pregunta = input("Tú: ")
        
        if pregunta.lower() == "salir":
            print("Hasta luego.")
            break
        
        respuesta = base_conocimiento.get(pregunta)
        
        if respuesta:
            print("Sistema: " + respuesta)
        else:
            adquirir_conocimiento(pregunta, base_conocimiento)

# Iniciar el chat
iniciar_chat()
