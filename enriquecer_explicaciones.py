"""
Enriquecedor de Explicaciones para Base de Conocimiento TICD
Añade explicaciones detalladas a las respuestas cuando no las tienen
"""

import json
import re

# Diccionario de explicaciones por temas comunes
EXPLICACIONES_TEMATICAS = {
    # Hardware y Medidas
    "KB|bytes|bits|MB|GB|TB|PB": {
        "explicacion": "En informática, 1 KB = 1024 bytes, 1 MB = 1024 KB, 1 GB = 1024 MB, etc. Es importante recordar que se usa base 1024 (2^10) en lugar de 1000.",
        "contexto": "Unidades de medida digital"
    },
    "RAM|memoria.*": {
        "explicacion": "La memoria RAM (Random Access Memory) es la memoria principal donde se almacenan temporalmente los programas y datos en ejecución. Es volátil, lo que significa que pierde su contenido al apagar el ordenador.",
        "contexto": "Memoria del sistema"
    },
    "ROM": {
        "explicacion": "La memoria ROM (Read-Only Memory) es de solo lectura y contiene el firmware básico del sistema. No se borra al apagar el equipo.",
        "contexto": "Memoria permanente"
    },
    "caché": {
        "explicacion": "La memoria caché es una memoria ultrarrápida que almacena datos de uso frecuente para acelerar el acceso del procesador, reduciendo el tiempo de respuesta del sistema.",
        "contexto": "Optimización del rendimiento"
    },
    
    # Periféricos
    "periférico.*entrada": {
        "explicacion": "Los periféricos de entrada permiten introducir información al ordenador, como el teclado, ratón, escáner o micrófono.",
        "contexto": "Dispositivos de entrada"
    },
    "periférico.*salida": {
        "explicacion": "Los periféricos de salida permiten extraer información del ordenador, como el monitor, impresora o altavoces.",
        "contexto": "Dispositivos de salida"
    },
    
    # Sistemas operativos
    "sistema operativo": {
        "explicacion": "El sistema operativo es el software fundamental que gestiona los recursos del hardware y proporciona una interfaz para que otros programas y usuarios interactúen con el ordenador.",
        "contexto": "Software de sistema"
    },
    "driver|drivers": {
        "explicacion": "Los drivers (controladores) son programas que permiten al sistema operativo comunicarse con dispositivos hardware específicos, traduciendo las órdenes del SO al lenguaje del dispositivo.",
        "contexto": "Software de control de hardware"
    },
    "Plug.*Play": {
        "explicacion": "Plug and Play es una tecnología que permite al sistema operativo reconocer y configurar automáticamente dispositivos hardware sin necesidad de instalación manual.",
        "contexto": "Configuración automática de hardware"
    },
    
    # Redes
    "dirección IP|IP": {
        "explicacion": "Una dirección IP es un identificador único numérico asignado a cada dispositivo en una red. En IPv4 consta de 4 números del 0 al 255 separados por puntos (ej: 192.168.1.1).",
        "contexto": "Identificación en red"
    },
    "HTTP": {
        "explicacion": "HTTP (Hypertext Transfer Protocol) es el protocolo de comunicación que permite la transferencia de información en la World Wide Web, base del funcionamiento de Internet.",
        "contexto": "Protocolo de Internet"
    },
    "URL": {
        "explicacion": "URL (Uniform Resource Locator) es la dirección completa de un recurso en Internet, que especifica su ubicación y el protocolo para acceder a él (ej: https://www.ejemplo.com/pagina.html).",
        "contexto": "Direcciones web"
    },
    "DNS": {
        "explicacion": "DNS (Domain Name System) es el sistema que traduce nombres de dominio legibles (como google.com) en direcciones IP numéricas que los ordenadores utilizan para comunicarse.",
        "contexto": "Resolución de nombres"
    },
    "LAN": {
        "explicacion": "LAN (Local Area Network) es una red de área local que conecta ordenadores y dispositivos en un área geográfica limitada, como una casa, oficina o edificio.",
        "contexto": "Tipos de redes"
    },
    
    # Seguridad
    "spam": {
        "explicacion": "El spam es correo electrónico no solicitado enviado de forma masiva, generalmente con fines publicitarios o maliciosos. El antispam ayuda a filtrar estos mensajes.",
        "contexto": "Correo no deseado"
    },
    "phishing": {
        "explicacion": "El phishing es una técnica de fraude donde se suplanta la identidad de una entidad legítima para obtener información confidencial como contraseñas o datos bancarios.",
        "contexto": "Fraude electrónico"
    },
    "virus|antivirus": {
        "explicacion": "Los virus son programas maliciosos que se replican e infectan sistemas. Los antivirus son software diseñado para detectar, prevenir y eliminar estos programas dañinos.",
        "contexto": "Malware y protección"
    },
    "scam": {
        "explicacion": "Un scam es una estafa online diseñada para engañar a las víctimas y obtener dinero o información personal mediante engaños o promesas falsas.",
        "contexto": "Estafas online"
    },
    "hoax|bulo": {
        "explicacion": "Un hoax o bulo es información falsa difundida generalmente por correo electrónico o redes sociales, diseñada para engañar o alarmar a los usuarios.",
        "contexto": "Desinformación"
    },
    "troyano": {
        "explicacion": "Un troyano es un tipo de malware que se presenta como software legítimo pero que realiza acciones maliciosas en segundo plano, como robar información o abrir puertas traseras.",
        "contexto": "Malware engañoso"
    },
    "criptografía|encriptación": {
        "explicacion": "La criptografía es la técnica de proteger información transformándola mediante algoritmos matemáticos, de modo que solo quien tenga la clave correcta pueda leerla.",
        "contexto": "Protección de datos"
    },
    "firewall|cortafuegos": {
        "explicacion": "Un firewall o cortafuegos es un sistema de seguridad que controla el tráfico de red entrante y saliente, bloqueando accesos no autorizados y protegiendo contra amenazas.",
        "contexto": "Seguridad de red"
    },
    
    # Ofimática
    "hoja de cálculo|celda": {
        "explicacion": "En una hoja de cálculo, una celda es la unidad básica de almacenamiento, identificada por columna y fila (ej: A1, B5). Un rango es un conjunto de celdas (ej: B5:H8).",
        "contexto": "Hojas de cálculo"
    },
    "fórmula": {
        "explicacion": "Una fórmula en hojas de cálculo comienza siempre con el signo '=' y realiza cálculos usando operadores (+, -, *, /, ^) y referencias a celdas.",
        "contexto": "Cálculos en hojas de cálculo"
    },
    "diapositiva|transición": {
        "explicacion": "En presentaciones, la transición es el efecto visual que se produce al pasar de una diapositiva a otra. Ayuda a dar fluidez y dinamismo a la presentación.",
        "contexto": "Presentaciones"
    },
    "alineación.*justificada": {
        "explicacion": "La alineación justificada distribuye el texto de forma uniforme entre los márgenes izquierdo y derecho, creando una apariencia ordenada y profesional con los bordes rectos.",
        "contexto": "Formato de texto"
    },
    
    # Bases de datos
    "SGBD|base.*datos": {
        "explicacion": "Un SGBD (Sistema Gestor de Bases de Datos) es el software que permite crear, gestionar y consultar bases de datos de forma eficiente y segura.",
        "contexto": "Gestión de bases de datos"
    },
    "clave primaria": {
        "explicacion": "La clave primaria es un campo o conjunto de campos que identifica de forma única cada registro en una tabla de base de datos, garantizando que no haya duplicados.",
        "contexto": "Estructura de bases de datos"
    },
    
    # Multimedia
    "RGB": {
        "explicacion": "RGB (Red, Green, Blue) es un modelo de color que combina luz roja, verde y azul en diferentes proporciones para crear cualquier color visible en pantallas digitales.",
        "contexto": "Modelos de color"
    },
    "vectorial": {
        "explicacion": "Las imágenes vectoriales se definen mediante fórmulas matemáticas y pueden escalarse sin perder calidad, siendo ideales para logos y diseños. Ocupan menos espacio que las imágenes rasterizadas.",
        "contexto": "Tipos de imagen"
    },
    "GIF|JPG|JPEG|PNG|TIFF": {
        "explicacion": "Los formatos de imagen tienen diferentes características: JPG (alta compresión, fotos), PNG (transparencias, gráficos), GIF (animaciones, pocos colores), TIFF (sin compresión, alta calidad).",
        "contexto": "Formatos de imagen"
    },
    "compresión": {
        "explicacion": "La compresión reduce el tamaño de archivos multimedia eliminando o simplificando información, pudiendo ser con pérdida (menor calidad) o sin pérdida (calidad original).",
        "contexto": "Optimización de archivos"
    },
    "MP3|OGG|MIDI": {
        "explicacion": "Los formatos de audio varían: MP3 (comprimido con pérdida), OGG (alternativa libre), MIDI (almacena instrucciones musicales, no audio real).",
        "contexto": "Formatos de audio"
    },
    
    # Web 2.0
    "Web 2.0": {
        "explicacion": "La Web 2.0 se caracteriza por ser interactiva y colaborativa, donde los usuarios no solo consumen contenido sino que también lo crean y comparten.",
        "contexto": "Evolución de Internet"
    },
    "red social": {
        "explicacion": "Las redes sociales son plataformas online que permiten a los usuarios crear perfiles, conectar con otros, compartir contenido y comunicarse en comunidades virtuales.",
        "contexto": "Comunicación online"
    },
    "wiki": {
        "explicacion": "Una wiki es un sitio web colaborativo que permite a múltiples usuarios crear y editar contenido de forma colectiva, siendo Wikipedia el ejemplo más conocido.",
        "contexto": "Colaboración online"
    },
    "blog|post": {
        "explicacion": "Un blog es un sitio web con publicaciones (posts) ordenadas cronológicamente, donde el autor comparte opiniones, información o experiencias de forma regular.",
        "contexto": "Publicación online"
    },
    "foro": {
        "explicacion": "Un foro es una plataforma de discusión online donde los usuarios publican mensajes organizados por temas, permitiendo conversaciones asincrónicas en comunidad.",
        "contexto": "Comunidades online"
    },
    
    # Licencias
    "Creative Commons": {
        "explicacion": "Creative Commons es una organización que ofrece licencias flexibles para que los creadores compartan su trabajo permitiendo ciertos usos (comercial, derivados, etc.) según sus preferencias.",
        "contexto": "Licencias de contenido"
    },
    
    # Navegadores
    "navegador": {
        "explicacion": "Un navegador web es una aplicación que permite acceder, visualizar e interactuar con páginas web en Internet. Ejemplos: Chrome, Firefox, Safari, Edge.",
        "contexto": "Acceso a Internet"
    },
    
    # Extensiones y formatos
    "\\.txt": {
        "explicacion": "Los archivos .txt son archivos de texto plano sin formato que pueden ser abiertos por cualquier editor de texto básico como el Bloc de Notas.",
        "contexto": "Formato de texto"
    },
    "\\.ods": {
        "explicacion": "ODS (OpenDocument Spreadsheet) es el formato estándar de hojas de cálculo de LibreOffice Calc y OpenOffice Calc.",
        "contexto": "Formato de hoja de cálculo"
    },
    "\\.odp": {
        "explicacion": "ODP (OpenDocument Presentation) es el formato estándar de presentaciones de LibreOffice Impress y OpenOffice Impress.",
        "contexto": "Formato de presentación"
    },
    "\\.odt": {
        "explicacion": "ODT (OpenDocument Text) es el formato estándar de documentos de texto de LibreOffice Writer y OpenOffice Writer.",
        "contexto": "Formato de documento de texto"
    },
    "\\.odb": {
        "explicacion": "ODB (OpenDocument Base) es el formato de base de datos de LibreOffice Base y OpenOffice Base.",
        "contexto": "Formato de base de datos"
    },
    
    # Almacenamiento
    "USB|flash": {
        "explicacion": "Las memorias USB o flash utilizan memoria de estado sólido para almacenar datos de forma portable, sin partes móviles, siendo resistentes y compactas.",
        "contexto": "Almacenamiento portable"
    },
    "DVD|CD|óptico": {
        "explicacion": "Los dispositivos ópticos (CD, DVD, Blu-ray) almacenan información mediante tecnología láser, leyendo y escribiendo datos en discos mediante cambios de reflectividad.",
        "contexto": "Almacenamiento óptico"
    },
    "disco duro": {
        "explicacion": "Un disco duro tradicional (HDD) almacena datos magnéticamente en platos giratorios. Los SSD modernos usan memoria flash, siendo más rápidos pero más caros.",
        "contexto": "Almacenamiento interno"
    }
}

def encontrar_explicacion_tematica(texto_pregunta, texto_respuesta):
    """Busca una explicación temática relevante según el contenido de la pregunta"""
    texto_completo = f"{texto_pregunta} {texto_respuesta}".lower()
    
    for patron, info in EXPLICACIONES_TEMATICAS.items():
        if re.search(patron.lower(), texto_completo):
            return info["explicacion"]
    
    return None

def enriquecer_explicaciones(archivo_entrada, archivo_salida):
    """Enriquece las explicaciones de la base de conocimiento"""
    
    # Cargar base de conocimiento
    with open(archivo_entrada, 'r', encoding='utf-8') as f:
        base = json.load(f)
    
    mejoradas = 0
    sin_cambios = 0
    
    for pregunta in base['preguntas']:
        explicacion_actual = pregunta.get('explicacion', '').strip()
        
        # Si no tiene explicación o es muy genérica, buscar una mejor
        if not explicacion_actual or explicacion_actual.startswith('La respuesta correcta es'):
            respuesta_correcta = pregunta.get('respuesta_correcta', '')
            texto_respuesta = pregunta['opciones'].get(respuesta_correcta, '')
            
            # Buscar explicación temática
            nueva_explicacion = encontrar_explicacion_tematica(
                pregunta['pregunta'],
                texto_respuesta
            )
            
            if nueva_explicacion:
                # Combinar con la respuesta correcta
                pregunta['explicacion'] = f"La respuesta correcta es '{respuesta_correcta}': {texto_respuesta}. {nueva_explicacion}"
                mejoradas += 1
            elif not explicacion_actual:
                # Si no hay explicación en absoluto, crear una básica
                pregunta['explicacion'] = f"La respuesta correcta es '{respuesta_correcta}': {texto_respuesta}"
                mejoradas += 1
            else:
                sin_cambios += 1
        else:
            sin_cambios += 1
    
    # Guardar base de conocimiento enriquecida
    with open(archivo_salida, 'w', encoding='utf-8') as f:
        json.dump(base, f, indent=2, ensure_ascii=False)
    
    print(f"\n✓ Base de conocimiento enriquecida guardada en: {archivo_salida}")
    print(f"  - Explicaciones mejoradas: {mejoradas}")
    print(f"  - Sin cambios: {sin_cambios}")
    print(f"  - Total preguntas: {len(base['preguntas'])}")

def main():
    archivo_entrada = "base_conocimiento_ticd.json"
    archivo_salida = "base_conocimiento_ticd.json"
    
    enriquecer_explicaciones(archivo_entrada, archivo_salida)

if __name__ == "__main__":
    main()
