import os
import re
import tkinter as tk
from tkinter import filedialog

def renombrar_archivos(buscar, inicio, fin):
    directorio = filedialog.askdirectory()
    patron_borrar = r"{}.*?{}".format(re.escape(inicio), re.escape(fin))
    for archivo in os.listdir(directorio):
        if not os.path.isdir(os.path.join(directorio, archivo)):
            extension = os.path.splitext(archivo)[1]
            nuevo_nombre = re.sub(buscar, "", archivo)
            nuevo_nombre = re.sub(patron_borrar, "", nuevo_nombre)
            nuevo_archivo = nuevo_nombre + extension
            os.rename(os.path.join(directorio, archivo), os.path.join(directorio, nuevo_archivo))

root = tk.Tk()
root.title("Renombrar archivos")
root.geometry("400x200")

label_buscar = tk.Label(root, text="Texto a buscar:")
label_buscar.pack()
entry_buscar = tk.Entry(root)
entry_buscar.pack()

label_inicio = tk.Label(root, text="Entre el caracter:")
label_inicio.pack()
entry_inicio = tk.Entry(root)
entry_inicio.pack()

label_fin = tk.Label(root, text="Y el caracter:")
label_fin.pack()
entry_fin = tk.Entry(root)
entry_fin.pack()

btn_seleccionar_directorio = tk.Button(root, text="Seleccionar directorio", command=lambda: renombrar_archivos(entry_buscar.get(), entry_inicio.get(), entry_fin.get()))
btn_seleccionar_directorio.pack(pady=10)

root.mainloop()
