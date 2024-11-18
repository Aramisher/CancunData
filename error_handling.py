import pandas as pd
import os

def validar_datos(df):
    errores = []
    for idx, row in df.iterrows():
        for col in df.columns:
            valor = row[col]
            if pd.isnull(valor):
                errores.append(f"Fila {idx+2}, Columna '{col}': Valor nulo")
            elif isinstance(valor, str) and not valor.isdigit():
                errores.append(f"Fila {idx+2}, Columna '{col}': Valor no numérico '{valor}'")
    return errores

def guardar_reporte_errores(errores):
    os.makedirs('outputs/reportes/', exist_ok=True)
    with open('outputs/reportes/reporte_errores.txt', 'w') as f:
        for error in errores:
            f.write(error + '\n')
