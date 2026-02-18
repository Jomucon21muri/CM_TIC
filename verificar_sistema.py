"""
Verificador de Sistema - Cuestionarios TICD
Verifica que todos los archivos necesarios estén presentes y funcionando
"""

import os
import json
from pathlib import Path

def check_file(filepath, description):
    """Verifica si un archivo existe"""
    exists = os.path.exists(filepath)
    status = "✅" if exists else "❌"
    print(f"  {status} {description}: {filepath.name}")
    return exists

def check_json_valid(filepath):
    """Verifica si un archivo JSON es válido"""
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            data = json.load(f)
        print(f"     ✓ JSON válido con {len(data.get('preguntas', []))} preguntas")
        return True
    except Exception as e:
        print(f"     ✗ Error al leer JSON: {e}")
        return False

def main():
    """Función principal de verificación"""
    print("\n" + "="*70)
    print("🔍 VERIFICACIÓN DEL SISTEMA DE CUESTIONARIOS TICD")
    print("="*70 + "\n")
    
    base_dir = Path(__file__).parent
    all_ok = True
    
    # Verificar archivos principales
    print("📄 ARCHIVOS PRINCIPALES:")
    required_files = [
        ('generador_cuestionarios.html', 'Generador web interactivo'),
        ('base_conocimiento_ticd.json', 'Base de datos de preguntas'),
    ]
    
    for filename, description in required_files:
        filepath = base_dir / filename
        if not check_file(filepath, description):
            all_ok = False
        elif filename.endswith('.json'):
            if not check_json_valid(filepath):
                all_ok = False
    
    # Verificar scripts Python
    print("\n🐍 SCRIPTS PYTHON:")
    scripts = [
        ('extraer_preguntas.py', 'Extractor de PDFs de tests'),
        ('extraer_soluciones.py', 'Extractor de PDFs de soluciones'),
        ('crear_base_conocimiento.py', 'Generador de base de datos'),
        ('enriquecer_explicaciones.py', 'Enriquecedor de explicaciones'),
        ('verificar_base_conocimiento.py', 'Analizador de estadísticas'),
        ('iniciar_cuestionarios.py', 'Script de inicio rápido'),
    ]
    
    for filename, description in scripts:
        filepath = base_dir / filename
        check_file(filepath, description)
    
    # Verificar documentación
    print("\n📚 DOCUMENTACIÓN:")
    docs = [
        ('README_CUESTIONARIOS.md', 'Documentación completa'),
        ('RESUMEN_SISTEMA.md', 'Resumen del sistema'),
        ('INICIO_RAPIDO.md', 'Guía de inicio rápido'),
    ]
    
    for filename, description in docs:
        filepath = base_dir / filename
        check_file(filepath, description)
    
    # Verificar carpetas
    print("\n📁 CARPETAS:")
    folders = [
        ('test', 'PDFs de tests originales'),
        ('soluciones', 'PDFs de soluciones'),
        ('preguntas_extraidas', 'Textos extraídos de PDFs'),
    ]
    
    for foldername, description in folders:
        folderpath = base_dir / foldername
        exists = os.path.exists(folderpath) and os.path.isdir(folderpath)
        status = "✅" if exists else "❌"
        print(f"  {status} {description}: {foldername}/")
        if exists:
            num_files = len(os.listdir(folderpath))
            print(f"     ℹ️  Contiene {num_files} archivos")
    
    # Verificar base de conocimiento
    print("\n📊 ESTADÍSTICAS DE LA BASE DE CONOCIMIENTO:")
    json_path = base_dir / 'base_conocimiento_ticd.json'
    if os.path.exists(json_path):
        try:
            with open(json_path, 'r', encoding='utf-8') as f:
                data = json.load(f)
            
            total = len(data['preguntas'])
            con_respuesta = sum(1 for p in data['preguntas'] if p.get('respuesta_correcta'))
            modulos = len(data['modulos'])
            
            print(f"  ℹ️  Total de preguntas: {total}")
            print(f"  ℹ️  Con respuesta correcta: {con_respuesta} ({con_respuesta/total*100:.1f}%)")
            print(f"  ℹ️  Módulos disponibles: {modulos}")
            
            # Mostrar módulos
            print("\n  📖 Módulos:")
            for mod_id, mod_info in data['modulos'].items():
                count = sum(1 for p in data['preguntas'] if mod_id in p.get('modulos', []))
                if count > 0:
                    print(f"     • {mod_info['nombre']}: {count} preguntas")
        except Exception as e:
            print(f"  ❌ Error al analizar base de conocimiento: {e}")
            all_ok = False
    
    # Resultado final
    print("\n" + "="*70)
    if all_ok:
        print("✅ SISTEMA COMPLETO Y LISTO PARA USAR")
        print("\n🚀 Para empezar:")
        print("   1. Ejecuta: python iniciar_cuestionarios.py")
        print("   2. O abre: generador_cuestionarios.html")
    else:
        print("⚠️  SISTEMA INCOMPLETO - Faltan algunos archivos")
        print("\n📝 Acciones recomendadas:")
        print("   1. Verifica que todos los archivos estén en la carpeta correcta")
        print("   2. Si falta la base de datos, ejecuta: python crear_base_conocimiento.py")
    print("="*70 + "\n")

if __name__ == "__main__":
    main()
