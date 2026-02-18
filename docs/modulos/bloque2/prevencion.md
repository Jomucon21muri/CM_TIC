# Estrategias de Protección y Prevención

## Copias de Seguridad (Backup)

Una **copia de seguridad** es una copia de los datos almacenada en un lugar diferente al original para poder recuperarla en caso de pérdida.

### Tipos de Copias de Seguridad

- **Completa:** Copia de todos los datos. Lenta pero completa
- **Incremental:** Solo copia lo que ha cambiado desde la última copia
- **Diferencial:** Copia lo que ha cambiado desde la última copia completa

### Regla 3-2-1 para Backups

!!! success "Regla 3-2-1"
    - **3** copias de tus datos (original + 2 copias)
    - **2** soportes diferentes (disco duro + nube, por ejemplo)
    - **1** copia fuera del sitio (offsite backup)

### Restauración

Proceso de recuperar los datos desde una copia de seguridad cuando se han perdido o dañado.

## Herramientas de Protección

### Antivirus

- Detecta, previene y elimina software malicioso (malware)
- Debe mantenerse actualizado constantemente
- Escaneo en tiempo real y bajo demanda
- Ejemplos: Windows Defender, Avast, Norton, Kaspersky

### Cortafuegos (Firewall)

- Controla el tráfico de red entrante y saliente
- Bloquea conexiones no autorizadas
- Puede ser hardware (en router) o software (en ordenador)
- Windows incluye firewall integrado

### Antiespías (Anti-spyware)

- Detecta y elimina software espía (spyware)
- El spyware recopila información sin consentimiento
- Ejemplos: Malwarebytes, Spybot Search & Destroy

### Antispam

- Filtra correos electrónicos no deseados
- Reduce el riesgo de phishing y malware
- Integrado en la mayoría de servicios de correo

## Actualizaciones de Software

- Mantener sistema operativo y aplicaciones actualizadas
- Los parches de seguridad corrigen vulnerabilidades
- Configurar actualizaciones automáticas cuando sea posible

## Encriptación/Cifrado

La **encriptación** es el proceso de convertir información legible en formato codificado que solo puede leerse con la clave correcta.

### Tipos de Cifrado

#### Cifrado simétrico

La misma clave para cifrar y descifrar (AES, DES)

- Más rápido
- Problema: compartir la clave de forma segura

#### Cifrado asimétrico

Clave pública (cifrar) y privada (descifrar) (RSA)

- Más seguro para transmisión
- Más lento
- Usado en HTTPS, email certificado

### Aplicaciones del Cifrado

- **HTTPS:** Navegación web segura (certificado SSL/TLS)
- **VPN:** Conexiones privadas virtuales
- **Cifrado de disco:** BitLocker (Windows), FileVault (macOS)
- **Mensajería cifrada:** WhatsApp, Signal (cifrado end-to-end)

## Contraseñas Seguras

!!! success "Características de una Buena Contraseña"
    - **Longitud:** Mínimo 12-16 caracteres
    - **Complejidad:** Mayúsculas, minúsculas, números y símbolos
    - **Impredecible:** No usar palabras del diccionario ni datos personales
    - **Única:** Diferente para cada servicio
    - **Ejemplos de MAL contraseña:** 12345678, contraseña, nombre123
    - **Ejemplo de BUENA contraseña:** T7$mK9@pL3#qW2

### Gestores de Contraseñas

- Almacenan todas las contraseñas de forma cifrada
- Solo necesitas recordar una contraseña maestra
- Generan contraseñas aleatorias fuertes
- Ejemplos: LastPass, 1Password, Bitwarden, KeePass

## Autenticación de Dos Factores (2FA)

Añade una segunda capa de seguridad además de la contraseña:

- **Algo que sabes:** Contraseña
- **Algo que tienes:** Móvil (código SMS o app autenticadora)
- **Algo que eres:** Huella dactilar, reconocimiento facial

## Certificados Digitales

- Documento electrónico que verifica la identidad
- Usado para firmar documentos digitalmente
- Ejemplos: DNI electrónico, certificados de la FNMT

## Navegación Segura

- Verificar HTTPS (candado verde en navegador)
- No conectarse a redes Wi-Fi públicas sin VPN
- Borrar cookies y caché periódicamente
- Usar modo de navegación privada/incógnito cuando sea necesario
- Mantener navegador actualizado
- Instalar extensiones de seguridad (bloqueadores de anuncios, anti-tracking)

---

[← Tipos de Malware](malware.md) | [Inicio](../../index.md) | [Propiedad Intelectual →](propiedad-intelectual.md)
