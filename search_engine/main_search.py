# PROCESO PRINCIPAL DE BÚSQUEDA - Coordina todos los métodos de búsqueda
# Este es el orquestador principal que llama a las diferentes funciones de búsqueda

import logging
from search_engine.keyword_search import search_by_keyword
from search_engine.content_search import search_by_content
from search_engine.emotion_search import search_by_emotion
from search_engine.fallback_search import get_fallback_response
from responses.response_selector import ResponseSelector
from utils.text_processor import extract_keywords

logger = logging.getLogger(__name__)
response_selector = ResponseSelector()

def main_search_engine(user_message: str, user_id: str = "default") -> str:
    """
    Proceso principal de búsqueda que sigue una jerarquía:
    1. Búsqueda por palabra clave exacta
    2. Búsqueda por contenido/tema
    3. Búsqueda emocional
    4. Respuesta por defecto
    
    Args:
        user_message: Mensaje del usuario
        user_id: ID del usuario para mantener historial de respuestas
        
    Returns:
        Respuesta formateada
    """
    logger.info(f"Iniciando búsqueda para mensaje: {user_message}")
    
    # Extraer palabras clave para logging
    keywords = extract_keywords(user_message)
    if keywords:
        logger.info(f"Palabras clave detectadas: {keywords}")
    
    # 1. BÚSQUEDA POR PALABRA CLAVE (UNIDAD 1-4)
    keyword_response = search_by_keyword(user_message)
    if keyword_response:
        logger.info("✓ Encontrado por palabra clave")
        selected_response = response_selector.select_random_response(
            keyword_response, 
            user_id
        )
        return selected_response
    
    # 2. BÚSQUEDA POR CONTENIDO/TEMA (ANÁLISIS SEMÁNTICO)
    content_response = search_by_content(user_message)
    if content_response:
        logger.info("✓ Encontrado por contenido")
        selected_response = response_selector.select_random_response(
            content_response, 
            user_id
        )
        return selected_response
    
    # 3. BÚSQUEDA EMOCIONAL (SI APLICA)
    emotion_response = search_by_emotion(user_message)
    if emotion_response:
        logger.info("✓ Encontrado por análisis emocional")
        selected_response = response_selector.select_random_response(
            emotion_response, 
            user_id
        )
        return selected_response
    
    # 4. RESPUESTA POR DEFECTO
    logger.info("✗ No encontrado, usando respuesta por defecto")
    return get_fallback_response()