# Emotion Detection Application

Aplicación de detección de emociones desarrollada como proyecto final del curso "Developing AI Applications with Python and Flask" de IBM, dentro del programa IBM Full Stack Software Developer Professional Certificate.

La aplicación utiliza la biblioteca Watson NLP para analizar un texto y determinar las emociones presentes (enojo, disgusto, miedo, alegría y tristeza), identificando además la emoción dominante. La aplicación está desplegada como un servicio web usando el framework Flask.

## Tecnologías utilizadas
- Python
- Flask
- Watson NLP (IBM)
- Requests

## Estructura del proyecto
- `EmotionDetection/emotion_detection.py` — lógica de detección de emociones, se comunica con el servicio de Watson NLP
- `server.py` — servidor Flask con los endpoints de la aplicación
- `templates/` — interfaz web (HTML)
- `static/` — archivos estáticos (CSS, JS)

## Cómo ejecutar
1. Instalar dependencias:
   ```
   pip install -r requirements.txt
   ```
2. Ejecutar el servidor:
   ```
   python server.py
   ```
3. Abrir en el navegador:
   ```
   http://localhost:5000
   ```

> **Nota:** esta aplicación requiere el entorno de IBM Skills Network Cloud IDE, ya que el servicio de Watson NLP embebido solo responde desde esa red.

## Autor
Santiago Londoño
