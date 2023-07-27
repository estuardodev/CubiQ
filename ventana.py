# Importaciones
import tkinter as tk
from tkinter import filedialog

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

    '''Fin de las funciones a utilizar'''

    '''Inicio de objetos dentro de la ventana'''
    # Etiqueta para mostrar la ruta de la imagen seleccionada
    label_ruta_imagen = tk.Label(ventana, text="No se ha seleccionado ninguna imagen.", wraplength=300)
    label_ruta_imagen.pack(pady=10)

    # Botón para seleccionar la imagen
    boton_seleccionar = tk.Button(ventana, text="Seleccionar imagen", command=seleccionar_imagen)
    boton_seleccionar.pack(pady=5)

    # Ejecutamos la ventana
    ventana.mainloop()