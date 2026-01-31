# RESPUESTAS POR DEFECTO - Cuando no se encuentra nada específico

import random

def get_fallback_response() -> str:
    """
    Devuelve una respuesta por defecto cuando no se encuentra
    contenido específico para la consulta del usuario.
    
    Returns:
        Respuesta por defecto
    """
    fallback_responses = [
        "No estoy seguro de entender completamente tu consulta. ¿Podrías reformularla o ser más específico?",
        "No encuentro información específica sobre eso en mi base de conocimiento. Intenta usar palabras clave como: estrés, decisiones, equipo, creatividad, tiempo, emociones.",
        "Parece que tu consulta no coincide con mis temas actuales. Puedo ayudarte con: gestión emocional, manejo de estrés, liderazgo, pensamiento crítico o trabajo en equipo.",
        "¿Podrías darme más detalles? Por ejemplo: 'Técnicas para manejar el estrés en exámenes' o 'Cómo mejorar la toma de decisiones en equipo'.",
        "No tengo una respuesta específica para eso. Usa /temas para ver los temas sobre los que sí puedo ayudarte, o /help para ver ejemplos de consultas.",
        "Mis conocimientos están basados en las unidades de Habilidades para la Vida. Intenta mencionar algún tema como: autoconocimiento, resiliencia, liderazgo o pensamiento creativo."
    ]
    
    return random.choice(fallback_responses)

def get_general_encouragement() -> str:
    """
    Devuelve un mensaje de aliento general.
    """
    encouragements = [
        "Recuerda que el autoconocimiento es el primer paso para el crecimiento personal.",
        "Cada desafío es una oportunidad para aprender y fortalecerte.",
        "La gestión emocional es una habilidad que se desarrolla con práctica constante.",
        "Pequeños pasos consistentes llevan a grandes cambios con el tiempo.",
        "No estás solo en este proceso de aprendizaje y desarrollo personal."
    ]
    
    return random.choice(encouragements)