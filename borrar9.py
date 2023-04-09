import os
import re
import tkinter as tk
import webbrowser
from tkinter import filedialog

def renombrar_archivos(buscar, inicio, fin, directorio):
    patron_borrar = r"{}.*?{}".format(re.escape(inicio), re.escape(fin))
    for archivo in os.listdir(directorio):
        if not os.path.isdir(os.path.join(directorio, archivo)):
            extension = os.path.splitext(archivo)[1]
            nuevo_nombre = re.sub(buscar, "", archivo)
            nuevo_nombre = re.sub(patron_borrar, "", nuevo_nombre)
            nuevo_archivo = nuevo_nombre + extension
            os.rename(os.path.join(directorio, archivo), os.path.join(directorio, nuevo_archivo))

def seleccionar_directorio():
    directorio = filedialog.askdirectory()
    entry_directorio.delete(0, tk.END)
    entry_directorio.insert(0, directorio)

def abrir_direccion():
    webbrowser.open("https://vasossvacioss.github.io/portafolio3/")

root = tk.Tk()
root.title("Renombrar archivos")
root.geometry("400x300")

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

label_directorio = tk.Label(root, text="Directorio:")
label_directorio.pack()
entry_directorio = tk.Entry(root)
entry_directorio.pack()
btn_directorio = tk.Button(root, text="Seleccionar directorio", command=seleccionar_directorio)
btn_directorio.pack(pady=10)

btn_renombrar = tk.Button(root, text="Renombrar archivos", command=lambda: renombrar_archivos(entry_buscar.get(), entry_inicio.get(), entry_fin.get(), entry_directorio.get()))
btn_renombrar.pack(pady=10)

btn_direccion = tk.Button(root, text="Repositorio GitHub", command=abrir_direccion)
btn_direccion.pack(side=tk.LEFT)

label_direccion = tk.Label(root, text="Desarrolado por Javier Romero.")
label_direccion.pack(side=tk.LEFT, padx=5)

root.mainloop()

