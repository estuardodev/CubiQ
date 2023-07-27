# Importaciones
import tkinter as tk

# Función que alamacena nuestra ventana
def ventana_programa():
    # Ventana
    ventana = tk.Tk()

    # Configuración de la ventana
    ventana.geometry("550x500")
    ventana.title("Conversor de Formatos")

    # Ejecutamos la ventana
    ventana.mainloop()