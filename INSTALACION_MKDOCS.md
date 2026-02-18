# 🚀 Guía de Instalación y Uso - MkDocs TICD

## 📦 Instalación Rápida

### Paso 1: Instalar Python

Si no tienes Python instalado:

1. Descarga Python 3.8+ desde [python.org](https://www.python.org/downloads/)
2. Durante la instalación, marca "Add Python to PATH"
3. Verifica: `python --version`

### Paso 2: Instalar MkDocs Material

Abre PowerShell en la carpeta del proyecto y ejecuta:

```powershell
# Opción 1: Instalación directa
pip install mkdocs-material mkdocs-glightbox

# Opción 2: Con entorno virtual (recomendado)
python -m venv .venv
.venv\Scripts\Activate.ps1
pip install mkdocs-material mkdocs-glightbox
```

### Paso 3: Ejecutar el Proyecto

```powershell
# Iniciar servidor de desarrollo
mkdocs serve

# Abre tu navegador en: http://127.0.0.1:8000
```

### Paso 4: Construir para Producción

```powershell
# Generar sitio estático
mkdocs build

# El sitio estará en la carpeta /site
```

---

## 🎯 Qué Está Incluido

### ✅ Totalmente Funcional (60%)

1. **Configuración Profesional**
   - mkdocs.yml completo con Material for MkDocs
   - Tema con modo claro/oscuro
   - Navegación jerárquica con tabs
   - Búsqueda inteligente
   - Todas las extensiones configuradas

2. **Sección de Inicio (100%)**
   - Página principal atra activa
   - Bienvenida al curso
   - Información detallada
   - Requisitos de acceso
   - Estructura del examen
   - Consejos de estudio

3. **Bloque 1 Completo (100%)**
   - 10 archivos Markdown perfectamente estructurados
   - Todo el contenido del HTML original convertido
   - Admonitions profesionales
   - Navegación entre páginas
   - Actividades de autoevaluación

4. **Sistema de Cuestionarios (80%)**
   - Generador HTML integrado
   - Base de 177 preguntas
   - Página principal completa
   - Funcionalidades JavaScript

5. **Assets Personalizados**
   - CSS con estilos del curso
   - JavaScript para interactividad
   - MathJax configurado
   - Animaciones y transiciones

### ⏳ Pendiente (40%)

- **Bloques 2-5**: Por convertir de HTML a Markdown (siguiendo modelo del Bloque 1)
- **Páginas adicionales de cuestionarios**: 5 páginas de documentación
- **Sección de evaluación**: Criterios, ejemplos, autoevaluación
- **Sistema técnico**: Documentación de arquitectura
- **Referencias**: Glosario, enlaces, normativa

---

## 📂 Arquitectura del Proyecto

```
Curso_madurez_TIC/
│
├── mkdocs.yml                         ⭐ Configuración principal
│
├── docs/                              📁 Contenido del sitio
│   ├── index.md                       ⭐ Página principal
│   ├── generador-cuestionarios.html   ⭐ Generador integrado
│   │
│   ├── assets/                        📁 Recursos
│   │   ├── stylesheets/extra.css      ⭐ Estilos personalizados
│   │   ├── javascripts/
│   │   │   ├── mathjax.js             ⭐ Matemáticas
│   │   │   └── cuestionarios.js       ⭐ Funcionalidades
│   │   ├── images/                    📁 Imágenes
│   │   └── base_conocimiento_ticd.json ⭐ Base de datos
│   │
│   ├── inicio/                        ✅ 6 archivos completos
│   ├── modulos/
│   │   ├── index.md                   ✅ Índice de módulos
│   │   ├── bloque1/                   ✅ 10 archivos completos
│   │   ├── bloque2/                   ⏳ Por crear
│   │   ├── bloque3/                   ⏳ Por crear
│   │   ├── bloque4/                   ⏳ Por crear
│   │   └── bloque5/                   ⏳ Por crear
│   │
│   ├── cuestionarios/                 🔄 1 archivo (faltan 5)
│   ├── evaluacion/                    ⏳ Por crear
│   ├── sistema/                       ⏳ Por crear
│   └── referencias/                   ⏳ Por crear
│
└── site/                              📁 Generado por mkdocs build
```

---

## 🎨 Características Destacadas

### Navegación Profesional
- **Tabs superiores** para secciones principales
- **Sidebar** con subsecciones expandibles
- **Breadcrumbs** de localización
- **TOC** integrada en el sidebar
- **Botón "volver arriba"**
- **Navegación footer** entre páginas

### Diseño Moderno
- **Modo claro/oscuro** con toggle
- **Paleta Indigo/Blue** personalizada
- **Hero banner** en homepage con gradientes
- **Cards** con hover effects
- **Tablas estilizadas** con colores corporativos
- **Botones** con gradientes y animaciones
- **Responsive** completo (móvil, tablet, desktop)

### Admonitions Profesionales
```markdown
!!! info "Información"
    Contenido informativo

!!!warning "Advertencia"
    Contenido de precaución

!!! success "Éxito"
    Contenido positivo

!!! danger "Peligro"
    Contenido crítico

!!! example "Ejemplo"
    Ejercicios y actividades

!!! tip "Consejo"
    Sugerencias útiles
```

### Funcionalidades JavaScript
- **Persistencia de checkboxes**: Guarda progreso en localStorage
- **Estadísticas de cuestionarios**: Tracking de rendimiento
- **Exportar/Importar progreso**: Backup de datos
- **Copy-to-clipboard**: En bloques de código
- **Smooth scroll**: Navegación fluida
- **Print-friendly**: Optimizado para impresión

---

## 🚀 Cómo Continuar el Desarrollo

### Opción A: Conversión Manual

1. Abre `Curso_eXeLearning_TICD/bloque2.html`
2. Lee el contenido HTML completo
3. Crea archivos en `docs/modulos/bloque2/` según estructura en mkdocs.yml:
   - `index.md`
   - `proteccion-datos.md`
   - `seguridad-internet.md`
   - etc.
4. Convierte HTML a Markdown:
   - `<h2>` → `##`
   - `<div class="info-box info">` → `!!! info "Título"`
   - Listas, tablas, código
5. Añade navegación al final de cada archivo
6. Repite para bloques 3, 4, 5

### Opción B: Usar IA para Acelerar

Prompt para cada bloque:

```
Lee el archivo completo Curso_eXeLearning_TICD/bloque[X].html y conviértelo a Markdown para MkDocs Material.

Requisitos:
1. Divide en archivos según mkdocs.yml líneas XXX-YYY
2. Convierte HTML a Markdown:
   - Títulos → ##, ###, ####
   - info-box → admonitions (!!! info, !!! warning)
   - Tablas, listas, código
3. Mantén TODO el contenido sin resumir
4. Añade navegación entre páginas
5. Dame el contenido de cada archivo en formato Markdown listo para copiar

Estructura esperada:
docs/modulos/bloque[X]/
  - index.md
  - seccion1.md
  - seccion2.md
  - etc.
```

### Opción C: Script Automatizado (Avanzado)

Crear un script Python que:
1. Lee los HTML con BeautifulSoup
2. Extrae contenido por secciones
3. Convierte a Markdown con regex/herramientas
4. Genera archivos en estructura correcta

---

## 📊 Progreso Actual

```
COMPLETADO:    ████████████░░░░░░░░  60%

Configuración: ████████████████████  100%
Assets:        ████████████████████  100%
Inicio:        ████████████████████  100%
Bloque 1:      ████████████████████  100%
Cuestionarios: ████████████████░░░░   80%
Bloques 2-5:   ░░░░░░░░░░░░░░░░░░░░    0%
Evaluación:    ░░░░░░░░░░░░░░░░░░░░    0%
Sistema:       ░░░░░░░░░░░░░░░░░░░░    0%
Referencias:   ░░░░░░░░░░░░░░░░░░░░    0%
```

---

## 💎 Ventajas del Sistema MkDocs Creado

### Comparado con HTML Original

| Aspecto | HTML Estático | MkDocs Material |
|---------|---------------|-----------------|
| **Navegación** | Menú simple | Navegación jerárquica multi-nivel ✅ |
| **Búsqueda** | No | Búsqueda inteligente con sugerencias ✅ |
| **Responsive** | Básico | Completamente optimizado ✅ |
| **Modo oscuro** | No | Sí, con toggle ✅ |
| **Actualización** | Manual en cada HTML | Centralizada en mkdocs.yml ✅ |
| **SEO** | Básico | Optimizado automáticamente ✅ |
| **Mantenimiento** | Difícil | Fácil con Markdown ✅ |
| **Accesibilidad** | Limitada | Estándares WCAG ✅ |
| **Analytics** | Manual| Fácil integración ✅ |
| **Versiones** | No | Soporte de versiones ✅ |

### Ventajas Adicionales

- ✅ **Markdown es más fácil** de escribir y mantener que HTML
- ✅ **Generación automática** de tabla de contenidos
- ✅ **Enlaces internos verificables** con mkdocs
- ✅ **Build process** que detecta errores
- ✅ **Plugins extensibles** para nuevas funcionalidades
- ✅ **Deploy automático** a GitHub Pages, Netlify, etc.
- ✅ **Offline-ready** con mkdocs build
- ✅ **Print-friendly** optimizado automáticamente

---

## 🎯 Recomendaciones Finales

### Para Completar Rápido (1-2 días)

1. **Prioriza Bloques 2 y 3** (más preguntas en examen)
2. **Usa IA** para conversión HTML → Markdown
3. **Revisa y ajusta** manualmente el resultado
4. **Prueba navegación** después de cada bloque
5. **Build y revisa** el sitio completo

### Para Calidad Máxima (1 semana)

1. **Convierte todos los bloques** con cuidado
2. **Añade imágenes** y diagramas donde ayude
3. **Crea ejercicios interactivos** adicionales
4. **Completa todas las secciones** pendientes
5. **Testing exhaustivo** en todos los dispositivos
6. **Feedback de usuarios** y ajustes

### Mantener a Largo Plazo

1. **Actualiza contenido** cuando cambien regulaciones
2. **Añade nuevas preguntas** de exámenes recientes
3. **Mejora explicaciones** basándote en feedback
4. **Monitoriza analytics** para ver qué se usa más
5. **Actualiza MkDocs Material** periódicamente

---

## 🆘 Troubleshooting

### El sitio no arranca

```powershell
# Verifica instalación
mkdocs --version
pip list | findstr mkdocs

# Reinstala si es necesario
pip install --upgrade mkdocs-material
```

### Enlaces rotos

```powershell
# Build con modo estricto para detectar errores
mkdocs build --strict

# Revisa la salida para ver qué archivos faltan
```

### Estilos no se aplican

- Verifica que `extra.css` está en `docs/assets/stylesheets/`
- Comprueba la ruta en `mkdocs.yml` extra_css
- Limpia caché del navegador (Ctrl+F5)

### JavaScript no funciona

- Abre consola del navegador (F12 → Console)
- Verifica rutas en `extra_javascript` en mkdocs.yml
- Comprueba errores de sintaxis en los .js

---

## 📞 Soporte

- **Documentación MkDocs**: https://www.mkdocs.org/
- **Material for MkDocs**: https://squidfunk.github.io/mkdocs-material/
- **Markdown Guide**: https://www.markdownguide.org/

---

## ✅ Checklist de Finalización

- [x] MkDocs instalado y funcionando
- [x] Servidor de desarrollo arranca correctamente
- [x] Bloque 1 completamente funcional
- [ ] Bloques 2-5 convertidos y probados
- [ ] Todas las páginas de cuestionarios creadas
- [ ] Secciones de evaluación, sistema y referencias completas
- [ ] Enlaces internos verificados
- [ ] Responsive testeado en móvil/tablet
- [ ] Build sin errores: `mkdocs build --strict`
- [ ] Site desplegado y accesible

---

**¡Éxito con tu proyecto MkDocs!** 🚀

Si necesitas ayuda para convertir los bloques restantes, no dudes en solicitar asistencia siguiendo el mismo proceso usado para el Bloque 1.

---

**Creado por**: REA by JaMC  
**Fecha**: Febrero 2026  
**Versión**: 1.0
