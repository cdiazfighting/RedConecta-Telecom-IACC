
import numpy as np
from scipy import stats
import joblib


# Calcula el promedio de una columna
def calcular_promedio(datos, columna):
    valores = datos[columna].dropna().to_numpy()
    return np.mean(valores)


# Busca posibles valores atípicos
def detectar_atipicos(datos, columna):
    valores = datos[columna].dropna()

    # Comprobamos que existan datos y variación
    if len(valores) < 2 or valores.std() == 0:
        return datos.iloc[0:0].copy()

    # Calculamos el puntaje Z con SciPy
    puntajes = stats.zscore(valores.to_numpy())

    # Seleccionamos valores con Z mayor a 3
    posiciones = np.abs(puntajes) > 3

    return datos.loc[valores.index[posiciones]]


# Guarda los resultados para utilizarlos después
def guardar_resultados(resultados, archivo):
    joblib.dump(resultados, archivo)
    print("Resultados guardados en:", archivo)
