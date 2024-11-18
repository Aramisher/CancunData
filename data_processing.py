import pandas as pd
import matplotlib.pyplot as plt
from error_handling import validar_datos
from error_handling import guardar_reporte_errores
import os

def procesar_datos(ruta_archivo):
    try:
        df = pd.read_excel(ruta_archivo)
        errores = validar_datos(df)
        if errores:
            guardar_reporte_errores(errores)
            return errores
        else:
            generar_graficas(df)
            return None
    except Exception as e:
        print(f"Ocurrió un error al procesar los datos: {e}")
        return [str(e)]

def generar_graficas(df):
    import os
    import matplotlib.pyplot as plt

    # Crear la carpeta si no existe
    os.makedirs('outputs/graficas/', exist_ok=True)

    # Determinar el eje X (Meses o Fecha)
    if 'Mes' in df.columns:
        eje_x = df['Mes']
    elif 'Fecha' in df.columns:
        eje_x = df['Fecha']
    else:
        eje_x = df.index  # Usar el índice si no hay columna de tiempo

    # Obtener todas las columnas numéricas excepto el eje X
    columnas_numericas = df.select_dtypes(include='number').columns.tolist()
    columnas_numericas = [col for col in columnas_numericas if col != 'Mes' and col != 'Fecha']

    # Generar gráficas para cada columna numérica
    for columna in columnas_numericas:
        plt.figure(figsize=(10, 5))
        plt.plot(eje_x, df[columna], marker='o')
        plt.title(f'{columna} Mensuales')
        plt.xlabel('Mes')
        plt.ylabel(columna)
        plt.grid(True)
        plt.savefig(f'outputs/graficas/{columna.lower()}_mensuales.png')
        plt.close()
