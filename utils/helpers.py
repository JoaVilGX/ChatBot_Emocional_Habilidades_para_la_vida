# FUNCIONES AUXILIARES - Utilidades generales para toda la aplicación

import random
import time
from typing import List, Any, Dict

def get_random_item(items: List[Any]) -> Any:
    """
    Devuelve un elemento aleatorio de una lista.
    
    Args:
        items: Lista de elementos
        
    Returns:
        Elemento aleatorio o None si la lista está vacía
    """
    if not items:
        return None
    return random.choice(items)

def chunk_list(lst: List[Any], chunk_size: int) -> List[List[Any]]:
    """
    Divide una lista en chunks del tamaño especificado.
    
    Args:
        lst: Lista a dividir
        chunk_size: Tamaño de cada chunk
        
    Returns:
        Lista de chunks
    """
    return [lst[i:i + chunk_size] for i in range(0, len(lst), chunk_size)]

def safe_get(dictionary: Dict, keys: List[str], default: Any = None) -> Any:
    """
    Obtiene un valor de un diccionario de forma segura,
    manejando claves anidadas.
    
    Args:
        dictionary: Diccionario base
        keys: Lista de claves (para acceso anidado)
        default: Valor por defecto si no se encuentra
        
    Returns:
        Valor encontrado o default
    """
    current = dictionary
    for key in keys:
        if isinstance(current, dict) and key in current:
            current = current[key]
        else:
            return default
    return current

def measure_time(func):
    """
    Decorador para medir el tiempo de ejecución de una función.
    """
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"⏱️  {func.__name__} tomó {end_time - start_time:.4f} segundos")
        return result
    return wrapper

def validate_message_length(message: str, max_length: int = 4096) -> bool:
    """
    Valida que un mensaje no exceda la longitud máxima permitida.
    
    Args:
        message: Mensaje a validar
        max_length: Longitud máxima permitida
        
    Returns:
        True si el mensaje es válido, False si es demasiado largo
    """
    return len(message) <= max_length

def truncate_message(message: str, max_length: int = 4096, suffix: str = "...") -> str:
    """
    Trunca un mensaje si excede la longitud máxima.
    
    Args:
        message: Mensaje a truncar
        max_length: Longitud máxima permitida
        suffix: Sufijo a añadir si se trunca
        
    Returns:
        Mensaje truncado si es necesario
    """
    if len(message) <= max_length:
        return message
    
    return message[:max_length - len(suffix)] + suffix