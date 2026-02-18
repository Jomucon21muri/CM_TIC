# 📦 Cómo Crear el Paquete SCORM del Curso TICD

## 🎯 ¿Qué es SCORM?

SCORM (Sharable Content Object Reference Model) es un estándar para empaquetar contenido educativo que permite:
- Importar el curso en plataformas LMS (Moodle, Aules, Blackboard, Canvas, etc.)
- Seguimiento del progreso del estudiante
- Registro de puntuaciones
- Compatibilidad entre diferentes sistemas

## 📋 Archivos Creados

Ya se han creado los archivos necesarios para SCORM:

✅ **imsmanifest.xml** - Archivo principal del paquete SCORM
✅ **scorm_api.js** - API para comunicación con el LMS

## 🚀 Pasos para Crear el Paquete SCORM

### Opción 1: Crear Manualmente (Recomendado)

#### Paso 1: Preparar los Archivos

Asegúrate de que la carpeta `Curso_eXeLearning_TICD` contiene:

```
Curso_eXeLearning_TICD/
├── imsmanifest.xml          ← Creado ✅
├── scorm_api.js             ← Creado ✅
├── index.html
├── bloque1.html
├── bloque2.html
├── bloque3.html
├── bloque4.html
├── bloque5.html
├── evaluacion.html
├── generador_cuestionarios.html
├── base_conocimiento_ticd.json
├── css/
│   └── style.css
├── images/ (si existe)
└── js/ (si existe)
```

#### Paso 2: Añadir Script SCORM a los HTML (Opcional)

Para habilitar seguimiento avanzado, añade esta línea al `<head>` de cada archivo HTML:

```html
<script src="scorm_api.js"></script>
```

#### Paso 3: Crear el Archivo ZIP

**En Windows (PowerShell):**

```powershell
# Navegar a la carpeta padre
cd "c:\Users\muril\OneDrive - Conselleria d'Educació\Curso_madurez_TIC"

# Crear el archivo ZIP
Compress-Archive -Path ".\Curso_eXeLearning_TICD\*" -DestinationPath ".\TICD_SCORM_Package.zip" -Force
```

**Importante:** El archivo ZIP debe contener los archivos directamente en la raíz, NO dentro de una subcarpeta.

#### Paso 4: Verificar el Paquete

Abre el archivo ZIP y verifica que:
- ✅ `imsmanifest.xml` está en la raíz del ZIP
- ✅ Todos los archivos HTML están en la raíz
- ✅ Las carpetas `css/`, `images/`, `js/` están presentes
- ✅ NO hay una carpeta adicional conteniendo todo

### Opción 2: Script Automático

Puedes ejecutar este script de PowerShell:

```powershell
# Script para crear paquete SCORM
$cursoPath = "c:\Users\muril\OneDrive - Conselleria d'Educació\Curso_madurez_TIC\Curso_eXeLearning_TICD"
$outputPath = "c:\Users\muril\OneDrive - Conselleria d'Educació\Curso_madurez_TIC\TICD_SCORM_Package.zip"

# Eliminar ZIP anterior si existe
if (Test-Path $outputPath) {
    Remove-Item $outputPath -Force
}

# Crear nuevo ZIP
Compress-Archive -Path "$cursoPath\*" -DestinationPath $outputPath -CompressionLevel Optimal

Write-Host "✅ Paquete SCORM creado: $outputPath" -ForegroundColor Green
Write-Host "📦 Tamaño: $((Get-Item $outputPath).Length / 1MB) MB" -ForegroundColor Cyan
```

## 📤 Importar en Moodle/Aules

### Pasos en Moodle:

1. **Acceder al curso** en Moodle/Aules
2. **Activar edición** (botón "Activar edición")
3. **"Añadir una actividad o recurso"**
4. Seleccionar **"Paquete SCORM"**
5. **Configurar**:
   - Nombre: "Curso TICD - Competencia Digital"
   - Descripción: (opcional)
   - Archivo del paquete: Subir el ZIP creado
6. **Opciones de calificación** (opcional):
   - Método de calificación: Si deseas calificaciones automáticas
7. **Guardar y mostrar**

### Pasos en Aules (Moodle de la Generalitat):

Exactamente los mismos pasos que Moodle, ya que Aules es Moodle.

## ⚙️ Configuración Avanzada SCORM

### Añadir Seguimiento de Completado

Si quieres que el LMS marque el curso como completado automáticamente, añade al final de cada HTML (antes de `</body>`):

```html
<script>
// Marcar página como visitada
if (typeof setLocation === 'function') {
    setLocation(document.title);
}

// Si es la última página, marcar como completado
if (window.location.href.indexOf('evaluacion.html') > -1) {
    setTimeout(function() {
        if (typeof setCompleted === 'function') {
            setCompleted();
        }
    }, 5000); // 5 segundos después de cargar evaluacion.html
}
</script>
```

### Añadir Seguimiento de Cuestionarios

Para que el generador de cuestionarios envíe puntuaciones al LMS, modifica `generador_cuestionarios.html`:

Añade después de calcular los resultados:

```javascript
// En la función mostrarResultados, después de calcular porcentaje:
if (typeof setScore === 'function') {
    setScore(correctas, 0, total);
}
if (porcentaje >= 50 && typeof setCompleted === 'function') {
    setCompleted();
}
```

## 🧪 Probar el Paquete SCORM

### Online (Gratuito):

1. **SCORM Cloud** (https://cloud.scorm.com)
   - Crear cuenta gratuita
   - Subir el ZIP
   - Probar funcionalidad

2. **Rustici SCORM Driver** (https://rusticisoftware.com/products/scorm-driver/)
   - Herramienta de testing

### Local:

1. **Instalar XAMPP o similar** (servidor web local)
2. Descomprimir el ZIP en la carpeta `htdocs`
3. Abrir en navegador: `http://localhost/Curso_eXeLearning_TICD`

## ⚠️ Problemas Comunes y Soluciones

### ❌ "Archivo de manifiesto no válido"

**Solución:** 
- Verifica que `imsmanifest.xml` esté en la raíz del ZIP
- Comprueba que no haya carpeta adicional dentro del ZIP

### ❌ "No se pueden cargar los recursos"

**Solución:**
- Revisa las rutas en `imsmanifest.xml`
- Asegúrate de que las carpetas `css/`, `images/` estén incluidas
- Verifica que no haya espacios o caracteres especiales en nombres de archivo

### ❌ "El curso no marca como completado"

**Solución:**
- Añade el script SCORM a los HTML
- Configura en Moodle: "Paquete SCORM" → "Completar actividad" → "Requiere completar"

### ❌ "Las imágenes no se cargan"

**Solución:**
- Verifica que las rutas sean relativas (no absolutas)
- Incluye todas las carpetas de recursos en el ZIP

## 📋 Checklist Pre-Subida

Antes de subir a Moodle/Aules, verifica:

- [ ] `imsmanifest.xml` está en la raíz del ZIP
- [ ] Todos los archivos HTML están incluidos
- [ ] Carpeta `css/` incluida con `style.css`
- [ ] Archivo `base_conocimiento_ticd.json` incluido
- [ ] `generador_cuestionarios.html` incluido
- [ ] No hay carpeta adicional contenedora
- [ ] El ZIP abre correctamente
- [ ] Tamaño del ZIP es razonable (< 50 MB)

## 🎓 Especificaciones del Paquete

- **Estándar:** SCORM 1.2
- **Tipo:** SCO (Sharable Content Object)
- **Organización:** Secuencial (8 elementos)
- **Compatible con:** Moodle 2.x+, Aules, Blackboard, Canvas, etc.

## 🔄 Actualizar el Paquete

Para actualizar el curso ya subido:

1. Hacer cambios en los archivos HTML
2. Recrear el ZIP con los pasos anteriores
3. En Moodle: Editar actividad → Reemplazar archivo del paquete
4. O eliminar la actividad antigua y crear una nueva

## 📊 Funcionalidades SCORM Incluidas

✅ Navegación entre bloques
✅ Estructura jerárquica del curso
✅ Seguimiento de progreso (con scripts adicionales)
✅ Compatible con calificaciones (con scripts adicionales)
✅ Funciona offline después de descargar
✅ Responsive y accesible

## 🚀 ¡Listo para Usar!

Tu curso TICD está preparado para ser empaquetado como SCORM y subido a cualquier LMS compatible.

**Siguiente paso:** Ejecuta el comando de PowerShell para crear el ZIP y súbelo a Moodle/Aules.

---

**Versión SCORM:** 1.2  
**Fecha:** Febrero 2026  
**Compatible con:** Moodle, Aules, Blackboard, Canvas, y otros LMS compatibles con SCORM
