# 3.5. Bases de Datos

Sistema para almacenar, organizar y gestionar grandes cantidades de información estructurada.

**Ejemplos:** Microsoft Access, LibreOffice Base, MySQL, SQL Server

## Conceptos Básicos

- **Base de datos:** Conjunto organizado de datos relacionados
- **Tabla:** Estructura que contiene datos sobre un tema específico
- **Registro (Fila):** Conjunto de datos sobre una entidad individual
- **Campo (Columna):** Cada tipo de información en un registro
- **Tipo de dato:** Texto, número, fecha, sí/no, etc.

## Diseño de una Base de Datos

### Ejemplo: Base de Datos de una Biblioteca

- **Tabla Libros:** ID_Libro, Título, ISBN, Año_Publicación, ID_Editorial
- **Tabla Autores:** ID_Autor, Nombre, Apellidos, Nacionalidad
- **Tabla Préstamos:** ID_Préstamo, ID_Libro, ID_Usuario, Fecha_Préstamo, Fecha_Devolución

## Campos Clave

- **Clave primaria (Primary Key):** Campo que identifica de forma única cada registro
    - No puede repetirse ni estar vacía
    - Ejemplo: ID_Cliente, DNI
- **Clave externa/foránea (Foreign Key):** Campo que relaciona con otra tabla
    - Referencia a la clave primaria de otra tabla
    - Establece relaciones entre tablas

## Relaciones entre Tablas

- **Uno a Uno (1:1):** Un registro en A se relaciona con un registro en B
- **Uno a Muchos (1:N):** Un registro en A se relaciona con varios en B
    - Ejemplo: Un autor puede tener muchos libros
- **Muchos a Muchos (N:M):** Varios registros en A con varios en B
    - Requiere tabla intermedia
    - Ejemplo: Libros y Autores (un libro puede tener varios autores)

## Integridad Referencial

- Garantiza que las relaciones entre tablas sean válidas
- No se puede eliminar un registro si tiene registros relacionados
- No se puede crear una relación con un registro inexistente

## Operaciones Básicas

### Consultas

- Recuperan información de la base de datos
- Pueden filtrar, ordenar y combinar datos de varias tablas
- Lenguaje SQL: `SELECT * FROM Clientes WHERE Ciudad='Valencia'`

### Formularios

- Interfaz amigable para introducir y visualizar datos
- Facilitan el trabajo con registros individuales
- Pueden incluir botones, listas desplegables

### Informes (Reports)

- Presentan datos de forma estructurada para imprimir
- Pueden agrupar, calcular totales y subtotales
- Formato profesional

## Ordenación y Filtros

- **Ordenar:** Ascendente (A-Z, 0-9) o descendente (Z-A, 9-0)
- **Filtros:** Mostrar solo registros que cumplen criterios
    - Por selección
    - Por formulario
    - Avanzados (con operadores lógicos)

---

[← Anterior: Hojas de Cálculo](hojas-calculo.md){ .md-button } [Siguiente: Presentaciones →](presentaciones.md){ .md-button .md-button--primary }
