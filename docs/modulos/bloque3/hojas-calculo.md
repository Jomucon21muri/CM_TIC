# 3.3. Hojas de Cálculo

Programas para organizar, analizar y representar datos numéricos.

**Ejemplos:** Microsoft Excel, LibreOffice Calc, Google Sheets

## Conceptos Básicos

- **Libro:** Archivo que contiene una o más hojas
- **Hoja:** Tabla compuesta de celdas organizadas en filas y columnas
- **Celda:** Intersección de una fila y columna (ej: A1, B5)
- **Rango:** Grupo de celdas (ej: A1:C10)

## Operadores

- **Aritméticos:** + (suma), - (resta), * (multiplicación), / (división), ^ (potencia)
- **Comparación:** = (igual), > (mayor), < (menor), >= (mayor o igual), <= (menor o igual), <> (diferente)
- **Texto:** & (concatenar)
- **Lógicos:** Y (AND), O (OR), NO (NOT)

## Fórmulas

- Expresión que realiza cálculos con valores de la hoja
- Siempre comienzan con **=**
- Ejemplos:
    - `=A1+B1` (suma dos celdas)
    - `=A1*B1` (multiplica dos celdas)
    - `=(A1+A2)/2` (media de dos valores)

## Funciones

Fórmulas predefinidas que realizan cálculos complejos.

### Funciones Matemáticas

- `=SUMA(A1:A10)` - Suma un rango de celdas
- `=PROMEDIO(A1:A10)` - Calcula la media
- `=MAX(A1:A10)` - Valor máximo
- `=MIN(A1:A10)` - Valor mínimo
- `=REDONDEAR(A1, 2)` - Redondea a 2 decimales
- `=POTENCIA(2, 3)` - 2 elevado a 3
- `=RAIZ(25)` - Raíz cuadrada de 25

### Funciones Estadísticas

- `=CONTAR(A1:A10)` - Cuenta celdas con números
- `=CONTARA(A1:A10)` - Cuenta celdas no vacías
- `=CONTAR.SI(A1:A10, ">5")` - Cuenta celdas que cumplen condición

### Funciones Lógicas

- `=SI(A1>10, "Aprobado", "Suspenso")` - Condicional
- `=Y(A1>0, A1<10)` - Verdadero si ambas condiciones se cumplen
- `=O(A1>10, B1>10)` - Verdadero si alguna condición se cumple

### Funciones de Texto

- `=CONCATENAR(A1, " ", B1)` - Une textos
- `=MAYUSC(A1)` - Convierte a mayúsculas
- `=MINUSC(A1)` - Convierte a minúsculas
- `=LARGO(A1)` - Longitud del texto

### Funciones de Fecha y Hora

- `=HOY()` - Fecha actual
- `=AHORA()` - Fecha y hora actuales
- `=AÑO(A1)` - Extrae el año de una fecha
- `=MES(A1)` - Extrae el mes
- `=DIA(A1)` - Extrae el día

### Funciones de Búsqueda

- `=BUSCARV(valor, rango, columna, FALSO)` - Busca valor verticalmente
- `=BUSCARH(valor, rango, fila, FALSO)` - Busca valor horizontalmente

## Referencias de Celdas

### Relativas (A1)

- Cambian al copiar la fórmula
- Ejemplo: Si `=A1+B1` está en C1 y se copia a C2, se convierte en `=A2+B2`

### Absolutas ($A$1)

- No cambian al copiar la fórmula
- Se usan con el símbolo $
- Ejemplo: `=$A$1*B1` siempre referencia A1

### Mixtas ($A1 o A$1)

- `$A1` - Columna fija, fila relativa
- `A$1` - Fila fija, columna relativa

## Gráficos

Representación visual de datos.

### Tipos de Gráficos

- **Columnas/Barras:** Comparar valores entre categorías
- **Líneas:** Mostrar tendencias a lo largo del tiempo
- **Circular (Sectores/Pastel):** Mostrar porcentajes de un total
- **Dispersión (XY):** Relación entre dos variables
- **Área:** Similar a líneas pero con área sombreada

### Elementos de un Gráfico

- Título del gráfico
- Ejes (X e Y) con etiquetas
- Leyenda
- Etiquetas de datos
- Líneas de cuadrícula

## Otras Funciones

- **Formato condicional:** Cambia aspecto de celdas según su valor
- **Ordenar:** Datos ascendente o descendentemente
- **Filtrar:** Mostrar solo filas que cumplen criterios
- **Validación de datos:** Limitar qué se puede introducir en una celda
- **Tablas dinámicas:** Resumen y análisis avanzado de datos

---

[← Anterior: Procesadores de Texto](procesadores-texto.md){ .md-button } [Siguiente: Bases de Datos →](bases-datos.md){ .md-button .md-button--primary }
