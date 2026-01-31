# BÚSQUEDA POR EMOCIÓN - Detecta emociones en el texto y responde acorde

from typing import Optional, List
import re

def search_by_emotion(user_message: str) -> Optional[List[str]]:
    """
    Detecta emociones en el mensaje y devuelve respuestas apropiadas.
    
    Args:
        user_message: Mensaje del usuario
        
    Returns:
        Lista de respuestas o None si no detecta emoción fuerte
    """
    message_lower = user_message.lower()
    
    # Patrones para emociones positivas
    positive_patterns = {
        r'\b(feliz|contento|alegre|emocionado|genial|excelente|maravilloso)\b': 'alegría',
        r'\b(orgulloso|logro|éxito|triunfo|conseguí|gané|aprobé)\b': 'orgullo',
        r'\b(esperanzado|optimista|confiado|seguro|positivo)\b': 'optimismo'
    }
    
    # Patrones para emociones negativas
    negative_patterns = {
        r'\b(triste|deprimido|desanimado|desesperado|melancolía)\b': 'tristeza',
        r'\b(enojo|enfado|furia|ira|molesto|indignado)\b': 'enojo',
        r'\b(miedo|temor|asustado|aterrorizado|ansioso|preocupado|nervioso)\b': 'miedo',
        r'\b(estresado|agobiado|abrumado|presionado|cansado|agotado)\b': 'estrés',
        r'\b(solo|soledad|aislado|incomprendido|abandonado)\b': 'soledad',
        r'\b(culpa|culpable|arrepentido|remordimiento)\b': 'culpa'
    }
    
    # Detectar emociones
    detected_emotions = []
    
    for pattern, emotion in positive_patterns.items():
        if re.search(pattern, message_lower):
            detected_emotions.append(emotion)
    
    for pattern, emotion in negative_patterns.items():
        if re.search(pattern, message_lower):
            detected_emotions.append(emotion)
    
    # Si no se detectan emociones claras, retornar None
    if not detected_emotions:
        return None
    
    # Obtener respuestas para la emoción más fuerte (primera detectada)
    primary_emotion = detected_emotions[0]
    
    # Respuestas para cada emoción (3 por cada una)
    emotion_responses = {
        'alegría': [
            "¡Me alegra mucho saber que te sientes así! 😊 Celebrar los momentos positivos es importante. ¿Quieres compartir qué te hace sentir tan bien?",
            "Es maravilloso escuchar que estás contento. Aprovecha esta energía positiva para avanzar en tus proyectos o simplemente disfrutar el momento.",
            "La alegría es contagiosa. Recuerda que puedes usar este estado emocional positivo para motivarte y motivar a otros. ¡Disfrútalo!"
        ],
        'orgullo': [
            "¡Felicidades por tu logro! 🎉 El orgullo es una emoción que motiva a seguir creciendo. Reconoce tu esfuerzo y celebra este momento.",
            "Sentir orgullo por tus logros es completamente válido. Tómate un momento para reflexionar sobre el camino que recorriste para llegar aquí.",
            "Los logros personales merecen ser celebrados. ¿Has pensado en compartir tu éxito con alguien? A veces, compartir la alegría la multiplica."
        ],
        'optimismo': [
            "El optimismo es una gran herramienta para enfrentar desafíos. Mantén esa actitud positiva y verás cómo las oportunidades aparecen.",
            "Es fantástico que tengas una visión optimista. Recuerda que el optimismo realista te permite ver oportunidades sin ignorar los desafíos.",
            "Tu actitud positiva puede inspirar a otros. ¿Hay algún proyecto en el que puedas aplicar esta energía optimista?"
        ],
        'tristeza': [
            "Lamento que estés pasando por un momento difícil. La tristeza es una emoción natural; permítete sentirla sin juicio. ¿Quieres hablar de lo que sucede?",
            "En momentos de tristeza, puede ayudar: 1) Expresar lo que sientes 2) Buscar apoyo en seres queridos 3) Realizar una actividad tranquila que te guste.",
            "La tristeza suele indicar que algo nos importa. Trata de identificar la causa y considera pequeños pasos para sentirte mejor. No tienes que hacerlo solo."
        ],
        'enojo': [
            "El enojo es una señal de que algo te importa o te ha lastimado. Intenta identificar la causa y expresarlo de manera asertiva, sin dañar a otros ni a ti mismo.",
            "Cuando sientas enojo: 1) Detente y respira hondo 2) Identifica el pensamiento detrás del enojo 3) Expresa tu necesidad de forma calmada.",
            "El enojo puede ser energía para el cambio. ¿Puedes canalizarlo hacia una solución constructiva del problema que lo causó?"
        ],
        'miedo': [
            "El miedo es una respuesta natural ante lo desconocido o amenazante. Intenta identificar si el miedo es realista y qué pequeños pasos puedes dar para enfrentarlo.",
            "Para manejar el miedo: 1) Reconoce y nombra el miedo 2) Evalúa la probabilidad real de que ocurra lo que temes 3) Prepara un plan de acción pequeño.",
            "El miedo a menudo se reduce cuando compartimos lo que sentimos. ¿Hay alguien de confianza con quien puedas hablar sobre esto?"
        ],
        'estrés': [
            "El estrés es señal de que estás enfrentando demandas importantes. Considera: ¿Puedes reducir la carga, cambiar tu perspectiva o mejorar tu manejo del tiempo?",
            "Técnicas rápidas para el estrés: respiración 4-7-8, hacer una pausa de 5 minutos, priorizar tareas con la matriz de Eisenhower, desahogarte con alguien.",
            "El estrés crónico requiere cambios. Evalúa tus hábitos de sueño, alimentación, ejercicio y tiempo de ocio. Pequeños ajustes pueden hacer gran diferencia."
        ],
        'soledad': [
            "La soledad puede ser difícil. Recuerda que es temporal y que hay personas que se preocupan por ti. ¿Has considerado unirte a un grupo o actividad social?",
            "La soledad a veces nos invita a conectar más profundamente con nosotros mismos. También puedes buscar conexiones significativas, aunque sean pocas.",
            "Cuando te sientas solo: 1) Llama a un amigo o familiar 2) Sal a un lugar público (café, biblioteca) 3) Únete a una actividad grupal (clase, voluntariado)."
        ],
        'culpa': [
            "La culpa puede ser útil si nos lleva a enmendar errores, pero no debe paralizarnos. Reflexiona: ¿Qué puedes aprender de esta situación? ¿Cómo reparar si es posible?",
            "Manejo de culpa: 1) Acepta la responsabilidad real (no exagerada) 2) Aprende la lección 3) Toma acción para reparar si es posible 4) Perdónate.",
            "Todos cometemos errores. La culpa excesiva no ayuda. ¿Estás siendo demasiado duro contigo mismo? Habla contigo como lo harías con un amigo."
        ]
    }
    
    return emotion_responses.get(primary_emotion, None)