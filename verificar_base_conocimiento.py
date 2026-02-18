"""
Verificador y Generador de Estadísticas para Base de Conocimiento TICD
Analiza la calidad y completitud de la base de conocimiento
"""

import json
from collections import Counter, defaultdict

def cargar_base(archivo):
    """Carga la base de conocimiento"""
    with open(archivo, 'r', encoding='utf-8') as f:
        return json.load(f)

def verificar_integridad(base):
    """Verifica la integridad de los datos"""
    problemas = []
    
    for i, pregunta in enumerate(base['preguntas']):
        # Verificar campos requeridos
        if not pregunta.get('pregunta'):
            problemas.append(f"Pregunta {i+1} ({pregunta.get('id')}): Sin texto de pregunta")
        
        if not pregunta.get('opciones') or len(pregunta['opciones']) < 2:
            problemas.append(f"Pregunta {i+1} ({pregunta.get('id')}): Menos de 2 opciones")
        
        if not pregunta.get('respuesta_correcta'):
            problemas.append(f"Pregunta {i+1} ({pregunta.get('id')}): Sin respuesta correcta")
        
        if not pregunta.get('explicacion'):
            problemas.append(f"Pregunta {i+1} ({pregunta.get('id')}): Sin explicación")
        
        # Verificar que la respuesta correcta esté en las opciones
        if pregunta.get('respuesta_correcta') not in pregunta.get('opciones', {}):
            problemas.append(f"Pregunta {i+1} ({pregunta.get('id')}): Respuesta correcta '{pregunta.get('respuesta_correcta')}' no está en opciones")
    
    return problemas

def generar_estadisticas(base):
    """Genera estadísticas detalladas de la base de conocimiento"""
    
    print("\n" + "="*70)
    print("📊 ESTADÍSTICAS DE LA BASE DE CONOCIMIENTO TICD")
    print("="*70)
    
    total_preguntas = len(base['preguntas'])
    
    # Estadísticas generales
    print(f"\n📚 GENERAL:")
    print(f"  • Total de preguntas: {total_preguntas}")
    print(f"  • Módulos definidos: {len(base['modulos'])}")
    
    # Preguntas con respuesta
    con_respuesta = sum(1 for p in base['preguntas'] if p.get('respuesta_correcta'))
    print(f"  • Preguntas con respuesta: {con_respuesta} ({con_respuesta/total_preguntas*100:.1f}%)")
    
    # Preguntas con explicación
    con_explicacion = sum(1 for p in base['preguntas'] if p.get('explicacion'))
    explicaciones_genericas = sum(1 for p in base['preguntas'] 
                                  if p.get('explicacion', '').startswith('La respuesta correcta es'))
    explicaciones_detalladas = con_explicacion - explicaciones_genericas
    
    print(f"  • Preguntas con explicación: {con_explicacion} ({con_explicacion/total_preguntas*100:.1f}%)")
    print(f"    - Explicaciones detalladas: {explicaciones_detalladas} ({explicaciones_detalladas/total_preguntas*100:.1f}%)")
    print(f"    - Explicaciones genéricas: {explicaciones_genericas} ({explicaciones_genericas/total_preguntas*100:.1f}%)")
    
    # Distribución por años
    print(f"\n📅 DISTRIBUCIÓN POR AÑO:")
    años = Counter(p['año'] for p in base['preguntas'])
    for año, count in sorted(años.items()):
        print(f"  • {año}: {count} preguntas ({count/total_preguntas*100:.1f}%)")
    
    # Distribución por módulos
    print(f"\n📖 DISTRIBUCIÓN POR MÓDULO:")
    modulo_count = defaultdict(int)
    for pregunta in base['preguntas']:
        for modulo in pregunta.get('modulos', ['general']):
            modulo_count[modulo] += 1
    
    for modulo, count in sorted(modulo_count.items(), key=lambda x: x[1], reverse=True):
        nombre_modulo = base['modulos'].get(modulo, {}).get('nombre', modulo)
        porcentaje = count/total_preguntas*100
        barra = '█' * int(porcentaje/2)
        print(f"  • {nombre_modulo:30} {count:3} preguntas {barra} {porcentaje:.1f}%")
    
    # Distribución de opciones
    print(f"\n🔤 OPCIONES POR PREGUNTA:")
    opciones_count = Counter(len(p.get('opciones', {})) for p in base['preguntas'])
    for num_opciones, count in sorted(opciones_count.items()):
        print(f"  • {num_opciones} opciones: {count} preguntas")
    
    # Distribución de respuestas correctas
    print(f"\n✅ DISTRIBUCIÓN DE RESPUESTAS CORRECTAS:")
    respuestas = Counter(p.get('respuesta_correcta', 'sin respuesta') for p in base['preguntas'])
    for letra, count in sorted(respuestas.items()):
        if letra != 'sin respuesta':
            print(f"  • Opción '{letra}': {count} veces ({count/con_respuesta*100:.1f}%)")
        else:
            print(f"  • Sin respuesta: {count} preguntas")
    
    # Longitud de preguntas
    print(f"\n📏 LONGITUD DE PREGUNTAS:")
    longitudes = [len(p['pregunta']) for p in base['preguntas'] if p.get('pregunta')]
    if longitudes:
        print(f"  • Promedio: {sum(longitudes)/len(longitudes):.0f} caracteres")
        print(f"  • Mínima: {min(longitudes)} caracteres")
        print(f"  • Máxima: {max(longitudes)} caracteres")
    
    # Longitud de explicaciones
    print(f"\n📝 LONGITUD DE EXPLICACIONES:")
    long_explicaciones = [len(p['explicacion']) for p in base['preguntas'] if p.get('explicacion')]
    if long_explicaciones:
        print(f"  • Promedio: {sum(long_explicaciones)/len(long_explicaciones):.0f} caracteres")
        print(f"  • Mínima: {min(long_explicaciones)} caracteres")
        print(f"  • Máxima: {max(long_explicaciones)} caracteres")
    
    # Preguntas multimódulo
    print(f"\n🔗 CLASIFICACIÓN MULTIMÓDULO:")
    multimodulo = [len(p.get('modulos', [])) for p in base['preguntas']]
    multimodulo_count = Counter(multimodulo)
    for num_modulos, count in sorted(multimodulo_count.items()):
        print(f"  • {num_modulos} módulo(s): {count} preguntas")
    
    print("\n" + "="*70)

def mostrar_problemas(problemas):
    """Muestra los problemas encontrados"""
    if problemas:
        print("\n⚠️  PROBLEMAS ENCONTRADOS:")
        for problema in problemas[:20]:  # Mostrar máximo 20
            print(f"  • {problema}")
        if len(problemas) > 20:
            print(f"  ... y {len(problemas)-20} problemas más")
    else:
        print("\n✅ No se encontraron problemas de integridad")

def mostrar_ejemplos(base, num_ejemplos=3):
    """Muestra ejemplos de preguntas"""
    print(f"\n📝 EJEMPLOS DE PREGUNTAS:")
    print("="*70)
    
    import random
    ejemplos = random.sample(base['preguntas'], min(num_ejemplos, len(base['preguntas'])))
    
    for i, pregunta in enumerate(ejemplos, 1):
        modulos = ', '.join(base['modulos'].get(m, {}).get('nombre', m) for m in pregunta.get('modulos', ['general']))
        
        print(f"\n{i}. [{pregunta['año']}] {pregunta['pregunta']}")
        print(f"   Módulos: {modulos}")
        
        for letra, texto in sorted(pregunta.get('opciones', {}).items()):
            marcador = "✓" if letra == pregunta.get('respuesta_correcta') else " "
            print(f"   {marcador} {letra}) {texto[:60]}{'...' if len(texto) > 60 else ''}")
        
        if pregunta.get('explicacion'):
            exp = pregunta['explicacion']
            print(f"   💡 {exp[:120]}{'...' if len(exp) > 120 else ''}")

def main():
    """Función principal"""
    archivo = "base_conocimiento_ticd.json"
    
    print("Cargando base de conocimiento...")
    base = cargar_base(archivo)
    
    # Generar estadísticas
    generar_estadisticas(base)
    
    # Verificar integridad
    problemas = verificar_integridad(base)
    mostrar_problemas(problemas)
    
    # Mostrar ejemplos
    mostrar_ejemplos(base, 3)
    
    print("\n" + "="*70)
    print("✓ Análisis completado")
    print("="*70 + "\n")

if __name__ == "__main__":
    main()
