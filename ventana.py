# Importaciones
import random
import tkinter as tk
from tkinter import filedialog, ttk

# Variables Globales
ruta_imagen_seleccionada = None
ruta_carpeta_guardado = None



# Función que alamacena nuestra ventana
def ventana_programa():
    # Ventana
    ventana = tk.Tk()

    # Configuración de la ventana
    ventana.geometry("550x500")
    ventana.title("Conversor de Formatos")

    '''Funciónes a utilizar'''
    def seleccionar_imagen():
        global ruta_imagen_seleccionada
        ruta_imagen_seleccionada = filedialog.askopenfilename(
            title="Seleccionar imagen",
            filetypes=(("Archivos de imagen", "*.png;*.jpg;*.jpeg;*.gif;*.webp"), ("Todos los archivos", "*.*"))
        )
        if ruta_imagen_seleccionada:
            label_ruta_imagen.config(text="Ruta de la imagen seleccionada: " + ruta_imagen_seleccionada)
        else:
            label_ruta_imagen.config(text="No se ha seleccionado ninguna imagen.")

    def seleccionar_carpeta():
        global ruta_carpeta_guardado
        ruta_carpeta_guardado = filedialog.askdirectory(title="Seleccionar carpeta de guardado")
        if ruta_carpeta_guardado:
            label_ruta_guardar.config(text="Carpeta de guardado seleccionada: " + ruta_carpeta_guardado)
        else:
            label_ruta_guardar.config(text="No se ha seleccionado ninguna carpeta de guardado.")

    '''Fin de las funciones a utilizar'''

    '''Inicio de objetos dentro de la ventana'''

    # Etiqueta para mostrar la ruta de la imagen seleccionada
    label_ruta_imagen = tk.Label(ventana, text="No se ha seleccionado ninguna imagen.", wraplength=300)
    label_ruta_imagen.pack(pady=10)

    # Botón para seleccionar la imagen
    boton_seleccionar = tk.Button(ventana, text="Seleccionar imagen", command=seleccionar_imagen)
    boton_seleccionar.pack(pady=5)

    # Etiqueta para mostrar la ruta de la imagen seleccionada
    formato_opciones = ["PNG", "JPG", "JPEG", "WEBP", "GIF"]
    laber_combo = tk.Label(ventana, text="Formato a Convertir.", wraplength=300)
    laber_combo.pack(pady=10)
    combo = ttk.Combobox(
        state="readonly",
        values=formato_opciones
    )
    combo.set(random.choice(formato_opciones))
    combo.pack(pady=10)

    # Etiqueta para mostrar la ruta de la carpeta seleccionada
    label_ruta_guardar = tk.Label(ventana, text="No se ha seleccionado ninguna carpeta de guardado.", wraplength=300)
    label_ruta_guardar.pack(pady=10)

    # Botón para seleccionar la carpeta de guardado
    boton_seleccionar_carpeta = tk.Button(ventana, text="Seleccionar carpeta", command=seleccionar_carpeta)
    boton_seleccionar_carpeta.pack(pady=5)

    '''Fin de objetos dentro de la ventana'''

    # Ejecutamos la ventana
    ventana.mainloop()