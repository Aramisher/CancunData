import tkinter as tk
from tkinter import filedialog, messagebox
from data_processing import procesar_datos


def iniciar_aplicacion():
    """
    Inicia la interfaz gráfica de usuario.
    """
    def seleccionar_archivo():
        ruta_archivo = filedialog.askopenfilename(filetypes=[("Archivos Excel", "*.xlsx *.xls")])
        if ruta_archivo:
            tipo_grafica = tipo_var.get()
            modo_grafica = modo_var.get()
            errores = procesar_datos(ruta_archivo, tipo_grafica, modo_grafica)
            if errores:
                messagebox.showerror("Errores Encontrados", f"Se encontraron errores en el archivo. Revisa el reporte en 'outputs/reportes/'.")
            else:
                messagebox.showinfo("Proceso Exitoso", "Las gráficas se generaron correctamente en 'outputs/graficas/'.")

    ventana = tk.Tk()
    ventana.title("Procesador de Datos")
    ventana.geometry("400x200")

    # Tipo de gráfica
    tk.Label(ventana, text="Seleccione el tipo de gráfica:").pack()
    tipo_var = tk.StringVar(value="linea")
    tk.Radiobutton(ventana, text="Línea", variable=tipo_var, value="linea").pack()
    tk.Radiobutton(ventana, text="Barras", variable=tipo_var, value="barras").pack()

    # Modo de gráfica
    tk.Label(ventana, text="Seleccione el modo de visualización:").pack()
    modo_var = tk.StringVar(value="independiente")
    tk.Radiobutton(ventana, text="Independiente", variable=modo_var, value="independiente").pack()
    tk.Radiobutton(ventana, text="Acumulativo", variable=modo_var, value="acumulativo").pack()
    tk.Radiobutton(ventana, text="Ambos", variable=modo_var, value="ambos").pack()

    # Botón para seleccionar archivo
    btn_seleccionar = tk.Button(ventana, text="Seleccionar Archivo Excel", command=seleccionar_archivo)
    btn_seleccionar.pack(expand=True)

    ventana.mainloop()
