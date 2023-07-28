# Importaciones
import time
from pathlib import Path

def convertir_imagen(formato_a_convertir, ruta_img_seleccionada, ruta_dir_guardar):
        source = Path(ruta_img_seleccionada)
        formato_convertir = formato_a_convertir
        destination = Path(ruta_dir_guardar).joinpath(source.stem + "." + formato_convertir.lower())
        return destination

