import tkinter as tk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
import matplotlib.pyplot as plt
import numpy as np
from ReadATP import graficar_variables_de_salida
import tkinter as tk
from tkinter import ttk
import random
import matplotlib.pyplot as plt
import tkinter as tk
from PIL import ImageTk, Image
import tkinter as tk
from tkinter import ttk
import matplotlib.pyplot as plt
import numpy as np
from ctypes import windll, byref, Structure, c_long, c_int
import tkinter as tk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
import matplotlib.pyplot as plt
import numpy as np
import threading
fig = None
canvas = None
vector_conservado = None

def clear_figure():
    global fig, canvas
    if fig is not None:
        fig.clf()
        canvas.draw()
op=0
Tension_global1 = None
Tension_global2 = None
Tension_global3 = None
Tension_global4 = None
Corriente = []
Tension_global1 = []
Tension_global2 = []
Tension_global3 = []
Tension_global4 = []
def plot_functions(option):
    global fig, canvas, vector_conservado, op, Tension_global1,Tension_global2,Tension_global3,Tension_global4, Corriente_descarga 

    # Definimos los parámetros de entrada
    nombre_archivo = "C:\\ATP\\work\\Prueba final tipo rayo Copia 01.lis"
    palabra_clave = "Variable maxima :"
    Numero_fases = 3
    clear_figure()
    plt.title('Sobretensiones generadas por descargas atmosféricas')
    plt.xlabel('Corriente de descarga [kA]')
    plt.ylabel('Sobretensión generada')
    if option == 1:
        graficar_variables_de_salida(nombre_archivo, palabra_clave, Numero_fases)
        resultado = graficar_variables_de_salida(nombre_archivo, palabra_clave, Numero_fases)
        Corriente_descarga=resultado[0]
        Sobretensión_generada1=resultado[1]
        plt.plot(Corriente_descarga, Sobretensión_generada1,label= "Torre 1")
        plt.legend()   # Mostrar la leyenda en la gráfica
        plt.grid(True)
        Tension_global1 = Sobretensión_generada1
        op=op+1
        vector_conservado=1
    elif option == 2:
        graficar_variables_de_salida(nombre_archivo, palabra_clave, Numero_fases)
        resultado = graficar_variables_de_salida(nombre_archivo, palabra_clave, Numero_fases)
        Corriente_descarga=resultado[0]
        Sobretensión_generada2=resultado[1]
        plt.plot(Corriente_descarga, Sobretensión_generada2,label= "Torre 2")
        plt.legend()   # Mostrar la leyenda en la gráfica
        plt.grid(True)
        op=op+1
        Tension_global2= Sobretensión_generada2
        vector_conservado=2
    elif option == 3:
        graficar_variables_de_salida(nombre_archivo, palabra_clave, Numero_fases)
        resultado = graficar_variables_de_salida(nombre_archivo, palabra_clave, Numero_fases)
        Corriente_descarga=resultado[0]
        Sobretensión_generada3=resultado[1]
        plt.plot(Corriente_descarga, Sobretensión_generada3,label= "Torre 3")
        plt.legend()   # Mostrar la leyenda en la gráfica
        plt.grid(True)
        op=op+1
        Tension_global3 = Sobretensión_generada3
        vector_conservado=3
    elif option == 4:
        graficar_variables_de_salida(nombre_archivo, palabra_clave, Numero_fases)
        resultado = graficar_variables_de_salida(nombre_archivo, palabra_clave, Numero_fases)
        Corriente_descarga=resultado[0]
        Sobretensión_generada4=resultado[1]
        plt.plot(Corriente_descarga, Sobretensión_generada4,label= "Torre 4")
        plt.legend()   # Mostrar la leyenda en la gráfica
        plt.grid(True)
        op=op+1
        Tension_global4 = Sobretensión_generada4
        vector_conservado=4
    elif option == 5:
        if op ==1 :
            plt.plot(Corriente_descarga, Tension_global1, label='Sobretensión en torre 1')
            plt.grid(True)
        if op ==2 :
            plt.plot(Corriente_descarga, Tension_global1, label='Sobretensión en torre 1')
            plt.plot(Corriente_descarga, Tension_global2, label='Sobretensión en torre 2')
            plt.grid(True)
        if op ==3 :
            plt.plot(Corriente_descarga, Tension_global1, label='Sobretensión en torre 1')
            plt.plot(Corriente_descarga, Tension_global2, label='Sobretensión en torre 2')
            plt.plot(Corriente_descarga, Tension_global3, label='Sobretensión en torre 3')
            plt.grid(True)
        if op ==4 :
            plt.plot(Corriente_descarga, Tension_global1, label='Sobretensión en torre 1')
            plt.plot(Corriente_descarga, Tension_global2, label='Sobretensión en torre 2')
            plt.plot(Corriente_descarga, Tension_global3, label='Sobretensión en torre 3')
            plt.plot(Corriente_descarga, Tension_global4, label='Sobretensión en torre 4')
            plt.grid(True)
        plt.legend()
        op=0
    elif option == 6:
        if vector_conservado == 1:
            plt.plot(Corriente_descarga, Tension_global1, label='Conservado')
            plt.title('Sobretensión en torre 1 conservada')
            plt.grid(True)
            print(len(Corriente_descarga))
            print(Corriente_descarga)
            print(len(Tension_global1))
            print(Tension_global1)
        elif vector_conservado == 2:
            plt.plot(Corriente_descarga, Tension_global2, label='Conservado')
            plt.title('Sobretensión en torre 2 conservada')
            plt.grid(True)
            print(Tension_global2)
        elif vector_conservado == 3:
            plt.plot(Corriente_descarga, Tension_global3, label='Conservado')
            plt.title('Sobretensión en torre 3 conservada')
            plt.grid(True)
            print(Tension_global3)
        elif vector_conservado == 4:
            plt.plot(Corriente_descarga, Tension_global4, label='Conservado')
            plt.title('Sobretensión en torre 4 conservada')
            plt.grid(True)
            print(Tension_global4)
    canvas.draw()
    return Tension_global1,Tension_global2,Tension_global3,Tension_global4

def generate_buttons(n):
    global canvas
    button_texts = ["Opción {}".format(i) for i in range(1, n+1)]
    button_frame = tk.Frame(tab2)  # Creamos un Frame para contener los botones
    button_frame.pack(side=tk.TOP, padx=5, pady=5)  # Empaquetamos el Frame en la ventana
    buttons = []
    for i in range(n):
        button = tk.Button(button_frame, text=button_texts[i], command=lambda option=i+1: plot_functions(option))
        buttons.append(button)
        button.pack(side=tk.LEFT, padx=5)  # Empaquetamos cada botón en el Frame
    button5 = tk.Button(tab2, text="Simular todo", command=lambda: plot_functions(5))
    button5.pack(pady=5)
    button6 = tk.Button(tab2, text="Conservar gráfica", command=lambda: plot_functions(6))
    button6.bind(("<Button-1>", ))
    button6.pack(pady=5)

def get_num_graphs():
    global fig, canvas
    num_graphs = int(entry.get())
    if num_graphs >= 1 and num_graphs <= 4:
        fig = plt.figure(figsize=(1, 1)) # Cambia el tamaño de la figura a 3x2 pulgadas
        generate_buttons(num_graphs)
        label.destroy()
        entry.destroy()
        submit_button.destroy()
        canvas = FigureCanvasTkAgg(fig, master=tab2)
        canvas.draw()
        canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1, padx=1, pady=1) 
    else:
        error_label.config(text="Ingrese un número entre 1 y 4")

root = tk.Tk()
# Obtenemos la altura de la barra de tareas en Windows
class RECT(Structure):
    _fields_ = [('left', c_long), ('top', c_long), ('right', c_long), ('bottom', c_long)]
rect = RECT()
windll.user32.SystemParametersInfoW(0x0030, 0, byref(rect), 0)
barra_tareas_alto = root.winfo_screenheight() - rect.bottom

# Establecemos la geometría de la ventana
ancho = root.winfo_screenwidth() - 100
alto = root.winfo_screenheight() - barra_tareas_alto - 100
root.geometry(f"{ancho}x{alto}+50+50")  # con margen de 50 pixeles en cada lado
root.minsize(ancho, alto)  # tamaño mínimo de la ventana

# Establecer tamaño de fuente y espaciado
fuente = ("Arial", 12)
espaciado = 10

# Título de la ventana
root.title("Aplicación para la coordinación de aislamiento por el método estadístico")

# Creamos un widget Notebook (pestañas)
notebook = ttk.Notebook(root)
notebook.pack(fill='both', expand='yes')

# Creamos dos pestañas
tab1 = ttk.Frame(notebook)
tab2 = ttk.Frame(notebook)
tab3 = ttk.Frame(notebook)
tab4 = ttk.Frame(notebook)
tab5 = ttk.Frame(notebook)

notebook.add(tab1, text='Pestaña 1')
notebook.add(tab2, text='Pestaña 2')
notebook.add(tab3, text='Pestaña 3')
notebook.add(tab4, text='Pestaña 4')
notebook.add(tab5, text='Pestaña 5')

# Cargar la imagen de fondo
img = Image.open(r"C:\Users\Sofia\Desktop\Noveno semestre\PF\Fondointerfaz.jpg")
img = img.resize((ancho, alto), Image.ANTIALIAS) # Redimensionar la imagen
img_tk = ImageTk.PhotoImage(img)

# Crear una etiqueta con la imagen de fondo en cada pestaña
fondo1 = tk.Label(tab1, image=img_tk)
fondo1.place(x=0, y=0)

fondo2 = tk.Label(tab2, image=img_tk)
fondo2.place(x=0, y=0)

fondo3 = tk.Label(tab3, image=img_tk)
fondo3.place(x=0, y=0)

fondo4 = tk.Label(tab4, image=img_tk)
fondo4.place(x=0, y=0)

fondo5 = tk.Label(tab5, image=img_tk)
fondo5.place(x=0, y=0)
label = tk.Label(tab2, text="Ingrese el número de gráficas que desea (1-4):")
label.pack(pady=10)
entry = tk.Entry(tab2)
entry.pack(pady=5)
submit_button = tk.Button(tab2, text="Aceptar", command=get_num_graphs)
submit_button.pack(pady=5)
error_label = tk.Label(tab2, fg="red")
error_label.pack(pady=5)
root.mainloop()