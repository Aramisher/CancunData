import tkinter as tk
from tkinter import filedialog, messagebox
from data_processing import procesar_datos

def iniciar_aplicacion():
    ventana = tk.Tk()
    ventana.title("Procesador de Datos")
    ventana.geometry("300x100")

    def seleccionar_archivo():
        ruta_archivo = filedialog.askopenfilename(filetypes=[("Archivos Excel", "*.xlsx *.xls")])
        if ruta_archivo:
            errores = procesar_datos(ruta_archivo)
            if errores:
                messagebox.showerror("Errores Encontrados", f"Se encontraron errores en el archivo. Revisa el reporte en 'outputs/reportes/'.")
            else:
                messagebox.showinfo("Proceso Exitoso", "Los datos se procesaron correctamente y las gráficas se generaron en 'outputs/graficas/'.")

    btn_seleccionar = tk.Button(ventana, text="Seleccionar Archivo Excel", command=seleccionar_archivo)
    btn_seleccionar.pack(expand=True)

    ventana.mainloop()
