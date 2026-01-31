# FORMATEADOR DE RESPUESTAS - Da formato consistente a las respuestas

def format_response(response: str) -> str:
    """
    Formatea una respuesta para hacerla más legible y atractiva.
    Añade emojis y asegura saltos de línea adecuados.

    Args:
        response: La respuesta en texto plano

    Returns:
        La respuesta formateada con emojis y saltos de línea
    """
    # Diccionario de palabras clave a emojis
    emoji_map = {
        'estrés': '😰',
        'ansiedad': '😥',
        'respiración': '🌬️',
        'tiempo': '⏰',
        'planificar': '📅',
        'equipo': '👥',
        'liderazgo': '🌟',
        'decisión': '🤔',
        'conflicto': '⚔️',
        'creatividad': '💡',
        'pensamiento': '🧠',
        'emociones': '😊',
        'autoconocimiento': '👁️',
        'empatía': '🤝',
        'autoestima': '💪',
        'resiliencia': '🛡️',
        'adaptación': '🔄',
        'técnica': '🔧',
        'paso': '👣',
        'importante': '❗',
        'ejemplo': '📌',
        'recomendación': '✅',
        'atención': '⚠️',
        'éxito': '🎉',
        'error': '❌',
        'pregunta': '❓',
        'idea': '💭',
        'proyecto': '📁',
        'meta': '🎯',
        'motivación': '🚀',
        'aprendizaje': '📚',
        'cambio': '🔄',
        'descanso': '😴',
        'salud': '💚',
        'mente': '🧘',
        'cuerpo': '💪',
        'alimento': '🍎',
        'ejercicio': '🏃',
        'sueño': '😴',
        'organización': '🗂️',
        'prioridad': '🔝',
        'proactivo': '⚡',
        'comunicación': '📢',
        'escucha': '👂',
        'hablar': '🗣️',
        'presentación': '📊',
        'examen': '📝',
        'universidad': '🎓',
        'trabajo': '💼',
        'familia': '👨‍👩‍👧‍👦',
        'amigos': '👫',
        'apoyo': '🤗',
        'soledad': '😔',
        'felicidad': '😄',
        'tristeza': '😢',
        'enojo': '😠',
        'miedo': '😨',
        'calma': '😌',
        'paz': '☮️',
        'amor': '❤️',
        'victoria': '🏆',
        'derrota': '💔',
        'inteligencia': '🧠',
        'sabiduría': '📜',
        'conocimiento': '🎓',
        'habilidad': '🛠️',
        'práctica': '🔁',
        'perseverancia': '⛰️',
        'disciplina': '✊',
        'confianza': '🤝',
        'honestidad': '📏',
        'transparencia': '🔍',
        'justicia': '⚖️',
        'colaboración': '🤲',
        'innovación': '🚀',
        'tecnología': '📱',
        'futuro': '🔮',
        'presente': '🕐',
        'pasado': '🕰️',
    }

    # Añadir emojis a palabras clave (sin alterar la estructura del texto)
    for palabra, emoji in emoji_map.items():
        if palabra in response.lower():
            # Solo añadir el emoji la primera vez que aparece
            if emoji not in response:
                response = response.replace(palabra, f"{palabra} {emoji}")
                # También para mayúsculas
                response = response.replace(palabra.capitalize(), f"{palabra.capitalize()} {emoji}")

    # Asegurar saltos de línea para listas numeradas
    lines = response.split('\n')
    formatted_lines = []
    for line in lines:
        # Si la línea empieza con un número o un guion, añadir un salto de línea antes (excepto la primera)
        if line.strip().startswith(('-', '*', '•', '1.', '2.', '3.', '4.', '5.', '6.', '7.', '8.', '9.', '10.')):
            formatted_lines.append('\n' + line)
        else:
            formatted_lines.append(line)

    response = '\n'.join(formatted_lines)

    # Asegurar que los puntos y aparte tengan doble salto de línea
    response = response.replace('. ', '.\n\n')

    # Eliminar dobles saltos de línea excesivos
    while '\n\n\n' in response:
        response = response.replace('\n\n\n', '\n\n')

    return response.strip()

def add_source_to_response(response: str, source: str) -> str:
    """
    Añade la fuente de la información a la respuesta.
    
    Args:
        response: Respuesta formateada
        source: Fuente de la información
        
    Returns:
        Respuesta con fuente añadida
    """
    if source:
        return f"{response}\n\n📖 *Fuente:* {source}"
    return response

def format_list_response(items: list, title: str = "") -> str:
    """
    Formatea una lista de elementos.
    
    Args:
        items: Lista de elementos
        title: Título opcional
        
    Returns:
        Texto formateado
    """
    if not items:
        return ""
    
    formatted = f"{title}\n" if title else ""
    
    for i, item in enumerate(items, 1):
        formatted += f"{i}. {item}\n"
    
    return formatted.strip()