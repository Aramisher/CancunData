import pandas as pd
import matplotlib.pyplot as plt
from error_handling import validar_datos, guardar_reporte_errores
import os


def procesar_datos(ruta_archivo, tipo_grafica="linea", modo="independiente", carpeta_salida="outputs/graficas"):
    """
    Procesa los datos de un archivo Excel, valida y genera gráficas y un reporte según las opciones del usuario.
    :param ruta_archivo: Ruta del archivo Excel.
    :param tipo_grafica: Tipo de gráfica ('linea', 'barras', 'pie').
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
            generar_reporte_uniforme(df, carpeta_salida)
            return None
    except Exception as e:
        print(f"Ocurrió un error al procesar los datos: {e}")
        return [str(e)]


def generar_graficas(df, tipo_grafica="linea", modo="independiente", carpeta_salida="outputs/graficas"):
    """
    Genera gráficas para cada columna del DataFrame según el tipo y modo seleccionados.
    :param df: DataFrame con los datos.
    :param tipo_grafica: Tipo de gráfica ('linea', 'barras', 'pie').
    :param modo: Modo de visualización ('independiente', 'acumulativo' o 'ambos').
    :param carpeta_salida: Carpeta donde se guardarán las gráficas.
    """
    os.makedirs(carpeta_salida, exist_ok=True)

    # Detectar si la primera columna es de tipo 'Mes' o 'Día'
    eje_x = df.iloc[:, 0]  # Primera columna
    eje_x_nombre = eje_x.name.lower()
    if "mes" in eje_x_nombre or "día" in eje_x_nombre or "dia" in eje_x_nombre:
        columnas = df.select_dtypes(include=['number']).columns[1:]  # Omitir la primera columna
    else:
        columnas = df.select_dtypes(include=['number']).columns

    for columna in columnas:
        if tipo_grafica == "pie":
            # Gráfico de Pie Chart siempre como independiente
            plt.figure(figsize=(8, 8))
            plt.pie(df[columna], labels=eje_x, autopct='%1.1f%%', startangle=140)
            plt.title(f'{columna} - Distribución')
            plt.savefig(f'{carpeta_salida}/{columna}_pie.png')
            plt.close()
        else:
            # Independiente
            if modo in ["independiente", "ambos"]:
                if tipo_grafica == "linea":
                    plt.figure(figsize=(10, 5))
                    plt.plot(eje_x, df[columna], marker='o', label=f"{columna}")
                    plt.title(f'{columna}')
                    plt.xlabel(eje_x.name)
                    plt.ylabel(columna)
                    plt.legend()
                    plt.grid(True)
                    plt.savefig(f'{carpeta_salida}/{columna}_independiente_linea.png')
                    plt.close()
                elif tipo_grafica == "barras":
                    plt.figure(figsize=(10, 5))
                    plt.bar(eje_x, df[columna], label=f"{columna}")
                    plt.title(f'{columna}')
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
                    plt.plot(eje_x, acumulativo, marker='o', label=f"{columna}")
                    plt.title(f'{columna} Acumulativo')
                    plt.xlabel(eje_x.name)
                    plt.ylabel(f"{columna} Acumulativo")
                    plt.legend()
                    plt.grid(True)
                    plt.savefig(f'{carpeta_salida}/{columna}_acumulativo_linea.png')
                    plt.close()
                elif tipo_grafica == "barras":
                    plt.figure(figsize=(10, 5))
                    plt.bar(eje_x, acumulativo, label=f"{columna}")
                    plt.title(f'{columna} Acumulativo')
                    plt.xlabel(eje_x.name)
                    plt.ylabel(f"{columna} Acumulativo")
                    plt.legend()
                    plt.savefig(f'{carpeta_salida}/{columna}_acumulativo_barras.png')
                    plt.close()


def generar_reporte_uniforme(df, carpeta_salida):
    """
    Genera un reporte uniforme con análisis detallado para todas las columnas numéricas, omitiendo la primera columna si es eje X.
    :param df: DataFrame con los datos.
    :param carpeta_salida: Carpeta donde se guardará el reporte.
    """
    reporte_path = os.path.join(carpeta_salida, "reporte_general.txt")

    # Detectar si la primera columna es de tipo 'Mes' o 'Día'
    eje_x = df.iloc[:, 0]  # Primera columna
    eje_x_nombre = eje_x.name.lower()
    if "mes" in eje_x_nombre or "día" in eje_x_nombre or "dia" in eje_x_nombre:
        columnas = df.select_dtypes(include=['number']).columns[1:]  # Omitir la primera columna
    else:
        columnas = df.select_dtypes(include=['number']).columns

    with open(reporte_path, "w") as reporte:
        reporte.write("REPORTE DETALLADO DE DATOS\n")
        reporte.write("=" * 50 + "\n\n")

        for columna in columnas:
            datos = df[columna]

            # Análisis detallado
            reporte.write(f"ANÁLISIS DE '{columna}':\n")
            reporte.write(f"- Valor máximo: {datos.max()}\n")
            reporte.write(f"- Valor mínimo: {datos.min()}\n")
            reporte.write(f"- Promedio: {datos.mean():.2f}\n")
            reporte.write(f"- Suma total: {datos.sum()}\n")

            # Cálculo de incrementos y decrementos
            cambios = datos.pct_change().dropna() * 100
            reporte.write(f"- Incremento/Decremento promedio (%): {cambios.mean():.2f}%\n")
            reporte.write(f"- Máximo incremento (%): {cambios.max():.2f}%\n")
            reporte.write(f"- Máximo decremento (%): {cambios.min():.2f}%\n")
            reporte.write("\n")

        # Resumen general
        reporte.write("=" * 50 + "\n")
        reporte.write("RESUMEN GENERAL\n")
        reporte.write(f"- Columnas analizadas: {', '.join(columnas)}\n")
        reporte.write(f"- Total de filas: {len(df)}\n")

    print(f"Reporte generado: {reporte_path}")
