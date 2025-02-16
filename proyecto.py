
import pyttsx3 as tts

# Inicializar el motor de texto a voz
engine = tts.init()

# Configuración de propiedades.
engine.setProperty('rate', 200)  # <-- Velocidad de la voz
engine.setProperty('volume', 0.5)  # <-- Volumen (0.0 a 1.0)

# Texto que quieres convertir a voz.
texto = "Este es un texto de ejemplo de mi primer proyecto, pasando de texto a voz."

# Convertimos el texto a voz,
engine.say(texto)

# Reproducimos la voz.
engine.runAndWait()
