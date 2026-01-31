emocional-bot/
├── bot/
│   ├── __init__.py
│   ├── main.py                    # Punto de entrada principal
│   ├── telegram_bot.py            # Configuración específica de Telegram
│   └── config.py                  # Configuración y tokens
├── search_engine/
│   ├── __init__.py
│   ├── main_search.py             # Proceso principal de búsqueda
│   ├── keyword_search.py          # Búsqueda por palabras clave
│   ├── content_search.py          # Búsqueda por contenido/tema
│   ├── emotion_search.py          # Búsqueda emocional (si aplica)
│   └── fallback_search.py         # Respuestas por defecto
├── knowledge_base/
│   ├── __init__.py
│   ├── unidad_1_inteligencia_emocional/
│   │   ├── autoconocimiento.py
│   │   ├── gestion_emociones.py
│   │   ├── empatia.py
│   │   └── autoestima.py
│   ├── unidad_2_resiliencia/
│   │   ├── manejo_estres.py
│   │   ├── estrategias_afrontamiento.py
│   │   ├── adaptacion_cambio.py
│   │   └── priorizacion_tiempo.py
│   ├── unidad_3_liderazgo/
│   │   ├── toma_decisiones.py
│   │   ├── manejo_grupos.py
│   │   ├── argumentacion.py
│   │   ├── trabajo_equipo.py
│   │   └── resolucion_conflictos.py
│   ├── unidad_4_pensamiento/
│   │   ├── pensamiento_critico.py
│   │   └── pensamiento_creativo.py
│   └── keywords_mapping.py        # Mapeo palabras clave → módulos
├── respuestas/
│   ├── __init__.py
│   ├── selector_respuestas.py     # Selecciona 1 de 3 respuestas
│   ├── formatter.py               # Formatea respuestas
│   └── templates.py               # Plantillas de respuesta
├── utils/
│   ├── __init__.py
│   ├── text_processor.py          # Procesamiento de texto
│   ├── logger.py                  # Sistema de logging
│   └── helpers.py                 # Funciones auxiliares
├── data/
│   ├── __init__.py
│   └── extracted_data.json        # Datos extraídos de PDFs
├── requirements.txt
├── .env
└── README.md