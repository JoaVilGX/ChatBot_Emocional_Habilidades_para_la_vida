# PLANTILLAS DE RESPUESTA - Estructuras predefinidas para diferentes tipos de respuesta

def template_step_by_step(steps: list, title: str = "Pasos a seguir:") -> str:
    """
    Crea una respuesta de tipo paso a paso.
    
    Args:
        steps: Lista de pasos
        title: Título de la sección
        
    Returns:
        Respuesta formateada
    """
    response = f"📋 *{title}*\n\n"
    
    for i, step in enumerate(steps, 1):
        response += f"{i}. {step}\n"
    
    response += "\n▶️ Sigue estos pasos en orden para mejores resultados."
    return response

def template_technique(name: str, description: str, steps: list = None) -> str:
    """
    Crea una respuesta para describir una técnica específica.
    
    Args:
        name: Nombre de la técnica
        description: Descripción breve
        steps: Pasos para aplicar la técnica (opcional)
        
    Returns:
        Respuesta formateada
    """
    response = f"🔧 *Técnica: {name}*\n\n"
    response += f"{description}\n\n"
    
    if steps:
        response += "*Cómo aplicarla:*\n"
        for i, step in enumerate(steps, 1):
            response += f"{i}. {step}\n"
    
    return response

def template_encouragement(problem: str, advice: str, action: str = "") -> str:
    """
    Crea un mensaje de aliento y apoyo.
    
    Args:
        problem: Descripción del problema
        advice: Consejo principal
        action: Acción recomendada (opcional)
        
    Returns:
        Mensaje formateado
    """
    response = f"🤗 *Entiendo que estás enfrentando: {problem}*\n\n"
    response += f"💡 *Mi consejo:* {advice}\n\n"
    
    if action:
        response += f"🚀 *Acción sugerida:* {action}\n\n"
    
    response += "Recuerda que es normal enfrentar desafíos y que cada paso, por pequeño que sea, te acerca a una solución."
    return response

def template_informative(topic: str, information: str, key_points: list = None) -> str:
    """
    Crea una respuesta informativa sobre un tema.
    
    Args:
        topic: Tema principal
        information: Información detallada
        key_points: Puntos clave (opcional)
        
    Returns:
        Respuesta formateada
    """
    response = f"📚 *Información sobre: {topic}*\n\n"
    response += f"{information}\n\n"
    
    if key_points:
        response += "*Puntos clave:*\n"
        for point in key_points:
            response += f"• {point}\n"
    
    return response