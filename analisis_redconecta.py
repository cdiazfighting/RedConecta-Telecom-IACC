
import pandas as pd
import matplotlib.pyplot as plt

# Cargo el archivo Excel
df = pd.read_excel("dataset_set_D_telecomunicaciones.xlsx")

# Reviso  los datos
print("Cantidad de registros:", len(df))
print("Cantidad de columnas:", len(df.columns))

print("\nPrimeros 5 registros:")
print(df.head())

# Verifico si existen datos vacíos
print("\nDatos vacíos:")
print(df.isnull().sum())

# Latencia promedio por región
latencia_region = df.groupby("region")["latencia_ms"].mean()

print("\nLatencia promedio por región:")
print(latencia_region.round(2))

# Incidencias por región
incidencias_region = df.groupby("region")[
    "incidencias_reportadas"
].sum()

print("\nIncidencias por región:")
print(incidencias_region)

# Tiempo promedio de resolución por servicio
tiempo_servicio = df.groupby("tipo_servicio")[
    "tiempo_resolucion_hr"
].mean()

print("\nTiempo promedio de resolución:")
print(tiempo_servicio.round(2))

# Cumplimiento de SLA
print("\nCumplimiento de SLA:")
print(df["cumplimiento_sla"].value_counts())


# adiero el otro codigo aca de los graficos


# Creo el dashboard con cuatro gráficos
fig, graficos = plt.subplots(2, 2, figsize=(13, 9))

# Gráfico 1: latencia por región
latencia_region.plot(
    kind="bar", ax=graficos[0, 0]
)
graficos[0, 0].set_title("Latencia promedio por región")
graficos[0, 0].set_ylabel("Milisegundos")
graficos[0, 0].set_xlabel("Región")

# Gráfico 2: incidencias por región
incidencias_region.plot(
    kind="bar", ax=graficos[0, 1]
)
graficos[0, 1].set_title("Incidencias por región")
graficos[0, 1].set_ylabel("Cantidad")
graficos[0, 1].set_xlabel("Región")

# Gráfico 3: tiempo promedio de resolución
tiempo_servicio.plot(
    kind="bar", ax=graficos[1, 0]
)
graficos[1, 0].set_title("Tiempo de resolución por servicio")
graficos[1, 0].set_ylabel("Horas")
graficos[1, 0].set_xlabel("Tipo de servicio")

# Gráfico 4: cumplimiento de SLA
df["cumplimiento_sla"].value_counts().plot(
    kind="pie",
    autopct="%1.1f%%",
    ax=graficos[1, 1]
)
graficos[1, 1].set_title("Cumplimiento de SLA")
graficos[1, 1].set_ylabel("")

plt.tight_layout()
plt.savefig("dashboard_redconecta.png", dpi=150)
plt.show()



# ---------------------------------------
# Reporte para el área de Soporte Técnico
# ---------------------------------------

# Seleciono  las columnas necesarias
soporte = df[[
    "fecha_registro",
    "region",
    "tipo_servicio",
    "incidencias_reportadas",
    "tickets_soporte",
    "tiempo_resolucion_hr"
]]

# Guardamos el reporte en Excel
soporte.to_excel(
    "reporte_soporte_tecnico.xlsx",
    index=False
)

print("Reporte de Soporte Técnico generado")


# ---------------------------------------
# Reporte para Experiencia de Clientes
# ---------------------------------------

# seleciono los datos de los clientes
clientes = df[[
    "fecha_registro",
    "tipo_servicio",
    "clientes_afectados",
    "latencia_ms",
    "cumplimiento_sla"
]]

# Guardo el segundo reporte en Excel
clientes.to_excel(
    "reporte_experiencia_clientes.xlsx",
    index=False
)

print("Reporte de Experiencia de Clientes generado")




# ---------------------------------------
# Pregunta 4 - Funciones reutilizables
# ---------------------------------------

from funciones.funciones_analisis import (
    calcular_promedio,
    detectar_atipicos,
    guardar_resultados
)

import os

# Creo carpeta para los resultados
os.makedirs("resultados", exist_ok=True)

# Calculo promedios usando NumPy
promedio_latencia = calcular_promedio(df, "latencia_ms")

promedio_resolucion = calcular_promedio(
    df, "tiempo_resolucion_hr"
)

print("\n--- Análisis con NumPy ---")
print("Latencia promedio:", round(promedio_latencia, 2))
print("Tiempo promedio de resolución:", round(promedio_resolucion, 2))


# Buscamos valores atípicos con SciPy
atipicos = detectar_atipicos(df, "latencia_ms")

print("\n--- Análisis con SciPy ---")
print("Posibles valores atípicos de latencia:", len(atipicos))

# Guardamos los registros encontrados en Excel
atipicos.to_excel(
    "resultados/latencias_atipicas.xlsx",
    index=False
)


# Guardamos un resumen con Joblib
resumen = {
    "latencia_promedio": float(promedio_latencia),
    "tiempo_resolucion_promedio": float(promedio_resolucion),
    "cantidad_atipicos": len(atipicos)
}

guardar_resultados(
    resumen,
    "resultados/resumen_redconecta.joblib"
)
