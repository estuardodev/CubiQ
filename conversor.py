# Importaciones
from PIL import Image
from pathlib import Path

def convertir_imagen(formato_a_convertir, ruta_img_seleccionada, ruta_dir_guardar):
        source = Path(ruta_img_seleccionada)
        formato_convertir = formato_a_convertir
        destino = Path(ruta_dir_guardar).joinpath(source.stem + "." + formato_convertir.lower())
        image = Image.open(ruta_img_seleccionada)  # Abrir imagen
        image.save(destino, format=formato_convertir)  # Convertir imagen al formato seleccionado y guardarla
        return destino

