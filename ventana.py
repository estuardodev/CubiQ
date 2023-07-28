# Importaciones
import random, time
import tkinter as tk
from tkinter import filedialog, ttk, messagebox
from conversor import convertir_imagen
from menu import acercade, actualizaciones


# Variables Globales
ruta_imagen_seleccionada = None
ruta_carpeta_guardado = None
FUENTE_PRINCIPAL = ('Arial', 18)
FUENTE_TEXTO = 'Arial'
FUENTE_BOTON = 'Arial'
COLOR_NARANJA = '#FA7200'
FONDO='#F0F0F0'


# Función que alamacena nuestra ventana
def ventana_programa():
    # Ventana
    ventana = tk.Tk()
    menu = tk.Menu()
    menu_ayuda = tk.Menu(menu, tearoff=0)
    menu.add_cascade(label="Ayuda", menu=menu_ayuda)
    menu_ayuda.add_command(label="Actualizaciones", command=actualizaciones)
    menu_ayuda.add_command(label="Acerca de", command=acercade)
    menu.add_cascade(label="Salir", command=ventana.quit)

    # Configuración de la ventana
    ancho_ventana = 550
    alto_ventana = 600
    x_ventana = ventana.winfo_screenwidth() // 2 - ancho_ventana // 2
    y_ventana = ventana.winfo_screenheight() // 2 - alto_ventana // 2
    posicion = str(ancho_ventana) + "x" + str(alto_ventana) + "+" + str(x_ventana) + "+" + str(y_ventana)
    ventana.geometry(posicion)
    ventana.title("CubiQ | Conversor de Imágenes")
    ventana.config(background=FONDO, menu=menu)
    ventana.resizable(False, False)
    
    label_principal = tk.Label(ventana, text="CubiQ | Conversor de Imágenes", wraplength=350, font=FUENTE_PRINCIPAL)
    label_principal.pack(pady=20)
    our_canvas=tk.Canvas(ventana,width=550,height=1,bg="black")
    our_canvas.pack()

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
            label_ruta_imagen.config(text="No se ha seleccionado ninguna imagen.", fg=COLOR_NARANJA, bg=FONDO, font=FUENTE_TEXTO)

    def seleccionar_carpeta():
        global ruta_carpeta_guardado
        ruta_carpeta_guardado = filedialog.askdirectory(title="Seleccionar carpeta de guardado")
        if ruta_carpeta_guardado:
            label_ruta_guardar.config(text="Carpeta de guardado seleccionada: " + ruta_carpeta_guardado)
        else:
            label_ruta_guardar.config(text="No se ha seleccionado ninguna carpeta de guardado.", fg=COLOR_NARANJA, bg=FONDO, font=FUENTE_TEXTO)

    
    def convertir():
        if ruta_imagen_seleccionada and ruta_carpeta_guardado:

            formato = combo.get() # obtenemos el formato a convertir seleccionado
            ejecutar_conversión = convertir_imagen(formato, ruta_imagen_seleccionada, ruta_carpeta_guardado)

            # Simular el proceso de conversión con un ciclo for
            for i in range(101):
                time.sleep(0.01)  # Simular un pequeño retraso
                progressbar["value"] = i
                progressbar.update()
             # Detener la barra de progreso y restablecer su valor
            progressbar.stop()
            progressbar["value"] = 0
            progressbar.update()

            # Actualizar el mensaje de conversión
            label_ruta_mensaje.config(text="Imagen convertida y guardada en: " + str(ejecutar_conversión))
            messagebox.showinfo(title = "Correcto", message = "Conversión exitosa")

        else:
            label_ruta_mensaje.config(text="Por favor, seleccione una imagen, una carpeta y un formato.", fg="red", bg=FONDO, font=FUENTE_TEXTO)
            messagebox.showerror(title = "Error", message = "Por favor, realiza todo lo que se te pide.", font=FUENTE_TEXTO)


    '''Fin de las funciones a utilizar'''

    '''Inicio de objetos dentro de la ventana'''

    # Etiqueta para mostrar la ruta de la imagen seleccionada
    label_ruta_imagen = tk.Label(ventana, text="No se ha seleccionado ninguna imagen.", fg=COLOR_NARANJA, bg=FONDO, wraplength=300, font=FUENTE_TEXTO)
    label_ruta_imagen.pack(pady=10)

    # Botón para seleccionar la imagen
    boton_seleccionar = tk.Button(ventana, text="Seleccionar imagen", command=seleccionar_imagen, font=FUENTE_BOTON)
    boton_seleccionar.pack(pady=5)

    # Etiqueta para mostrar la ruta de la imagen seleccionada
    formato_opciones = ["PNG", "JPG", "JPEG", "WEBP", "GIF"]
    laber_combo = tk.Label(ventana, text="Formato a Convertir.", wraplength=300, font=FUENTE_TEXTO)
    laber_combo.pack(pady=10)
    combo = ttk.Combobox(
        state="readonly",
        values=formato_opciones
    )
    combo.set(random.choice(formato_opciones))
    combo.pack(pady=10)

    # Etiqueta para mostrar la ruta de la carpeta seleccionada
    label_ruta_guardar = tk.Label(ventana, text="No se ha seleccionado ninguna carpeta de guardado.", fg=COLOR_NARANJA, bg=FONDO, wraplength=300, font=FUENTE_TEXTO)
    label_ruta_guardar.pack(pady=10)

    # Botón para seleccionar la carpeta de guardado
    boton_seleccionar_carpeta = tk.Button(ventana, text="Seleccionar carpeta", command=seleccionar_carpeta, font=FUENTE_BOTON)
    boton_seleccionar_carpeta.pack(pady=5)

    # Barra de progreso
    progressbar = ttk.Progressbar(ventana, mode="determinate", maximum=100)

    # Etiqueta para mostrar el mensaje de conversión
    label_ruta_mensaje = tk.Label(ventana, text="No se ha detectado ningún problema.", wraplength=300, fg="green", bg=FONDO, font=FUENTE_TEXTO)
    label_ruta_mensaje.pack(pady=10)

    # Botón para convertir la imagen
    boton_convertir = tk.Button(ventana, text="Convertir Imágen", command=convertir, font=FUENTE_BOTON)
    boton_convertir.pack(pady=5)

    # Configurar la posición de la barra de progreso
    progressbar.pack(pady=5)

    '''Fin de objetos dentro de la ventana'''

  
    # Ejecutamos la ventana
    ventana.mainloop()