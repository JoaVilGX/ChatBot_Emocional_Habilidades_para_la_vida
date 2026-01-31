# BOT DE TELEGRAM PRINCIPAL - Integra todos los módulos
# Contenido: Configuración del bot, handlers, y procesamiento de mensajes

import logging
from telegram import Update, ReplyKeyboardMarkup
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes
from search_engine.main_search import main_search_engine
from bot.config import TELEGRAM_TOKEN
from utils.logger import setup_logger

# Configurar logging
setup_logger()
logger = logging.getLogger(__name__)

# COMANDOS DEL BOT
async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Maneja el comando /start - Da la bienvenida"""
    welcome_message = """
    🤖 *Hola! Soy tu asistente académico basado en Habilidades para la Vida*
    
    *Puedo ayudarte con:*
    • Gestión emocional y autoconocimiento
    • Manejo de estrés y ansiedad
    • Toma de decisiones y liderazgo
    • Pensamiento crítico y creativo
    • Trabajo en equipo y resolución de conflictos
    
    *Ejemplos de consultas:*
    - "Tengo mucho estrés con los exámenes"
    - "¿Cómo mejorar mi toma de decisiones?"
    - "Necesito técnicas para hablar en público"
    - "¿Cómo desarrollar pensamiento crítico?"
    
    ¡Escribe tu consulta y te ayudaré!
    """
    
    # Teclado rápido con opciones comunes
    keyboard = [
        ["📚 Estrés académico", "🤝 Trabajo en equipo"],
        ["🎯 Toma de decisiones", "💡 Pensamiento creativo"],
        ["😌 Manejo emocional", "🕐 Gestión del tiempo"]
    ]
    reply_markup = ReplyKeyboardMarkup(keyboard, resize_keyboard=True)
    
    await update.message.reply_text(
        welcome_message,
        parse_mode='Markdown',
        reply_markup=reply_markup
    )
    logger.info(f"Usuario {update.effective_user.id} inició conversación")

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Maneja el comando /help - Muestra ayuda"""
    help_text = """
    *Comandos disponibles:*
    /start - Iniciar conversación
    /help - Esta ayuda
    /temas - Ver temas disponibles
    
    *Puedes preguntar sobre:*
    • *Unidad 1:* Emociones, autoconocimiento, empatía, autoestima
    • *Unidad 2:* Estrés, ansiedad, adaptación, gestión del tiempo
    • *Unidad 3:* Liderazgo, decisiones, trabajo en equipo, conflictos
    • *Unidad 4:* Pensamiento crítico, creatividad, innovación
    
    Ejemplo: "Técnicas para manejar el estrés"
    """
    await update.message.reply_text(help_text, parse_mode='Markdown')

async def temas_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Maneja el comando /temas - Lista temas disponibles"""
    temas_text = """
    *📚 TEMAS DISPONIBLES (basados en PDFs académicos)*
    
    *UNIDAD 1 - INTELIGENCIA EMOCIONAL*
    • Autoconocimiento y gestión emocional
    • Empatía y habilidades sociales
    • Autoestima y mentalidad de crecimiento
    
    *UNIDAD 2 - RESILIENCIA Y MANEJO DE ESTRÉS*
    • Técnicas para estrés y ansiedad
    • Estrategias de afrontamiento
    • Adaptación al cambio
    • Priorización del tiempo
    
    *UNIDAD 3 - LIDERAZGO*
    • Toma de decisiones
    • Manejo de grupos
    • Argumentación y discurso
    • Resolución de conflictos
    • Trabajo en equipo
    
    *UNIDAD 4 - PENSAMIENTO*
    • Pensamiento crítico
    • Pensamiento creativo
    • Desarrollo de creatividad
    
    *PALABRAS CLAVE COMUNES:*
    estrés, ansiedad, decisión, equipo, creatividad, tiempo, conflicto, emociones
    """
    await update.message.reply_text(temas_text, parse_mode='Markdown')

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Procesa todos los mensajes de texto"""
    user_message = update.message.text
    user_id = update.effective_user.id
    
    logger.info(f"Mensaje de {user_id}: {user_message}")
    
    # Mostrar "escribiendo..." mientras procesa
    await context.bot.send_chat_action(
        chat_id=update.effective_chat.id,
        action="typing"
    )
    
    try:
        # Buscar respuesta usando el motor principal
        response = main_search_engine(user_message, str(user_id))
        
        # Enviar respuesta
        await update.message.reply_text(
            response,
            parse_mode='Markdown',
            disable_web_page_preview=True
        )
        
        logger.info(f"Respuesta enviada a {user_id}")
        
    except Exception as e:
        logger.error(f"Error procesando mensaje: {e}")
        await update.message.reply_text(
            "⚠️ *Lo siento, ocurrió un error al procesar tu consulta.*\n\n"
            "Por favor, intenta reformular tu pregunta o usa /help para ver ejemplos.",
            parse_mode='Markdown'
        )

async def error_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Maneja errores del bot"""
    logger.error(f"Error: {context.error}")
    
    if update and update.message:
        await update.message.reply_text(
            "❌ Ocurrió un error inesperado. "
            "El equipo técnico ha sido notificado. "
            "Por favor, intenta nuevamente."
        )

def main():
    """Función principal para iniciar el bot"""
    # Crear aplicación
    application = Application.builder().token(TELEGRAM_TOKEN).build()
    
    # Añadir handlers de comandos
    application.add_handler(CommandHandler("start", start_command))
    application.add_handler(CommandHandler("help", help_command))
    application.add_handler(CommandHandler("temas", temas_command))
    
    # Añadir handler de mensajes
    application.add_handler(MessageHandler(
        filters.TEXT & ~filters.COMMAND,
        handle_message
    ))
    
    # Añadir handler de errores
    application.add_error_handler(error_handler)
    
    # Iniciar bot
    logger.info("🤖 Bot iniciado...")
    print("✅ Bot iniciado. Presiona Ctrl+C para detener.")
    
    application.run_polling(allowed_updates=Update.ALL_TYPES)

if __name__ == "__main__":
    main()