# CONFIGURACIÓN DEL BOT - Variables de entorno y configuraciones globales

import os
from dotenv import load_dotenv

# Cargar variables de entorno desde .env
load_dotenv()

# Token de Telegram
TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN")

# Configuración de logging
LOG_LEVEL = os.getenv("LOG_LEVEL", "INFO")

# Configuración de rutas
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
KNOWLEDGE_BASE_DIR = os.path.join(BASE_DIR, "knowledge_base")
RESPONSES_DIR = os.path.join(BASE_DIR, "responses")
DATA_DIR = os.path.join(BASE_DIR, "data")

# Validar que el token esté presente
if not TELEGRAM_TOKEN:
    raise ValueError("No se encontró TELEGRAM_TOKEN en las variables de entorno")