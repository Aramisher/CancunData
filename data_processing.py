import pandas as pd
import matplotlib.pyplot as plt
from error_handling import validar_datos, guardar_reporte_errores
import os


def procesar_datos(ruta_archivo, tipo_grafica="linea", modo="independiente", carpeta_salida="outputs/graficas"):
    """
    Procesa los datos de un archivo Excel, valida y genera gráficas según las opciones del usuario.
    :param ruta_archivo: Ruta del archivo Excel.
    :param tipo_grafica: Tipo de gráfica ('linea' o 'barras').
    :param modo: Modo de visualización ('independiente', 'acumulativo' o 'ambos').
    :param carpeta_salida: Carpeta donde se guardarán las gráficas.
    :return: Lista de errores encontrados, o None si no hay errores.
    """
    try:
        # Leer el archivo Excel
        df = pd.read_excel(ruta_archivo)

        # Validar datos
        errores = validar_datos(df)
        if errores:
            guardar_reporte_errores(errores)
            return errores
        else:
            generar_graficas(df, tipo_grafica, modo, carpeta_salida)
            return None
    except Exception as e:
        print(f"Ocurrió un error al procesar los datos: {e}")
        return [str(e)]


def generar_graficas(df, tipo_grafica="linea", modo="independiente", carpeta_salida="outputs/graficas"):
    """
    Genera gráficas para cada columna del DataFrame según el tipo y modo seleccionados.
    :param df: DataFrame con los datos.
    :param tipo_grafica: Tipo de gráfica ('linea' o 'barras').
    :param modo: Modo de visualización ('independiente', 'acumulativo' o 'ambos').
    :param carpeta_salida: Carpeta donde se guardarán las gráficas.
    """
    os.makedirs(carpeta_salida, exist_ok=True)

    # Asumimos que la primera columna es el eje X (como "Mes")
    eje_x = df.iloc[:, 0]  # Primera columna
    columnas = df.columns[1:]  # Todas las demás columnas

    for columna in columnas:
        # Independiente
        if modo in ["independiente", "ambos"]:
            if tipo_grafica == "linea":
                plt.figure(figsize=(10, 5))
                plt.plot(eje_x, df[columna], marker='o', label=f"{columna} Independiente")
                plt.title(f'{columna} Mensual (Independiente)')
                plt.xlabel(eje_x.name)
                plt.ylabel(columna)
                plt.legend()
                plt.grid(True)
                plt.savefig(f'{carpeta_salida}/{columna}_independiente_linea.png')
                plt.close()
            elif tipo_grafica == "barras":
                plt.figure(figsize=(10, 5))
                plt.bar(eje_x, df[columna], label=f"{columna} Independiente")
                plt.title(f'{columna} Mensual (Independiente)')
                plt.xlabel(eje_x.name)
                plt.ylabel(columna)
                plt.legend()
                plt.savefig(f'{carpeta_salida}/{columna}_independiente_barras.png')
                plt.close()

        # Acumulativo
        if modo in ["acumulativo", "ambos"]:
            acumulativo = df[columna].cumsum()
            if tipo_grafica == "linea":
                plt.figure(figsize=(10, 5))
                plt.plot(eje_x, acumulativo, marker='o', label=f"{columna} Acumulativo")
                plt.title(f'{columna} Mensual (Acumulativo)')
                plt.xlabel(eje_x.name)
                plt.ylabel(f"{columna} Acumulativo")
                plt.legend()
                plt.grid(True)
                plt.savefig(f'{carpeta_salida}/{columna}_acumulativo_linea.png')
                plt.close()
            elif tipo_grafica == "barras":
                plt.figure(figsize=(10, 5))
                plt.bar(eje_x, acumulativo, label=f"{columna} Acumulativo")
                plt.title(f'{columna} Mensual (Acumulativo)')
                plt.xlabel(eje_x.name)
                plt.ylabel(f"{columna} Acumulativo")
                plt.legend()
                plt.savefig(f'{carpeta_salida}/{columna}_acumulativo_barras.png')
                plt.close()
