import os
import re

folder_path = "/home/vasossvacioss/Escritorio/Fotos"  # Ruta de la carpeta que contiene los archivos
pattern = re.compile(r'(?<=.)(.*?)(?=jpg)', re.IGNORECASE)

# Recorre todos los archivos de la carpeta y renombra los que contengan las palabras a eliminar
for filename in os.listdir(folder_path):
    if pattern.search(filename):
        new_filename = pattern.sub(" ", filename)
        os.rename(os.path.join(folder_path, filename), os.path.join(folder_path, new_filename))
