# 🚀 INICIO RÁPIDO - Generador de Cuestionarios TICD

## Opción 1: Usar Script de Python (Recomendado)

Ejecuta este comando en PowerShell desde la carpeta del proyecto:

```powershell
python iniciar_cuestionarios.py
```

O con el entorno virtual:

```powershell
& ".venv/Scripts/python.exe" iniciar_cuestionarios.py
```

## Opción 2: Abrir Directamente el HTML

1. Navega a la carpeta del proyecto
2. **Doble clic en**: `generador_cuestionarios.html`
3. Se abrirá en tu navegador predeterminado

## 📱 Uso del Generador

### Paso 1: Configurar
- **Módulo**: Selecciona un tema específico o "Todos los módulos"
- **Preguntas**: Elige entre 5 y 30 preguntas
- Haz clic en **"Generar Cuestionario"**

### Paso 2: Responder
- Lee cada pregunta
- Marca la opción que consideres correcta (a, b, c, d)
- Puedes cambiar respuestas antes de verificar

### Paso 3: Verificar
- Haz clic en **"Verificar Respuestas"**
- Verás:
  - ✅ Correctas en verde
  - ❌ Incorrectas en rojo
  - 💡 Explicación de cada respuesta
  - 📊 Estadísticas finales

### Paso 4: Repetir
- **"Nuevo Cuestionario"** para practicar más

## 📂 Archivos Principales

- `generador_cuestionarios.html` - **ABRE ESTE ARCHIVO** para usar el generador
- `base_conocimiento_ticd.json` - Base de datos de preguntas
- `iniciar_cuestionarios.py` - Script de inicio rápido
- `README_CUESTIONARIOS.md` - Documentación completa
- `RESUMEN_SISTEMA.md` - Resumen técnico

## 🎯 Módulos Disponibles

1. **Hardware y Arquitectura** - Memoria, procesadores, periféricos
2. **Redes e Internet** - Protocolos, IP, conexiones
3. **Seguridad Informática** - Virus, spam, protección
4. **Software y Sistemas Operativos** - Windows, Linux, gestión
5. **Ofimática** - Word, Excel, presentaciones
6. **Bases de Datos** - SGBD, tablas, claves
7. **Multimedia** - Imágenes, audio, vídeo
8. **Web 2.0 y Redes Sociales** - Blogs, wikis, comunidades
9. **Licencias y Derechos** - Creative Commons, copyright

## ⚙️ Requisitos

- **Navegador moderno**: Chrome, Firefox, Safari, Edge (últimas versiones)
- **Sin conexión a Internet necesaria** - Funciona completamente offline
- **Sin instalación** - Solo abre el archivo HTML

## 💡 Consejos

- **Practica por módulos** si tienes dudas en temas específicos
- **Usa 10-15 preguntas** para sesiones de estudio cortas
- **Lee las explicaciones** para aprender de los errores
- **Repite cuestionarios** hasta dominar todos los temas
- **Mezcla todos los módulos** para preparación completa

## 🆘 Solución de Problemas

### El generador no carga
- Asegúrate de que `base_conocimiento_ticd.json` está en la misma carpeta
- Prueba con otro navegador
- Verifica que no hay bloqueadores de JavaScript

### No se muestran las preguntas
- Revisa la consola del navegador (F12) para ver errores
- Verifica que el archivo JSON es válido

### Las explicaciones no aparecen
- Haz clic en "Verificar Respuestas" primero
- Las explicaciones solo se muestran después de verificar

## 📞 Soporte

Para problemas o mejoras:
1. Revisa `README_CUESTIONARIOS.md` para documentación completa
2. Ejecuta `python verificar_base_conocimiento.py` para diagnóstico

---

**¡Todo listo para empezar a practicar! 🎓**

Simplemente abre `generador_cuestionarios.html` y comienza tu autoevaluación.
