"""
Sistema de Base de Conocimiento para Cuestionarios TICD
Extrae preguntas y respuestas de los tests y crea una base de datos estructurada por módulos
"""

import os
import re
import json

# Definición de los módulos temáticos
MODULOS = {
    "hardware": {
        "nombre": "Hardware y Arquitectura",
        "keywords": ["KB", "bytes", "bits", "memoria", "RAM", "ROM", "caché", "microprocesador", "CPU", 
                     "periférico", "ratón", "teclado", "scanner", "monitor", "USB", "flash", "disco duro",
                     "DVD", "CD", "óptico", "almacenamiento", "PB", "petabyte", "TB", "terabyte", "GB", "MB"]
    },
    "software": {
        "nombre": "Software y Sistemas Operativos",
        "keywords": ["sistema operativo", "driver", "firmware", "ROM", "software", "shareware", "bugs",
                     "Plug&Play", "hardware", "lenguaje de programación", "código", "Unicode", "ASCII", "ANSI"]
    },
    "redes": {
        "nombre": "Redes e Internet",
        "keywords": ["IP", "dirección IP", "red", "LAN", "WAN", "router", "protocolo", "HTTP", "HTTPS",
                     "URL", "DNS", "WWW", "internet", "navegador", "Chrome", "Safari", "Explorer", "Firefox"]
    },
    "seguridad": {
        "nombre": "Seguridad Informática",
        "keywords": ["spam", "virus", "antivirus", "phishing", "scam", "hoax", "troyano", "malware",
                     "firewall", "criptografía", "encriptación", "contraseña", "seguridad", "antispam"]
    },
    "ofimatica": {
        "nombre": "Ofimática",
        "keywords": ["procesador de texto", "hoja de cálculo", "celda", "fórmula", "presentación",
                     "diapositiva", "transición", "OpenOffice", "LibreOffice", "Writer", "Calc", "Impress",
                     "Base", "texto", "alineación", "justificada", "vista preliminar", ".txt", ".doc", 
                     ".odt", ".ods", ".odp", ".odb"]
    },
    "bases_datos": {
        "nombre": "Bases de Datos",
        "keywords": ["base de datos", "SGBD", "tabla", "registro", "campo", "clave primaria", "SQL",
                     "relacional", "consulta"]
    },
    "multimedia": {
        "nombre": "Multimedia",
        "keywords": ["imagen", "vídeo", "audio", "formato", "JPG", "GIF", "PNG", "TIFF", "vectorial",
                     "rasterizado", "RGB", "píxel", "resolución", "compresión", "AVI", "MP3", "MP4",
                     "OGG", "MIDI", "FLV", "calidad", "Adobe Flash"]
    },
    "web_social": {
        "nombre": "Web 2.0 y Redes Sociales",
        "keywords": ["Web 2.0", "red social", "comunidad virtual", "foro", "wiki", "blog", "post",
                     "página web", "dinámica", "estática", "interactiva", "MUD", "moderador", "Google Docs"]
    },
    "licencias": {
        "nombre": "Licencias y Derechos",
        "keywords": ["Creative Commons", "licencia", "copyright", "autor", "uso comercial", "obra derivada",
                     "dominio público", "copyleft"]
    }
}

def parse_test_file(file_path):
    """Parsea un archivo de test y extrae todas las preguntas"""
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    preguntas = []
    lines = content.split('\n')
    
    i = 0
    while i < len(lines):
        line = lines[i].strip()
        
        # Detectar inicio de pregunta (número seguido de punto o paréntesis)
        match = re.match(r'^(\d+)[\.\)\-]\s*(.*)', line)
        if match:
            num_pregunta = match.group(1)
            texto_pregunta = match.group(2).strip()
            
            # Continuar leyendo hasta encontrar las opciones
            i += 1
            while i < len(lines) and not re.match(r'^[a-d][\.\)]', lines[i].strip()):
                texto_adicional = lines[i].strip()
                if texto_adicional and not re.match(r'^(\d+)[\.\)\-]', texto_adicional):
                    texto_pregunta += " " + texto_adicional
                else:
                    break
                i += 1
            
            # Extraer opciones (con o sin espacio después de letra)
            opciones = {}
            while i < len(lines) and re.match(r'^[a-d][\.\)]', lines[i].strip()):
                option_line = lines[i].strip()
                option_match = re.match(r'^([a-d])[\.\)]\s*(.*)', option_line)
                if option_match:
                    letra = option_match.group(1)
                    texto_opcion = option_match.group(2).strip()
                    
                    # Continuar leyendo si la opción continúa en la siguiente línea
                    i += 1
                    while i < len(lines):
                        next_line = lines[i].strip()
                        if not next_line or re.match(r'^[a-d][\.\)]', next_line) or re.match(r'^(\d+)[\.\)\-]', next_line):
                            break
                        texto_opcion += " " + next_line
                        i += 1
                    
                    opciones[letra] = texto_opcion
                else:
                    i += 1
            
            if len(opciones) >= 2:  # Solo añadir si tiene al menos 2 opciones
                preguntas.append({
                    'numero': int(num_pregunta),
                    'pregunta': texto_pregunta,
                    'opciones': opciones
                })
        else:
            i += 1
    
    return preguntas

def parse_solutions_simple(file_path):
    """Parsea un archivo de soluciones formato simple (tabla)"""
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    soluciones = {}
    
    # Buscar patrones como "1 b", "2 c", etc. (formato tabla)
    matches = re.findall(r'(\d+)\s+([a-d])(?:\s|$)', content)
    for num, respuesta in matches:
        soluciones[int(num)] = respuesta
    
    # Buscar formato alternativo "1.a", "2.c", etc. (formato línea)
    matches2 = re.findall(r'(\d+)\.([a-d])(?:\s|$)', content)
    for num, respuesta in matches2:
        if int(num) not in soluciones:  # No sobrescribir si ya existe
            soluciones[int(num)] = respuesta
    
    return soluciones

def parse_solutions_detailed(file_path):
    """Parsea un archivo de soluciones formato detallado (con explicaciones)"""
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    soluciones = {}
    lines = content.split('\n')
    
    i = 0
    while i < len(lines):
        line = lines[i].strip()
        
        # Detectar número de pregunta
        match = re.match(r'^(\d+)\.\s*(.*)', line)
        if match:
            num_pregunta = int(match.group(1))
            resto = match.group(2).strip()
            
            # Formato 1: Respuesta con paréntesis "1. Pregunta: a) respuesta..."
            respuesta_match = re.search(r'^[^:]+:\s*([a-d])\)', resto)
            if respuesta_match:
                letra = respuesta_match.group(1)
                explicacion = resto[respuesta_match.end():].strip()
                
                # Continuar leyendo la explicación si continúa en siguientes líneas
                i += 1
                while i < len(lines):
                    next_line = lines[i].strip()
                    if not next_line or re.match(r'^\d+\.', next_line):
                        break
                    explicacion += " " + next_line
                    i += 1
                
                soluciones[num_pregunta] = {
                    'respuesta': letra,
                    'explicacion': explicacion
                }
                continue
            
            # Formato 2: Respuesta directa "1. a) respuesta..."
            respuesta_match = re.match(r'^([a-d])\)\s*(.*)', resto)
            if respuesta_match:
                letra = respuesta_match.group(1)
                explicacion = respuesta_match.group(2).strip()
                
                # Continuar leyendo la explicación si continúa en siguientes líneas
                i += 1
                while i < len(lines):
                    next_line = lines[i].strip()
                    if not next_line or re.match(r'^\d+\.', next_line):
                        break
                    explicacion += " " + next_line
                    i += 1
                
                soluciones[num_pregunta] = {
                    'respuesta': letra,
                    'explicacion': explicacion
                }
                continue
        
        i += 1
    
    return soluciones

def clasificar_pregunta(pregunta_texto):
    """Clasifica una pregunta en uno o más módulos según palabras clave"""
    texto_lower = pregunta_texto.lower()
    modulos_detectados = []
    
    for modulo_id, modulo_info in MODULOS.items():
        for keyword in modulo_info['keywords']:
            if keyword.lower() in texto_lower:
                modulos_detectados.append(modulo_id)
                break
    
    # Si no se detecta ningún módulo, clasificar como "general"
    if not modulos_detectados:
        modulos_detectados.append("general")
    
    return modulos_detectados

def generar_explicacion_generica(pregunta_texto, respuesta_correcta, opciones):
    """Genera una explicación genérica cuando no hay explicación específica"""
    opcion_texto = opciones.get(respuesta_correcta, "")
    return f"La respuesta correcta es '{respuesta_correcta}': {opcion_texto}"

def main():
    """Función principal para crear la base de conocimiento"""
    folder = "preguntas_extraidas"
    
    # Estructura de la base de conocimiento
    base_conocimiento = {
        "modulos": MODULOS,
        "preguntas": []
    }
    
    # Listar todos los archivos de tests (no soluciones)
    test_files = sorted([f for f in os.listdir(folder) if f.endswith('.txt') and 'SOL' not in f])
    
    for test_file in test_files:
        print(f"\nProcesando: {test_file}")
        test_path = os.path.join(folder, test_file)
        
        # Extraer año del nombre del archivo
        year_match = re.search(r'(20\d{2})', test_file)
        year = year_match.group(1) if year_match else "unknown"
        
        # Parsear preguntas
        preguntas = parse_test_file(test_path)
        print(f"  - Encontradas {len(preguntas)} preguntas")
        
        # Buscar archivo de soluciones correspondiente
        sol_file = test_file.replace('PAGS_TICD', 'SOL.PAGS_TICD')
        sol_path = os.path.join(folder, sol_file)
        
        soluciones = {}
        if os.path.exists(sol_path):
            # Intentar parsear formato detallado primero
            soluciones_detalladas = parse_solutions_detailed(sol_path)
            if soluciones_detalladas:
                soluciones = soluciones_detalladas
                print(f"  - Soluciones detalladas cargadas: {len(soluciones)}")
            else:
                # Si no, parsear formato simple
                soluciones_simple = parse_solutions_simple(sol_path)
                soluciones = {k: {'respuesta': v, 'explicacion': ''} for k, v in soluciones_simple.items()}
                print(f"  - Soluciones simples cargadas: {len(soluciones)}")
        else:
            print(f"  - Advertencia: No se encontró archivo de soluciones")
        
        # Combinar preguntas con soluciones y clasificar
        for pregunta in preguntas:
            num = pregunta['numero']
            modulos = clasificar_pregunta(pregunta['pregunta'])
            
            respuesta_info = soluciones.get(num, {})
            respuesta_correcta = respuesta_info.get('respuesta', '') if isinstance(respuesta_info, dict) else respuesta_info
            explicacion = respuesta_info.get('explicacion', '') if isinstance(respuesta_info, dict) else ''
            
            # Generar explicación genérica si no hay
            if not explicacion and respuesta_correcta:
                explicacion = generar_explicacion_generica(pregunta['pregunta'], respuesta_correcta, pregunta['opciones'])
            
            base_conocimiento['preguntas'].append({
                'id': f"{year}_{num}",
                'año': year,
                'numero_original': num,
                'pregunta': pregunta['pregunta'],
                'opciones': pregunta['opciones'],
                'respuesta_correcta': respuesta_correcta,
                'explicacion': explicacion,
                'modulos': modulos
            })
    
    # Guardar base de conocimiento en JSON
    output_file = "base_conocimiento_ticd.json"
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(base_conocimiento, f, indent=2, ensure_ascii=False)
    
    print(f"\n✓ Base de conocimiento creada: {output_file}")
    print(f"✓ Total de preguntas: {len(base_conocimiento['preguntas'])}")
    
    # Estadísticas por módulo
    print("\n--- Estadísticas por Módulo ---")
    stats = {}
    for pregunta in base_conocimiento['preguntas']:
        for modulo in pregunta['modulos']:
            stats[modulo] = stats.get(modulo, 0) + 1
    
    for modulo, count in sorted(stats.items(), key=lambda x: x[1], reverse=True):
        nombre_modulo = MODULOS.get(modulo, {}).get('nombre', modulo)
        print(f"  {nombre_modulo}: {count} preguntas")

if __name__ == "__main__":
    main()
