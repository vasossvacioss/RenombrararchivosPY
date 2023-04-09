import os

# Directorio donde se encuentran los archivos
directorio = "/home/vasossvacioss/Escritorio/Fotos"

# Loop para renombrar cada archivo en el directorio
for archivo in os.listdir(directorio):
    # Si el archivo no es un directorio
    if not os.path.isdir(os.path.join(directorio, archivo)):
        # Separar el nombre del archivo en dos partes en el primer punto
        partes_nombre = archivo.split(".", 1)
        
        # Obtener la primera parte del nombre del archivo
        nombre_base = partes_nombre[0]
        
        # Obtener la segunda parte del nombre del archivo y la extensión
        if len(partes_nombre) == 2:
            extension = "." + partes_nombre[1]
        else:
            extension = ""
        
        # Concatenar la primera parte del nombre del archivo con la extensión
        nuevo_archivo = nombre_base + extension
        
        # Renombrar el archivo
        os.rename(os.path.join(directorio, archivo), os.path.join(directorio, nuevo_archivo))
