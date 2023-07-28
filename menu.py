# Imporaciones
import tkinter as tk

# Acerca de
def acercade():
    ventana = tk.Tk()
    ventana.geometry("250x200")
    ventana.title("Acerca de")
    ventana.resizable(False, False)

    label_principal = tk.Label(ventana, text="CubiQ | Conversor de Imágenes", wraplength=300, font='Arial')
    label_principal.pack(pady=20)
    our_canvas=tk.Canvas(ventana,width=550,height=1,bg="black")
    our_canvas.pack()

    label_descripcion = tk.Label(ventana, text="CubiQ es un programa Open Source que se rige sobre la licencia MIT.", wraplength=200, font='Arial')
    label_descripcion.pack(pady=5)
    label_autor = tk.Label(ventana, text="Autor: @estuardodev", wraplength=200, font=('Arial', 12))
    label_autor.pack(pady=5)
    label_version = tk.Label(ventana, text="Versión: 0.1.0", wraplength=200, font=('Arial', 10))
    label_version.pack(pady=5)


    ventana.mainloop()

def actualizaciones():
    ventana = tk.Tk()
    ventana.geometry("100x100")

    ventana.mainloop()
