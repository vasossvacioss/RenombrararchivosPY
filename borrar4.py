import os
import re

# Directorio donde se encuentran los archivos
directorio = "/home/vasossvacioss/Escritorio/Fotos"


# Patrón a eliminar
patron_borrar = r"\.[^.]*"


for archivo in os.listdir(directorio):
 
    if not os.path.isdir(os.path.join(directorio, archivo)):
      
        extension = os.path.splitext(archivo)[1]
        
       
        nuevo_nombre = re.sub(patron_borrar, "", archivo)
        
        nuevo_archivo = nuevo_nombre + extension
        
        # Renombrar el archivo
        os.rename(os.path.join(directorio, archivo), os.path.join(directorio, nuevo_archivo))
