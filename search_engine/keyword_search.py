# BÚSQUEDA POR PALABRAS CLAVE
import re
from typing import Optional, List, Dict
from knowledge_base.keywords_mapping import KEYWORDS_MAPPING

def search_by_keyword(user_message: str) -> Optional[List[str]]:
    """
    Busca palabras clave exactas en el mensaje del usuario.
    Retorna las respuestas asociadas a esa palabra clave.
    
    Args:
        user_message: Mensaje del usuario en minúsculas
        
    Returns:
        Lista de respuestas posibles o None si no encuentra
    """
    # Normalizar mensaje
    message_lower = user_message.lower().strip()
    words = re.findall(r'\b\w+\b', message_lower)
    
    # Buscar coincidencias exactas
    for word in words:
        if word in KEYWORDS_MAPPING:
            return KEYWORDS_MAPPING[word]["responses"]
    
    # Buscar coincidencias parciales (palabras compuestas)
    for keyword, data in KEYWORDS_MAPPING.items():
        if len(keyword.split()) > 1:  # Palabra compuesta
            if keyword in message_lower:
                return data["responses"]
    
    return None

# UNIDAD 1: INTELIGENCIA EMOCIONAL
# Palabras clave relacionadas con autoconocimiento y gestión emocional
AUTOCONOCIMIENTO_KEYWORDS = {
    "autoconocimiento", "conocerme", "identidad", "valores",
    "fortalezas", "debilidades", "autoevaluación", "reflexión"
}

GESTION_EMOCIONAL_KEYWORDS = {
    "emociones", "sentimientos", "control emocional", "regular emociones",
    "ira", "tristeza", "alegría", "miedo", "ansiedad", "estrés"
}

# UNIDAD 2: RESILIENCIA Y MANEJO DE ESTRÉS
# Palabras clave relacionadas con estrés y adaptación
ESTRES_KEYWORDS = {
    "estrés", "agotamiento", "burnout", "presión", "tensión",
    "ansiedad", "nervios", "preocupación", "inquietud"
}

ADAPTACION_KEYWORDS = {
    "adaptación", "cambio", "flexibilidad", "resiliencia",
    "superar", "afrontar", "desafíos", "obstáculos"
}

# UNIDAD 3: LIDERAZGO
# Palabras clave relacionadas con liderazgo y trabajo en equipo
LIDERAZGO_KEYWORDS = {
    "liderazgo", "líder", "equipo", "grupo", "coordinación",
    "delegar", "motivar", "inspirar", "dirigir"
}

TOMA_DECISIONES_KEYWORDS = {
    "decisión", "elegir", "opciones", "alternativas", "evaluar",
    "plan", "estrategia", "objetivos", "metas"
}

# UNIDAD 4: PENSAMIENTO CRÍTICO Y CREATIVO
# Palabras clave relacionadas con pensamiento
PENSAMIENTO_KEYWORDS = {
    "pensamiento", "crítico", "creativo", "innovación",
    "ideas", "soluciones", "problemas", "análisis"
}