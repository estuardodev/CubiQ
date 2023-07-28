# Importaciones
import random, time
import tkinter as tk
from tkinter import filedialog, ttk, messagebox
from pathlib import Path
from conversor import convertir_imagen

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

    
    def convertir():
        if ruta_imagen_seleccionada and ruta_carpeta_guardado:

            formato = combo.get() # obtenemos el formato a convertir seleccionado
            ejecutar_conversión = convertir_imagen(formato_a_convertir=formato, ruta_img_seleccionada=ruta_imagen_seleccionada, ruta_dir_guardar=ruta_carpeta_guardado)

            # Simular el proceso de conversión con un ciclo for
            for i in range(101):
                time.sleep(0.03)  # Simular un pequeño retraso
                progressbar["value"] = i
                progressbar.update()

            # Actualizar el mensaje de conversión
            label_ruta_mensaje.config(text="Imagen convertida y guardada en: " + str(ejecutar_conversión))
            messagebox.showinfo(title = "Correcto", message = "Conversión exitosa")

        else:
            label_ruta_mensaje.config(text="Por favor, seleccione una imagen, una carpeta y un formato.", fg="red")
            messagebox.showerror(title = "Error", message = "Por favor, realiza todo lo que se te pide.")


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

    # Barra de progreso
    progressbar = ttk.Progressbar(ventana, mode="determinate", maximum=100)

    # Etiqueta para mostrar el mensaje de conversión
    label_ruta_mensaje = tk.Label(ventana, text="No se ha detectado ningún problema.", wraplength=300, fg="green")
    label_ruta_mensaje.pack(pady=10)

    # Botón para convertir la imagen
    boton_convertir = tk.Button(ventana, text="Convertir Imágen", command=convertir)
    boton_convertir.pack(pady=5)

    # Configurar la posición de la barra de progreso
    progressbar.pack(pady=5)

    '''Fin de objetos dentro de la ventana'''

    # Ejecutamos la ventana
    ventana.mainloop()