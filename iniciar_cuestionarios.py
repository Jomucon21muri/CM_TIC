"""
Script de Inicio Rápido - Sistema de Cuestionarios TICD
Abre el generador de cuestionarios en el navegador predeterminado
"""

import webbrowser
import os
from pathlib import Path

def main():
    """Abre el generador de cuestionarios"""
    # Obtener la ruta del archivo HTML
    script_dir = Path(__file__).parent
    html_file = script_dir / "generador_cuestionarios.html"
    
    if not html_file.exists():
        print("❌ Error: No se encontró generador_cuestionarios.html")
        print(f"   Buscando en: {html_file}")
        return
    
    # Convertir a URL file://
    file_url = html_file.as_uri()
    
    print("🚀 Abriendo Generador de Cuestionarios TICD...")
    print(f"📁 Ubicación: {html_file}")
    print(f"🌐 URL: {file_url}")
    print("\n✨ El generador se abrirá en tu navegador predeterminado")
    print("   Si no se abre automáticamente, copia la URL anterior en tu navegador\n")
    
    # Abrir en el navegador
    try:
        webbrowser.open(file_url)
        print("✅ Navegador abierto correctamente")
        print("\n📚 Cómo usar:")
        print("   1. Selecciona un módulo (o 'Todos los módulos')")
        print("   2. Elige el número de preguntas (5-30)")
        print("   3. Haz clic en 'Generar Cuestionario'")
        print("   4. Responde las preguntas")
        print("   5. Haz clic en 'Verificar Respuestas' para ver los resultados\n")
        print("¡Disfruta practicando! 🎓\n")
    except Exception as e:
        print(f"❌ Error al abrir el navegador: {e}")
        print(f"   Por favor, abre manualmente el archivo: {html_file}")

if __name__ == "__main__":
    main()
