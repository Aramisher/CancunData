import pandas as pd
import matplotlib.pyplot as plt
from error_handling import validar_datos, guardar_reporte_errores
import os


def procesar_datos(ruta_archivo, tipo_grafica="linea", modo="independiente"):
    """
    Procesa los datos de un archivo Excel, valida y genera gráficas según las opciones del usuario.
    :param ruta_archivo: Ruta del archivo Excel.
    :param tipo_grafica: Tipo de gráfica ('linea' o 'barras').
    :param modo: Modo de visualización ('independiente', 'acumulativo' o 'ambos').
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
            generar_graficas(df, tipo_grafica, modo)
            return None
    except Exception as e:
        print(f"Ocurrió un error al procesar los datos: {e}")
        return [str(e)]


def generar_graficas(df, tipo_grafica="linea", modo="independiente"):
    """
    Genera gráficas según el tipo y modo seleccionados.
    :param df: DataFrame con los datos.
    :param tipo_grafica: Tipo de gráfica ('linea' o 'barras').
    :param modo: Modo de visualización ('independiente', 'acumulativo' o 'ambos').
    """
    os.makedirs('outputs/graficas/', exist_ok=True)

    if modo in ["independiente", "ambos"]:
        if tipo_grafica == "linea":
            plt.figure(figsize=(10, 5))
            plt.plot(df['Mes'], df['Ventas'], marker='o', label="Ventas Independientes")
            plt.title('Ventas Mensuales (Independiente)')
            plt.xlabel('Mes')
            plt.ylabel('Ventas')
            plt.legend()
            plt.grid(True)
            plt.savefig('outputs/graficas/ventas_independiente_linea.png')
        elif tipo_grafica == "barras":
            plt.figure(figsize=(10, 5))
            plt.bar(df['Mes'], df['Ventas'], label="Ventas Independientes")
            plt.title('Ventas Mensuales (Independiente)')
            plt.xlabel('Mes')
            plt.ylabel('Ventas')
            plt.legend()
            plt.savefig('outputs/graficas/ventas_independiente_barras.png')

    if modo in ["acumulativo", "ambos"]:
        ventas_acumuladas = df['Ventas'].cumsum()
        if tipo_grafica == "linea":
            plt.figure(figsize=(10, 5))
            plt.plot(df['Mes'], ventas_acumuladas, marker='o', label="Ventas Acumulativas")
            plt.title('Ventas Mensuales (Acumulativo)')
            plt.xlabel('Mes')
            plt.ylabel('Ventas Acumulativas')
            plt.legend()
            plt.grid(True)
            plt.savefig('outputs/graficas/ventas_acumulativo_linea.png')
        elif tipo_grafica == "barras":
            plt.figure(figsize=(10, 5))
            plt.bar(df['Mes'], ventas_acumuladas, label="Ventas Acumulativas")
            plt.title('Ventas Mensuales (Acumulativo)')
            plt.xlabel('Mes')
            plt.ylabel('Ventas Acumulativas')
            plt.legend()
            plt.savefig('outputs/graficas/ventas_acumulativo_barras.png')
