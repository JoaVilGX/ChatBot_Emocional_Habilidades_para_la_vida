# SISTEMA DE LOGGING - Configuración centralizada de logs

import logging
import sys
from bot.config import LOG_LEVEL

def setup_logger():
    """
    Configura el logger global para la aplicación.
    """
    # Definir nivel de log
    log_level = getattr(logging, LOG_LEVEL.upper(), logging.INFO)
    
    # Configurar formato
    log_format = "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
    
    # Configurar handlers
    handlers = []
    
    # Handler para consola
    console_handler = logging.StreamHandler(sys.stdout)
    console_handler.setFormatter(logging.Formatter(log_format))
    handlers.append(console_handler)
    
    # Configurar logging básico
    logging.basicConfig(
        level=log_level,
        format=log_format,
        handlers=handlers
    )
    
    # Reducir log de algunas librerías
    logging.getLogger("httpx").setLevel(logging.WARNING)
    logging.getLogger("telegram").setLevel(logging.WARNING)
    
    logger = logging.getLogger(__name__)
    logger.info(f"Logger configurado con nivel: {LOG_LEVEL}")
    
    return logger