# Texto a Voz con pyttsx3
Este proyecto utiliza la librería pyttsx3 para convertir texto en voz. pyttsx3 es una librería multiplataforma que funciona sin necesidad de conexión a internet y es compatible con Windows, macOS y Linux.

# Requisitos Previos
Antes de ejecutar el proyecto, asegúrate de tener instalado Python en tu sistema. Además, necesitarás instalar la librería pyttsx3. Puedes instalarla utilizando pip:

bash
Copy
pip install pyttsx3
Configuración del Proyecto
Clona este repositorio en tu máquina local o descarga los archivos del proyecto.

Asegúrate de que tienes un entorno de Python configurado y que has instalado la librería pyttsx3 como se mencionó anteriormente.

# Uso del Código
El siguiente código muestra cómo utilizar pyttsx3 para convertir texto en voz:

python
Copy
import pyttsx3 as tts

# Inicializar el motor de texto a voz
engine = tts.init()

# Configuración de propiedades.
engine.setProperty('rate', 500)  # <-- Velocidad de la voz
engine.setProperty('volume', 0.5)  # <-- Volumen (0.0 a 1.0)

# Texto que quieres convertir a voz.
texto = "Este es un texto de ejemplo de mi primer proyecto, pasando de texto a voz."

# Convertimos el texto a voz,
engine.say(texto)

# Reproducimos la voz.
engine.runAndWait()
Explicación del Código
Inicialización del motor: engine = tts.init() inicializa el motor de texto a voz.

Configuración de propiedades:

engine.setProperty('rate', 500): Establece la velocidad de la voz. El valor por defecto es 200. Un valor más alto aumenta la velocidad.

engine.setProperty('volume', 0.5): Establece el volumen de la voz. El valor debe estar entre 0.0 (mudo) y 1.0 (volumen máximo).

Conversión de texto a voz: engine.say(texto) añade el texto a la cola de reproducción.

Reproducción de la voz: engine.runAndWait() reproduce el texto en voz alta y espera hasta que termine la reproducción.

Personalización
Puedes personalizar la voz y otros parámetros según tus necesidades. Aquí hay algunas opciones adicionales que puedes explorar:

Cambiar la voz: Puedes cambiar la voz utilizando engine.setProperty('voice', voice_id). Para obtener una lista de voces disponibles, puedes usar el siguiente código:

python
Copy
voices = engine.getProperty('voices')
for voice in voices:
    print("Voice:", voice.name, "ID:", voice.id)
Guardar el audio en un archivo: Puedes guardar el audio generado en un archivo utilizando engine.save_to_file(texto, 'nombre_del_archivo.mp3') antes de llamar a engine.runAndWait().

Ejecución del Proyecto
Para ejecutar el proyecto, simplemente ejecuta el archivo Python que contiene el código:

bash
Copy
python nombre_del_archivo.py
Contribuciones
Si deseas contribuir a este proyecto, por favor abre un issue o envía un pull request. Todas las contribuciones son bienvenidas.

Licencia
Este proyecto está bajo la licencia MIT. Para más detalles, consulta el archivo LICENSE.
