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
    # Crear la carpeta si no existe
    os.makedirs('outputs/graficas/', exist_ok=True)
    # Generar y guardar las gráficas
    plt.figure(figsize=(10, 5))
    plt.plot(df['Mes'], df['Ventas'], marker='o')
    plt.title('Ventas Mensuales')
    plt.xlabel('Mes')
    plt.ylabel('Ventas')
    plt.grid(True)
    plt.savefig('outputs/graficas/ventas_mensuales.png')
