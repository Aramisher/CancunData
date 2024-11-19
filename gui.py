import tkinter as tk
import ttkbootstrap as ttk
from ttkbootstrap.constants import *
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
                messagebox.showerror(
                    "Errores Encontrados",
                    "Se encontraron errores en el archivo. Revisa el reporte en 'outputs/reportes/'."
                )
            else:
                messagebox.showinfo(
                    "Proceso Exitoso",
                    "Las gráficas se generaron correctamente en 'outputs/graficas/'."
                )

    # Crear la ventana principal
    ventana = ttk.Window(themename='cosmo')
    ventana.title("Procesador de Datos")
    ventana.geometry("500x400")  # Tamaño inicial más grande para evitar ventana vacía

    # Crear un marco principal
    frame = ttk.Frame(ventana, padding=20)
    frame.pack(expand=True, fill=BOTH)  # Asegura que el marco ocupe todo el espacio disponible

    # Tipo de gráfica
    label_tipo = ttk.Label(frame, text="Seleccione el tipo de gráfica:", font=('Helvetica', 12))
    label_tipo.pack(pady=(0, 5), anchor='w')
    tipo_var = tk.StringVar(value="linea")
    radio_linea = ttk.Radiobutton(frame, text="Línea", variable=tipo_var, value="linea", bootstyle="primary")
    radio_linea.pack(anchor='w', pady=2)
    radio_barras = ttk.Radiobutton(frame, text="Barras", variable=tipo_var, value="barras", bootstyle="primary")
    radio_barras.pack(anchor='w', pady=2)

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

    # Estilo personalizado para un botón más pequeño y con bordes redondeados
    style = ttk.Style()
    style.configure(
        "Custom.TButton", 
        font=("Helvetica", 10),  # Texto más pequeño
        padding=(5, 5),  # Reduce el padding
        borderwidth=2,
        focusthickness=3,
        focuscolor="none",
    )
    style.map(
        "Custom.TButton", 
        background=[("active", "#0056b3"), ("!active", "#007bff")],  # Azul claro
        foreground=[("active", "white"), ("!active", "white")],
        relief=[("pressed", "groove"), ("!pressed", "ridge")]
    )

    # Botón para seleccionar archivo (con estilo personalizado)
    btn_seleccionar = ttk.Button(
        frame,
        text="Seleccionar Archivo Excel",
        command=seleccionar_archivo,
        bootstyle='primary',
        style="Custom.TButton"  # Aplica el estilo personalizado
    )
    btn_seleccionar.pack(pady=20)

    ventana.mainloop()
