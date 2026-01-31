# BÚSQUEDA POR CONTENIDO/TEMA - Análisis semántico
# Contenido: Estrategias, técnicas, situaciones específicas

from typing import Optional, List
import re

def search_by_content(user_message: str) -> Optional[List[str]]:
    """
    Busca por contenido o tema basado en análisis de contexto.
    Usa patrones y frases comunes para identificar temas.
    
    Args:
        user_message: Mensaje del usuario
        
    Returns:
        Lista de respuestas o None
    """
    message_lower = user_message.lower()
    
    # PATRONES PARA TÉCNICAS ESPECÍFICAS (UNIDAD 2)
    if re.search(r'(respirar|respiración|calmar|tranquilizar)', message_lower):
        return get_breathing_techniques()
    
    if re.search(r'(organizar|tiempo|planificar|priorizar|horario)', message_lower):
        return get_time_management_responses()
    
    if re.search(r'(conflicto|pelea|disputa|desacuerdo|problema interpersonal)', message_lower):
        return get_conflict_resolution_responses()
    
    # PATRONES PARA SITUACIONES ACADÉMICAS
    if re.search(r'(examen|prueba|evaluación|calificación|test|final)', message_lower):
        return get_exam_stress_responses()
    
    if re.search(r'(presentación|exponer|hablar público|oratoria|discurso)', message_lower):
        return get_public_speaking_responses()
    
    # PATRONES PARA RELACIONES INTERPERSONALES
    if re.search(r'(amigo|compañero|relación|comunicar|pareja|familia|social)', message_lower):
        return get_relationship_responses()
    
    # PATRONES PARA LIDERAZGO
    if re.search(r'(liderar|equipo|grupo|coordinación|delegar|motivar)', message_lower):
        return get_leadership_responses()
    
    # PATRONES PARA CREATIVIDAD
    if re.search(r'(creativo|innovación|idea|solucionar problema|brainstorming)', message_lower):
        return get_creativity_responses()
    
    # PATRONES PARA TOMA DE DECISIONES
    if re.search(r'(decidir|decisión|elegir|opción|alternativa)', message_lower):
        return get_decision_making_responses()
    
    return None

def get_breathing_techniques() -> List[str]:
    """Respuestas sobre técnicas de respiración - Unidad 2, Tema 1"""
    return [
        "TÉCNICA 4-7-8: Inhala por 4 segundos, mantén 7 segundos, exhala por 8 segundos. Repite 4 veces. Ideal para ansiedad aguda.",
        "RESPIRACIÓN DIAFRAGMÁTICA: Coloca una mano en el pecho y otra en el abdomen. Al inhalar, el abdomen debe expandirse. Practica 5 minutos diarios.",
        "RESPIRACIÓN CUADRADA: 4 segundos inhalando, 4 sosteniendo, 4 exhalando, 4 en pausa. Excelente para restaurar calma y concentración."
    ]

def get_time_management_responses() -> List[str]:
    """Respuestas sobre gestión del tiempo - Unidad 2, Tema 2"""
    return [
        "MATRIZ DE EISENHOWER: Clasifica tareas en: 1) Urgente/Importante (haz ahora) 2) Importante/No urgente (programa) 3) Urgente/No importante (delega) 4) Ni urgente ni importante (elimina).",
        "TÉCNICA POMODORO: Trabaja 25 minutos, descansa 5. Cada 4 pomodoros, descansa 15-30 minutos. Mejora concentración y previene agotamiento.",
        "PLANIFICACIÓN SEMANAL: Dedica 30 minutos cada domingo para planificar la semana. Establece 3 metas principales por día y bloquea tiempo para ellas."
    ]

def get_conflict_resolution_responses() -> List[str]:
    """Respuestas sobre resolución de conflictos - Unidad 3, Tema 1"""
    return [
        "PASOS PARA RESOLVER CONFLICTOS: 1) Escucha activa 2) Identifica intereses (no posiciones) 3) Genera opciones win-win 4) Acuerda solución específica 5) Implementa y evalúa.",
        "COMUNICACIÓN ASERTIVA EN CONFLICTOS: Usa 'Yo' no 'Tú'. Ej: 'Yo me siento X cuando Y, me gustaría Z' en lugar de 'Tú siempre haces...'. Evita generalizaciones.",
        "MEDIACIÓN EFECTIVA: Neutral, escucha ambas partes, clarifica malentendidos, busca puntos comunes, facilita acuerdo mutuo, sigue implementación."
    ]

def get_exam_stress_responses() -> List[str]:
    """Respuestas sobre estrés en exámenes - Unidad 2 aplicado a contexto académico"""
    return [
        "ESTRATEGIAS PARA EXÁMENES: 1) Planifica estudio con tiempo 2) Usa técnicas activas (resúmenes, tests, enseñar a otros) 3) Practica en condiciones similares al examen 4) Cuida sueño y alimentación.",
        "MANEJO DE ANSIEDAD EN EXÁMENES: La noche anterior: revisión ligera, cena balanceada, sueño de 7-8 horas. Día del examen: desayuno proteico, llegada temprana, respiración calmante antes de empezar.",
        "DURANTE EL EXAMEN: Lee todas las preguntas primero, empieza por las fáciles, gestiona tiempo (ej: 1 minuto por punto), si te bloqueas pasa a otra y regresa después, revisa al final."
    ]

def get_public_speaking_responses() -> List[str]:
    """Respuestas sobre hablar en público - Unidad 3 (comunicación)"""
    return [
        "PRESENTACIONES EFECTIVAS: Estructura: apertura impactante (30%), desarrollo claro (50%), conclusión memorable (20%). Practica en voz alta 3 veces mínimo.",
        "MIEDO ESCÉNICO: 1) Visualiza éxito 2) Respiración diafragmática 3) Enfócate en mensaje, no en audiencia 4) Usa notas de apoyo 5) Practica con amigos 6) Comienza con anécdota personal.",
        "COMUNICACIÓN NO VERBAL: Postura abierta, contacto visual distribuido, gestos naturales, tono de voz variado, sonrisa genuina, movimiento apropiado, vestimenta adecuada."
    ]

def get_relationship_responses() -> List[str]:
    """Respuestas sobre relaciones interpersonales - Unidad 1, Tema 2"""
    return [
        "HABILIDADES SOCIALES: Escucha activa, comunicación asertiva, empatía, respeto, manejo de emociones en interacciones. Practica en situaciones de bajo riesgo primero.",
        "EMPATÍA EN RELACIONES: Escucha sin juzgar, valida emociones del otro ('entiendo que te sientas...'), pregunta abiertamente, ofrece apoyo específico, respeta diferencias.",
        "COMUNICACIÓN ASERTIVA: Expresa necesidades claramente sin agresividad ni pasividad. Usa frases como 'Me gustaría...', 'Necesito...', 'Me siento... cuando...'."
    ]

def get_leadership_responses() -> List[str]:
    """Respuestas sobre liderazgo - Unidad 3"""
    return [
        "LIDERAZGO EFECTIVO: Inspirar visión, comunicar claramente, delegar adecuadamente, motivar equipo, resolver conflictos, tomar decisiones informadas, dar feedback constructivo.",
        "TRABAJO EN EQUIPO: Roles claros, objetivos compartidos, comunicación abierta, confianza mutua, diversidad valorada, resolución colaborativa, celebración de logros.",
        "DELEGACIÓN EFECTIVA: 1) Define tarea claramente 2) Escoge persona adecuada 3) Proporciona recursos 4) Establece expectativas 5) Da autonomía 6) Supervisa sin microgestionar 7) Reconoce esfuerzo."
    ]

def get_creativity_responses() -> List[str]:
    """Respuestas sobre creatividad - Unidad 4"""
    return [
        "DESARROLLO CREATIVO: Brainstorming sin juicios, mapas mentales, pensamiento lateral, asociaciones libres, role-playing, desafíos creativos, exposición a diversas experiencias.",
        "PENSAMIENTO LATERAL: Romper patrones establecidos. Técnicas: provocación, cambio de enfoque, analogías, preguntas '¿Qué pasaría si...?', invertir problema.",
        "AMBIENTE CREATIVO: Espacio sin juicios, tiempo para incubación, diversidad de perspectivas, recursos disponibles, tolerancia al error, celebración de ideas novedosas."
    ]

def get_decision_making_responses() -> List[str]:
    """Respuestas sobre toma de decisiones - Unidad 3, Tema 2"""
    return [
        "PROCESO DECISIONAL: 1) Define problema 2) Recopila datos 3) Identifica causa raíz 4) Genera alternativas 5) Evalúa opciones 6) Elige 7) Implementa 8) Evalúa resultados.",
        "MÉTODO 5 WHYS: Pregunta '¿Por qué?' 5 veces para encontrar causa raíz. Ejemplo: Ventas bajas → menos clientes → competencia mejor → falta innovación → recursos insuficientes.",
        "EVALUACIÓN DE ALTERNATIVAS: Usa criterios SMART: Específico, Medible, Alcanzable, Relevante, Temporal. Considera pros/contras, recursos, riesgos y alineación con objetivos."
    ]