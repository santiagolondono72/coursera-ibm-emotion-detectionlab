from ibm_watson import NaturalLanguageUnderstandingV1
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
import json

def emotion_detector(text_to_analyze):
    """
    Función que analiza el texto y detecta las emociones usando IBM Watson NLU
    """
    # En el lab de Coursera se usa 'dummy_key'
    authenticator = IAMAuthenticator('dummy_key')
    nlu = NaturalLanguageUnderstandingV1(
        version='2021-08-01',
        authenticator=authenticator
    )
  response = nlu.analyze(
        text=text_to_analyze,
        features={'emotion': {}}
    ).get_result()

    # Extraer las emociones
    emociones = response['emotion']['document']['emotion']
    
    # Encontrar la emoción dominante
    dominant_emotion = max(emociones, key=emociones.get)
    emociones['dominant_emotion'] = dominant_emotion
    
    return emociones

# Ejemplo de uso
if _name_ == "_main_":
    texto = "I am so happy and excited today!"
    resultado = emotion_detector(texto)
    print(json.dumps(resultado, indent=2))

    response = nlu.analyze(
        text=text_to_analyze,
        features={'emotion': {}}
    ).get_result()

    # Extraer las emociones
    emociones = response['emotion']['document']['emotion']
    
    # Encontrar la emoción dominante
    dominant_emotion = max(emociones, key=emociones.get)
    emociones['dominant_emotion'] = dominant_emotion
