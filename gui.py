import tkinter as tk
from tkinter import filedialog, messagebox
import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from data_processing import procesar_datos

def iniciar_aplicacion():
    """
    Inicia la interfaz gráfica de usuario.
    """
    def seleccionar_carpeta():
        # Permite al usuario seleccionar una carpeta para guardar los gráficos
        carpeta = filedialog.askdirectory()
        if carpeta:
            return carpeta
        else:
            messagebox.showwarning("Advertencia", "No se seleccionó ninguna carpeta.")
            return None

    def seleccionar_archivo():
        # Permite al usuario seleccionar un archivo Excel
        ruta_archivo = filedialog.askopenfilename(filetypes=[("Archivos Excel", "*.xlsx *.xls")])
        if ruta_archivo:
            # Mostrar mensaje profesional
            messagebox.showinfo(
                "Seleccione Carpeta de Salida",
                "A continuación, deberá seleccionar la carpeta donde se guardarán los gráficos generados. Por favor, elija una ubicación adecuada."
            )
            # Continuar con la selección de carpeta
            tipo_grafica = tipo_var.get()
            modo_grafica = modo_var.get()
            carpeta_graficas = seleccionar_carpeta()  # Obtener carpeta donde guardar las gráficas
            if carpeta_graficas:
                errores = procesar_datos(ruta_archivo, tipo_grafica, modo_grafica, carpeta_graficas)
                if errores:
                    messagebox.showerror("Errores Encontrados", f"Se encontraron errores en el archivo. Revisa el reporte.")
                else:
                    messagebox.showinfo("Proceso Exitoso", "Las gráficas se generaron correctamente.")
            else:
                messagebox.showwarning("Advertencia", "No se seleccionó carpeta para guardar las gráficas.")

    # Crear ventana principal con un tema de ttkbootstrap
    ventana = ttk.Window(themename='cosmo')
    ventana.title("Procesador de Datos")
    ventana.geometry("600x400")

    # Crear un marco para los widgets
    frame = ttk.Frame(ventana, padding=20)
    frame.pack(expand=True, fill=BOTH)

    # Tipo de gráfica
    label_tipo = ttk.Label(frame, text="Seleccione el tipo de gráfica:", font=('Helvetica', 12))
    label_tipo.pack(pady=(0, 5), anchor='w')
    tipo_var = tk.StringVar(value="linea")
    radio_linea = ttk.Radiobutton(frame, text="Línea", variable=tipo_var, value="linea", bootstyle="primary")
    radio_linea.pack(anchor='w', pady=2)
    radio_barras = ttk.Radiobutton(frame, text="Barras", variable=tipo_var, value="barras", bootstyle="primary")
    radio_barras.pack(anchor='w', pady=2)
    radio_pie = ttk.Radiobutton(frame, text="Pie Chart", variable=tipo_var, value="pie", bootstyle="primary")
    radio_pie.pack(anchor='w', pady=2)

    # Modo de gráfica
    label_modo = ttk.Label(frame, text="Seleccione el modo de visualización:", font=('Helvetica', 12))
    label_modo.pack(pady=(10, 5), anchor='w')
    modo_var = tk.StringVar(value="independiente")
    radio_independiente = ttk.Radiobutton(frame, text="Independiente", variable=modo_var, value="independiente", bootstyle="success")
    radio_independiente.pack(anchor='w', pady=2)
    radio_acumulativo = ttk.Radiobutton(frame, text="Acumulativo", variable=modo_var, value="acumulativo", bootstyle="success")
    radio_acumulativo.pack(anchor='w', pady=2)
    radio_ambos = ttk.Radiobutton(frame, text="Ambos", variable=modo_var, value="ambos", bootstyle="success")
    radio_ambos.pack(anchor='w', pady=2)

    # Botón para seleccionar archivo
    btn_seleccionar = ttk.Button(
        frame,
        text="Seleccionar Archivo Excel",
        command=seleccionar_archivo,
        bootstyle='primary',
        padding=(5, 5)
    )
    btn_seleccionar.pack(pady=20)

    ventana.mainloop()
