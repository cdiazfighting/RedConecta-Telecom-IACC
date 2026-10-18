
# Proyecto de Ciencia de Datos - RedConecta Telecom

## 1. Descripción del proyecto

Este proyecto corresponde a la semana 8 de Ciencia de Datos
de IACC. Se analiza la información operacional de la empresa
RedConecta Telecom S. A. utilizando Python.

## 2. Objetivo

Analizar el comportamiento de los servicios de telecomunicaciones
para identificar posibles problemas relacionados con la latencia,
las incidencias, los tiempos de resolución y el cumplimiento de SLA.

## 3. Datos utilizados

Se utiliza el archivo dataset_set_D_telecomunicaciones.xlsx.

El archivo contiene 200 registros y 10 columnas.

Entre los datos disponibles se encuentran:

- Fecha de registro
- Región
- Tipo de servicio
- Tráfico de datos
- Latencia
- Incidencias reportadas
- Tickets de soporte
- Tiempo de resolución
- Clientes afectados
- Cumplimiento de SLA

## 4. Herramientas utilizadas

- Python: lenguaje de programación
- Pandas: carga y análisis del Excel
- Matplotlib: generación de gráficos
- OpenPyXL: lectura y escritura de Excel
- Git: control de versiones
- GitHub: almacenamiento y publicación del proyecto

## 5. Etapas del análisis

### Carga de datos

Se utiliza Pandas para leer el archivo Excel.

### Revisión de los datos

Se comprueba la cantidad de registros, las columnas
y si existen datos vacíos.

### Análisis

Se agrupan los datos por región y tipo de servicio.

Se calculan promedios de latencia, tiempos de resolución
y cantidad de incidencias.

### Visualización

Se construye un dashboard con cuatro gráficos:

1. Latencia promedio por región
2. Incidencias por región
3. Tiempo de resolución por servicio
4. Cumplimiento de SLA

### Generación de reportes

Se generan dos archivos Excel:

- reporte_soporte_tecnico.xlsx
- reporte_experiencia_clientes.xlsx

## 6. Resultados obtenidos

### Incidencias por región

- Centro: 862
- Norte: 848
- Sur: 999

La región Sur presenta la mayor cantidad de
incidencias reportadas.

### Tiempo promedio de resolución

- Empresas: 25,56 horas
- Internet Hogar: 24,46 horas
- Móvil: 26,28 horas

El servicio Móvil presenta el tiempo promedio
de resolución más alto.

### Cumplimiento de SLA

- Cumple: 96 registros (48 %)
- No cumple: 104 registros (52 %)

El porcentaje de incumplimiento es mayor
que el porcentaje de cumplimiento.

## 7. Cómo ejecutar el proyecto

Primero se debe crear y activar un entorno virtual:

python3 -m venv .venv
source .venv/bin/activate

Luego instalar las librerías:

python -m pip install -r requirements.txt

Finalmente ejecutar el programa:

python analisis_redconecta.py

## 8. Actualización de los datos

Cuando existan nuevos registros, se puede actualizar
el archivo Excel manteniendo los mismos nombres de columnas.

Después se debe ejecutar nuevamente el programa para
obtener los resultados actualizados.

Antes de analizar los nuevos registros, es importante
revisar su calidad y verificar que no existan errores.

## 9. Consideraciones éticas

Los resultados deben interpretarse considerando
las características y limitaciones de los datos.

No es recomendable tomar decisiones basándose
solamente en un indicador.

También es importante proteger la información
de los clientes y evitar publicar datos personales.

## 10. Conclusión

El análisis permite conocer algunas diferencias entre
regiones y tipos de servicio.

Los resultados pueden ayudar a identificar problemas
y orientar posibles mejoras en la atención y calidad
del servicio.

La documentación facilita que otras personas puedan
comprender el proyecto y continuar trabajando con él.
