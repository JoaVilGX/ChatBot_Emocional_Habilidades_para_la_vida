# 🤖 Asistente Académico - ChatBot_Emocional_Habilidades_para_la_vida

## Objetivo

Construir un robot emocional que analice la situación ingresada por un usuario y brinde recomendaciones para manejar esa emoción de forma adaptativa.

## 📚 Descripción

Bot de Telegram inteligente que funciona como asistente académico para la materia **"Habilidades para la Vida"**. Utiliza contenido estructurado de 4 PDFs académicos para proporcionar respuestas detalladas, personalizadas y basadas en evidencia sobre:

- **Inteligencia Emocional** (Unidad 1)
- **Resiliencia y Manejo de Estrés** (Unidad 2)
- **Liderazgo y Trabajo en Equipo** (Unidad 3)
- **Pensamiento Crítico y Creativo** (Unidad 4)

## ✨ Características Principales

### 🎯 **Sistema de Búsqueda Inteligente**
- **Búsqueda jerárquica**: Palabras clave → Contenido → Análisis emocional
- **3 respuestas diferentes por concepto**: Evita repetición, mantiene frescura
- **Formateo automático**: Emojis, saltos de línea, estructuras claras
- **Respuestas detalladas**: Guías paso a paso, estrategias prácticas, ejemplos concretos

### 📊 **Cobertura Académica Completa**
- **25+ palabras clave principales** extraídas de los PDFs
- **75+ respuestas detalladas** (3 por cada palabra clave)
- **4 unidades académicas** cubiertas exhaustivamente
- **Situaciones específicas**: Exámenes, presentaciones, conflictos, trabajo en equipo

### 💬 **Interacción Natural**
- Comandos simples: `/start`, `/help`, `/temas`
- Teclado rápido con opciones comunes
- Respuestas empáticas y alentadoras
- Formato Markdown para mejor legibilidad

## 🏗️ Estructura del Proyecto

```
emocional-bot/
├── bot/                          # Configuración principal del bot
│   ├── main.py                   # Punto de entrada
│   ├── telegram_bot.py           # Configuración de Telegram
│   └── config.py                 # Variables de entorno
├── search_engine/                # Motor de búsqueda inteligente
│   ├── main_search.py            # Orquestador principal
│   ├── keyword_search.py         # Búsqueda por palabras clave
│   ├── emotion_search.py         # Búsqueda por emociones
│   ├── content_search.py         # Búsqueda semántica
│   └── fallback_search.py        # Respuestas por defecto
├── knowledge_base/               # Base de conocimiento
│   └── keywords_mapping.py       # Mapeo palabras clave
├── responses/                    # Gestión de respuestas
│   ├── response_selector.py      # Selecciona 1 de 3 respuestas
│   ├── formatter.py              # Formatea con emojis y saltos
│   └── templates.py              # Plantillas de respuesta
├── utils/                        # Utilidades
│   ├── text_processor.py         # Procesamiento de texto
│   ├── logger.py                 # Sistema de logging
│   └── helpers.py                # Funciones auxiliares
├── requirements.txt              # Dependencias
├── .env.example                  # Ejemplo de variables
└── README.md                     # Este archivo
```

## 🚀 Instalación y Configuración

### Prerrequisitos
- Python 3.8 o superior
- Cuenta de Telegram
- Token de Bot de Telegram (obtenido de [@BotFather](https://t.me/botfather))

### Paso 1: Clonar el repositorio
```bash
git clone <url-del-repositorio>
cd emocional-bot
```

### Paso 2: Crear entorno virtual
```bash
python -m venv venv
# En Windows:
venv\Scripts\activate
# En Mac/Linux:
source venv/bin/activate
```

### Paso 3: Instalar dependencias
```bash
pip install -r requirements.txt
```

### Paso 4: Configurar variables de entorno
```bash
cp .env.example .env
# Editar .env con tu editor favorito
# Agregar tu token de Telegram: TELEGRAM_TOKEN=tu_token_aqui
```

### Paso 5: Ejecutar el bot
```bash
python -m bot.telegram_bot
```

## 🤖 Uso del Bot

### Comandos Disponibles
| Comando | Descripción | Ejemplo |
|---------|-------------|---------|
| `/start` | Inicia el bot y muestra menú principal | `/start` |
| `/help` | Muestra ayuda y ejemplos de uso | `/help` |
| `/temas` | Lista todos los temas disponibles | `/temas` |

### Palabras Clave Principales
El bot reconoce automáticamente estas palabras clave:

#### 🧠 **Unidad 1: Inteligencia Emocional**
- `autoconocimiento` - Proceso de descubrir tu esencia
- `emociones` - Manejo y regulación emocional
- `empatía` - Comprensión de perspectivas ajenas
- `autoestima` - Construcción de valor personal
- `habilidades sociales` - Conexiones interpersonales

#### ⚡ **Unidad 2: Resiliencia y Manejo de Estrés**
- `estrés` - Técnicas de manejo y transformación
- `ansiedad` - Protocolos para regulación
- `afrontamiento` - Estrategias para desafíos
- `tiempo` - Gestión y priorización efectiva

#### 👑 **Unidad 3: Liderazgo**
- `liderazgo` - Estilos y desarrollo
- `equipo` - Trabajo colaborativo efectivo
- `decisión` - Toma de decisiones estratégicas

#### 💡 **Unidad 4: Pensamiento**
- `pensamiento crítico` - Análisis y evaluación
- `creatividad` - Innovación y generación de ideas

### Ejemplos de Consultas
```
Usuario: "Tengo mucho estrés con los exámenes"
Bot: Respuesta detallada con técnicas de manejo de estrés académico

Usuario: "¿Cómo mejorar mi trabajo en equipo?"
Bot: Guía completa para equipos de alto desempeño

Usuario: "Necesito ser más creativo"
Bot: Programa de 6 semanas para desarrollar creatividad

Usuario: "No puedo tomar decisiones importantes"
Bot: Proceso de 7 pasos para toma de decisiones efectiva
```

## 🔧 Personalización

### Añadir Nuevas Palabras Clave
1. Editar `knowledge_base/detailed_responses.py`
2. Añadir nueva entrada en el diccionario `DETAILED_RESPONSES`
3. Proporcionar 3 respuestas detalladas
4. El sistema automáticamente las integrará

### Modificar Formato de Respuestas
- Editar `responses/formatter.py` para cambiar emojis o estructura
- Modificar `EMOJI_MAP` para personalizar emojis por categoría
- Ajustar métodos de formateo para cambiar saltos de línea

### Expandir Base de Conocimiento
```python
# Ejemplo de añadir nueva palabra clave
"nueva_palabra": [
    """📌 Primera respuesta detallada
    Con saltos de línea y emojis 🎯""",
    """🔍 Segunda respuesta diferente
    Otra perspectiva del mismo tema 💡""",
    """🚀 Tercera respuesta práctica
    Con pasos específicos y ejemplos 📝"""
]
```

## 📊 Estadísticas del Proyecto

| Métrica | Valor |
|---------|-------|
| Palabras clave principales | 25+ |
| Respuestas detalladas | 75+ (3 por palabra clave) |
| Unidades académicas cubiertas | 4 |
| Situaciones específicas | 10+ |
| Líneas de código | ~2000 |
| Emojis utilizados | 50+ |

## 🤝 Contribución

Las contribuciones son bienvenidas. Por favor:

1. Haz fork del repositorio
2. Crea una rama para tu feature (`git checkout -b feature/AmazingFeature`)
3. Commit tus cambios (`git commit -m 'Add some AmazingFeature'`)
4. Push a la rama (`git push origin feature/AmazingFeature`)
5. Abre un Pull Request

### Áreas para Contribuir
- **Nuevas palabras clave**: Expansión de la base de conocimiento
- **Mejoras en búsqueda**: Algoritmos más inteligentes
- **Traducciones**: Soporte para otros idiomas
- **Interfaz**: Mejoras en la experiencia de usuario

## 👥 Créditos

### Desarrollo
- **Desarrollador Principal**: Joaquin Villacreses Moreno

### Fuentes Académicas
El bot utiliza contenido académico estructurado de:
1. **Unidad 1**: Inteligencia Emocional - Autoconocimiento, gestión emocional, empatía
2. **Unidad 2**: Resiliencia y Manejo de Estrés - Estrategias, adaptación, tiempo
3. **Unidad 3**: Liderazgo - Toma de decisiones, trabajo en equipo, conflictos
4. **Unidad 4**: Pensamiento Crítico y Creativo - Análisis, innovación, solución de problemas

### Agradecimientos
- **Telegram** por la plataforma de bots
- **Python-telegram-bot** por la excelente librería
- **Comunidad académica** por el contenido de habilidades para la vida

## 🔗 Enlaces Útiles

- [Documentación de python-telegram-bot](https://python-telegram-bot.org/)
- [Crear un bot en Telegram](https://core.telegram.org/bots#3-how-do-i-create-a-bot)
- [Guía de Markdown para Telegram](https://core.telegram.org/bots/api#markdownv2-style)

## 📞 Soporte

Si encuentra problemas o tiene preguntas:
1. **Email**: JoaquinVillita2006@gmail.com
2. **Telegram**: @Joaquin V

---

**✨ ¡Disfruta aprendiendo y desarrollando tus habilidades para la vida con nuestro asistente académico!** 🎓