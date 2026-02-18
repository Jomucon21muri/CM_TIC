# =============================================================================
# Script para Crear Paquete SCORM del Curso TICD
# =============================================================================
# Este script empaqueta todo el contenido del curso en formato SCORM 1.2
# para ser importado en plataformas LMS (Moodle, Aules, etc.)
# =============================================================================

Write-Host "========================================" -ForegroundColor Cyan
Write-Host "  Creador de Paquete SCORM - Curso TICD" -ForegroundColor Cyan
Write-Host "========================================" -ForegroundColor Cyan
Write-Host ""

# Rutas de entrada y salida
$cursoPath = "c:\Users\muril\OneDrive - Conselleria d'Educació\Curso_madurez_TIC\Curso_eXeLearning_TICD"
$outputPath = "c:\Users\muril\OneDrive - Conselleria d'Educació\Curso_madurez_TIC\TICD_SCORM_Package.zip"

# Verificar que existe la carpeta del curso
if (-not (Test-Path $cursoPath)) {
    Write-Host "❌ Error: No se encuentra la carpeta del curso en:" -ForegroundColor Red
    Write-Host "   $cursoPath" -ForegroundColor Yellow
    exit 1
}

Write-Host "📂 Carpeta del curso encontrada" -ForegroundColor Green
Write-Host "   $cursoPath" -ForegroundColor Gray
Write-Host ""

# Verificar archivos críticos SCORM
Write-Host "🔍 Verificando archivos SCORM..." -ForegroundColor Cyan

$archivosCriticos = @(
    "imsmanifest.xml",
    "scorm_api.js",
    "index.html",
    "generador_cuestionarios.html",
    "base_conocimiento_ticd.json"
)

$todosPresentes = $true
foreach ($archivo in $archivosCriticos) {
    $rutaCompleta = Join-Path $cursoPath $archivo
    if (Test-Path $rutaCompleta) {
        Write-Host "   ✅ $archivo" -ForegroundColor Green
    } else {
        Write-Host "   ❌ $archivo (NO ENCONTRADO)" -ForegroundColor Red
        $todosPresentes = $false
    }
}

if (-not $todosPresentes) {
    Write-Host ""
    Write-Host "❌ Faltan archivos críticos. No se puede crear el paquete SCORM." -ForegroundColor Red
    exit 1
}

Write-Host ""
Write-Host "✅ Todos los archivos críticos están presentes" -ForegroundColor Green
Write-Host ""

# Eliminar paquete anterior si existe
if (Test-Path $outputPath) {
    Write-Host "🗑️  Eliminando paquete anterior..." -ForegroundColor Yellow
    Remove-Item $outputPath -Force
    Write-Host "   ✅ Archivo anterior eliminado" -ForegroundColor Green
    Write-Host ""
}

# Crear el paquete ZIP
Write-Host "📦 Creando paquete SCORM..." -ForegroundColor Cyan
Write-Host "   Comprimiendo archivos..." -ForegroundColor Gray

try {
    Compress-Archive -Path "$cursoPath\*" -DestinationPath $outputPath -CompressionLevel Optimal -Force
    Write-Host "   ✅ Compresión completada" -ForegroundColor Green
} catch {
    Write-Host "   ❌ Error al comprimir: $($_.Exception.Message)" -ForegroundColor Red
    exit 1
}

Write-Host ""

# Verificar el paquete creado
if (Test-Path $outputPath) {
    $archivoZip = Get-Item $outputPath
    $tamanoMB = [math]::Round($archivoZip.Length / 1MB, 2)
    
    Write-Host "========================================" -ForegroundColor Green
    Write-Host "  ✅ PAQUETE SCORM CREADO EXITOSAMENTE" -ForegroundColor Green
    Write-Host "========================================" -ForegroundColor Green
    Write-Host ""
    Write-Host "📦 Archivo: " -NoNewline -ForegroundColor Cyan
    Write-Host "$($archivoZip.Name)" -ForegroundColor White
    Write-Host "📂 Ubicación: " -NoNewline -ForegroundColor Cyan
    Write-Host "$($archivoZip.DirectoryName)" -ForegroundColor White
    Write-Host "💾 Tamaño: " -NoNewline -ForegroundColor Cyan
    Write-Host "$tamanoMB MB" -ForegroundColor White
    Write-Host "📅 Fecha: " -NoNewline -ForegroundColor Cyan
    Write-Host "$($archivoZip.LastWriteTime)" -ForegroundColor White
    Write-Host ""
    
    # Verificar contenido del ZIP
    Write-Host "🔍 Verificando contenido del paquete..." -ForegroundColor Cyan
    
    # Leer contenido del ZIP
    Add-Type -AssemblyName System.IO.Compression.FileSystem
    $zip = [System.IO.Compression.ZipFile]::OpenRead($outputPath)
    
    $manifestEncontrado = $false
    $htmlEncontrados = 0
    $carpetaCss = $false
    
    foreach ($entry in $zip.Entries) {
        if ($entry.Name -eq "imsmanifest.xml" -and $entry.FullName -eq "imsmanifest.xml") {
            $manifestEncontrado = $true
        }
        if ($entry.Name -like "*.html") {
            $htmlEncontrados++
        }
        if ($entry.FullName -like "css/*") {
            $carpetaCss = $true
        }
    }
    
    $zip.Dispose()
    
    # Mostrar resultados de verificación
    if ($manifestEncontrado) {
        Write-Host "   ✅ imsmanifest.xml en la raíz del ZIP" -ForegroundColor Green
    } else {
        Write-Host "   ⚠️  imsmanifest.xml NO está en la raíz" -ForegroundColor Yellow
    }
    
    Write-Host "   ✅ $htmlEncontrados archivos HTML encontrados" -ForegroundColor Green
    
    if ($carpetaCss) {
        Write-Host "   ✅ Carpeta css/ incluida" -ForegroundColor Green
    } else {
        Write-Host "   ⚠️  Carpeta css/ no encontrada" -ForegroundColor Yellow
    }
    
    Write-Host ""
    Write-Host "========================================" -ForegroundColor Cyan
    Write-Host "  📤 PRÓXIMOS PASOS" -ForegroundColor Cyan
    Write-Host "========================================" -ForegroundColor Cyan
    Write-Host ""
    Write-Host "1️⃣  Accede a tu plataforma Moodle o Aules" -ForegroundColor White
    Write-Host "2️⃣  Activa la edición en tu curso" -ForegroundColor White
    Write-Host "3️⃣  'Añadir una actividad o recurso'" -ForegroundColor White
    Write-Host "4️⃣  Selecciona 'Paquete SCORM'" -ForegroundColor White
    Write-Host "5️⃣  Sube el archivo:" -ForegroundColor White
    Write-Host "     $($archivoZip.Name)" -ForegroundColor Yellow
    Write-Host ""
    Write-Host "📖 Más información en: CREAR_PAQUETE_SCORM.md" -ForegroundColor Gray
    Write-Host ""
    
    # Opción para abrir la carpeta
    Write-Host "¿Deseas abrir la carpeta del paquete? (S/N): " -NoNewline -ForegroundColor Cyan
    $respuesta = Read-Host
    
    if ($respuesta -eq "S" -or $respuesta -eq "s") {
        Start-Process explorer.exe -ArgumentList "/select,`"$outputPath`""
    }
    
} else {
    Write-Host "❌ Error: El paquete no se creó correctamente" -ForegroundColor Red
    exit 1
}

Write-Host ""
Write-Host "✅ Proceso completado exitosamente" -ForegroundColor Green
Write-Host ""
