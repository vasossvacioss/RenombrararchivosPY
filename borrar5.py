import os
import re
import tkinter as tk
from tkinter import filedialog

def renombrar_archivos():
    directorio = filedialog.askdirectory()
    patron_borrar = r"\.[^.]*"
    for archivo in os.listdir(directorio):
        if not os.path.isdir(os.path.join(directorio, archivo)):
            extension = os.path.splitext(archivo)[1]
            nuevo_nombre = re.sub(patron_borrar, "", archivo)
            nuevo_archivo = nuevo_nombre + extension
            os.rename(os.path.join(directorio, archivo), os.path.join(directorio, nuevo_archivo))

root = tk.Tk()
root.title("Renombrar archivos")
root.geometry("300x100")

btn_seleccionar_directorio = tk.Button(root, text="Seleccionar directorio", command=renombrar_archivos)
btn_seleccionar_directorio.pack(pady=10)

root.mainloop()
