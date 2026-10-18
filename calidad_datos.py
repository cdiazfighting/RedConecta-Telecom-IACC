
import pandas as pd

# Cargamos el archivo de la empresa
df = pd.read_excel("dataset_set_D_telecomunicaciones.xlsx")

# Revisamos la calidad de los datos
print("Total de registros:", len(df))
print("Datos vacíos:", df.isnull().sum().sum())
print("Registros duplicados:", df.duplicated().sum())

# Revisamos valores negativos
columnas = [
    "trafico_datos_gb",
    "latencia_ms",
    "incidencias_reportadas",
    "tickets_soporte",
    "tiempo_resolucion_hr",
    "clientes_afectados"
]

negativos = (df[columnas] < 0).sum().sum()
print("Valores negativos:", negativos)

# Buscamos registros que debemos revisar
revision = df[
    (df["incidencias_reportadas"] == 0) &
    (df["tickets_soporte"] > 0)
]

print("Registros para revisar:", len(revision))

# Guardamos los posibles casos para revisar
revision.to_excel(
    "resultados/registros_para_revision.xlsx",
    index=False
)
