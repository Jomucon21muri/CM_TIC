# 📚 Sistema de Base de Conocimiento y Cuestionarios TICD

Sistema completo para gestionar y generar cuestionarios aleatorios basados en preguntas de exámenes de Tratamiento de la Información y Competencia Digital (TICD).

## 🎯 Características

- **Base de conocimiento organizada por módulos**: 9 módulos temáticos + categoría general
- **177 preguntas extraídas** de exámenes de diferentes años (2016-2025)
- **Explicaciones educativas detalladas** para cada respuesta
- **Generador de cuestionarios aleatorios** con interfaz web interactiva
- **Resultados detallados** con porcentaje de acierto y feedback inmediato

## 📋 Módulos Disponibles

1. **Hardware y Arquitectura** (38 preguntas) - Memoria, procesadores, periféricos, almacenamiento
2. **Redes e Internet** (42 preguntas) - Protocolos, direcciones IP, DNS, tipos de redes
3. **Seguridad Informática** (9 preguntas) - Virus, spam, phishing, criptografía
4. **Software y Sistemas Operativos** (14 preguntas) - Funciones, tipos, gestión
5. **Ofimática** (28 preguntas) - Procesadores de texto, hojas de cálculo, presentaciones
6. **Bases de Datos** (7 preguntas) - SGBD, estructuras, claves
7. **Multimedia** (17 preguntas) - Formatos de imagen, audio, vídeo
8. **Web 2.0 y Redes Sociales** (14 preguntas) - Comunidades virtuales, blogs, wikis
9. **Licencias y Derechos** (5 preguntas) - Creative Commons, copyright
10. **General** (41 preguntas) - Preguntas multidisciplinares

## 🚀 Cómo Usar

### 1. Generar/Actualizar la Base de Conocimiento

Si necesitas regenerar la base de conocimiento desde los PDFs:

```bash
# Extraer texto de los PDFs (ya hecho)
python extraer_preguntas.py
python extraer_soluciones.py

# Crear la base de conocimiento
python crear_base_conocimiento.py

# Enriquecer con explicaciones detalladas
python enriquecer_explicaciones.py
```

Esto generará el archivo `base_conocimiento_ticd.json`.

### 2. Usar el Generador de Cuestionarios

Abre el archivo `generador_cuestionarios.html` en tu navegador web:

1. **Selecciona un módulo** (o "Todos los módulos" para pregunta aleatoria)
2. **Indica el número de preguntas** que deseas (5-30)
3. **Haz clic en "Generar Cuestionario"**
4. **Responde las preguntas** seleccionando una opción
5. **Verifica tus respuestas** para ver el resultado y las explicaciones

## 📁 Estructura de Archivos

```
Curso_madurez_TIC/
├── test/                           # PDFs originales de tests
│   ├── 001 - PAGS_TICD_junio2016.pdf
│   ├── 002 - PAGS_TICD_junio2017.pdf
│   └── ...
├── soluciones/                     # PDFs con soluciones
│   ├── 001 - SOL.PAGS_TICD_junio2016.pdf
│   └── ...
├── preguntas_extraidas/            # Texto extraído de PDFs
│   ├── 001 - PAGS_TICD_junio2016.txt
│   └── ...
├── base_conocimiento_ticd.json     # Base de datos de preguntas
├── generador_cuestionarios.html    # Aplicación web interactiva
├── extraer_preguntas.py            # Extrae PDFs de tests
├── extraer_soluciones.py           # Extrae PDFs de soluciones
├── crear_base_conocimiento.py      # Crea la base de conocimiento
├── enriquecer_explicaciones.py     # Añade explicaciones detalladas
└── README_CUESTIONARIOS.md         # Este archivo
```

## 🔧 Tecnologías Utilizadas

- **Python 3.13** para procesamiento de PDFs y generación de base de conocimiento
- **PyPDF2** para extracción de texto de PDFs
- **HTML5/CSS3/JavaScript** para la interfaz web
- **JSON** para almacenamiento de datos

## 📊 Formato de la Base de Conocimiento

```json
{
  "modulos": {
    "hardware": {
      "nombre": "Hardware y Arquitectura",
      "keywords": ["memoria", "CPU", "periférico", ...]
    },
    ...
  },
  "preguntas": [
    {
      "id": "2016_1",
      "año": "2016",
      "numero_original": 1,
      "pregunta": "Diez KB son:",
      "opciones": {
        "a": "12400 bites",
        "b": "10240 bytes",
        "c": "10,00 bytes",
        "d": "1.000.000 bytes"
      },
      "respuesta_correcta": "b",
      "explicacion": "La respuesta correcta es 'b': 10240 bytes. En informática, 1 KB = 1024 bytes...",
      "modulos": ["hardware"]
    },
    ...
  ]
}
```

## ✨ Características del Generador Web

- **Interfaz moderna y responsive** adaptada a móviles y tablets
- **Selección por módulo** para practicar temas específicos
- **Número configurable de preguntas** (5-30)
- **Feedback inmediato** al verificar respuestas
- **Explicaciones educativas** para cada respuesta
- **Estadísticas detalladas** (correctas, incorrectas, sin responder)
- **Indicadores visuales** de respuestas correctas/incorrectas
- **Animaciones suaves** para mejor experiencia de usuario

## 🎓 Uso Educativo

Este sistema está diseñado para:

1. **Autoevaluación** de estudiantes preparando exámenes TICD
2. **Práctica por módulos** para reforzar áreas específicas
3. **Aprendizaje activo** con explicaciones detalladas
4. **Seguimiento de progreso** mediante estadísticas

## 🔄 Actualización y Mantenimiento

### Añadir nuevos exámenes:

1. Coloca el PDF del test en la carpeta `test/`
2. Coloca el PDF de soluciones en la carpeta `soluciones/`
3. Ejecuta los scripts de extracción y generación

### Mejorar explicaciones:

Edita el archivo `enriquecer_explicaciones.py` y añade nuevas entradas en el diccionario `EXPLICACIONES_TEMATICAS`.

### Ajustar clasificación de módulos:

Edita el diccionario `MODULOS` en `crear_base_conocimiento.py` para añadir nuevas palabras clave o módulos.

## 📝 Estadísticas Actuales

- **Total de preguntas**: 177
- **Años cubiertos**: 2016-2025
- **Preguntas con explicaciones**: 170 (96%)
- **Módulos temáticos**: 9 + general

## 🤝 Contribuciones

Para mejorar el sistema:

1. Añade más patrones de explicación en `enriquecer_explicaciones.py`
2. Mejora el parsing de PDFs en `crear_base_conocimiento.py`
3. Añade nuevas características al generador web
4. Reporta errores en clasificación de preguntas

## 📧 Soporte

Para preguntas o mejoras, contacta con el administrador del curso.

---

**Versión**: 1.0  
**Fecha**: Febrero 2026  
**Licencia**: Uso educativo
