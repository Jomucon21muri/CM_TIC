# 1.8. Configuración Básica de Redes TCP/IP

## Protocolo TCP/IP

El **TCP/IP** (Transmission Control Protocol/Internet Protocol) es el conjunto de protocolos fundamentales que permite la comunicación en Internet y redes locales.

## Dirección IP

Una **dirección IP** es un identificador único para cada dispositivo conectado a una red.

### IPv4 (Internet Protocol version 4)

- Formato: 4 números separados por puntos (0-255)
- Ejemplo: 192.168.1.100
- Total de direcciones: aproximadamente 4.300 millones

### IPv6 (Internet Protocol version 6)

- Formato: 8 grupos de 4 dígitos hexadecimales
- Ejemplo: 2001:0db8:85a3:0000:0000:8a2e:0370:7334
- Creado para solucionar la escasez de direcciones IPv4

### Clases de Direcciones IP (IPv4)

- **Clase A:** 1.0.0.0 a 126.255.255.255 (redes muy grandes)
- **Clase B:** 128.0.0.0 a 191.255.255.255 (redes medianas)
- **Clase C:** 192.0.0.0 a 223.255.255.255 (redes pequeñas)

### Direcciones IP Privadas

Rangos reservados para redes locales (no enrutables en Internet):

- Clase A: 10.0.0.0 a 10.255.255.255
- Clase B: 172.16.0.0 a 172.31.255.255
- Clase C: 192.168.0.0 a 192.168.255.255

## Máscara de Subred

La **máscara de subred** determina qué parte de la dirección IP corresponde a la red y cuál al host.

- Ejemplo: 255.255.255.0
- Permite dividir una red en subredes más pequeñas

## Puerta de Enlace (Gateway)

- Dirección IP del router que conecta la red local con otras redes
- Ejemplo: 192.168.1.1

## Servidor DNS

El **DNS** (Domain Name System) traduce nombres de dominio (www.google.com) a direcciones IP.

- Ejemplos de servidores DNS públicos:
    - Google DNS: 8.8.8.8 y 8.8.4.4
    - Cloudflare: 1.1.1.1

## DHCP (Dynamic Host Configuration Protocol)

- Asigna automáticamente direcciones IP a dispositivos en la red
- Evita tener que configurar manualmente cada dispositivo
- Normalmente está en el router

## Configuración Típica en una Red Doméstica

!!! info "Configuración de Ejemplo"
    - **Dirección IP:** 192.168.1.100 (asignada por DHCP)
    - **Máscara de subred:** 255.255.255.0
    - **Puerta de enlace:** 192.168.1.1 (router)
    - **DNS:** 192.168.1.1 o 8.8.8.8

---

[:octicons-arrow-right-24: Siguiente: Actividades](actividades.md){ .md-button .md-button--primary }
[:octicons-arrow-left-24: Anterior: Dispositivos de Red](dispositivos-red.md){ .md-button }
