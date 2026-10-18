
import nbformat as nbf

notebook = nbf.v4.new_notebook()

notebook.cells = [
    nbf.v4.new_markdown_cell(
        "# Análisis de RedConecta Telecom\n"
        "Proyecto de Ciencia de Datos - Semana 8 IACC\n\n"
        "Objetivo: analizar latencia, incidencias y SLA."
    ),

    nbf.v4.new_code_cell(
        "import pandas as pd\n"
        "import matplotlib.pyplot as plt\n"
        "df = pd.read_excel('dataset_set_D_telecomunicaciones.xlsx')\n"
        "print('Registros:', len(df))\n"
        "display(df.head())"
    ),

    nbf.v4.new_code_cell(
        "print('Incidencias por región:')\n"
        "display(df.groupby('region')['incidencias_reportadas'].sum())\n"
        "print('Tiempo promedio de resolución:')\n"
        "display(df.groupby('tipo_servicio')['tiempo_resolucion_hr'].mean())\n"
        "print('Cumplimiento SLA:')\n"
        "display(df['cumplimiento_sla'].value_counts())"
    ),

    nbf.v4.new_code_cell(
        "fig, ax = plt.subplots(1, 2, figsize=(11, 4))\n"
        "df.groupby('region')['latencia_ms'].mean().plot("
        "kind='bar', ax=ax[0], title='Latencia por región')\n"
        "df['cumplimiento_sla'].value_counts().plot("
        "kind='pie', autopct='%1.1f%%', ax=ax[1], "
        "title='Cumplimiento SLA')\n"
        "ax[0].set_ylabel('Latencia (ms)')\n"
        "ax[1].set_ylabel('')\n"
        "plt.tight_layout()\n"
        "plt.show()"
    )
]

notebook.metadata["kernelspec"] = {
    "display_name": "Python 3",
    "language": "python",
    "name": "python3"
}

nbf.write(notebook, "analisis_redconecta.ipynb")
print("Notebook creado correctamente")
