import tkinter as tk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
import matplotlib.pyplot as plt
import numpy as np
from ReadATP import graficar_variables_de_salida
fig = None
canvas = None
vector_conservado = None

def clear_figure():
    global fig, canvas
    if fig is not None:
        fig.clf()
        canvas.draw()
op=0
op_1 = None
op_2 = None
op_3 = None
op_4 = None
Tension_global = None
def plot_functions(option):
    global fig, canvas, vector_conservado, op, op_1, op_2, op_3, op_4, Tension_global, Corriente_descarga 

    # Definimos los parámetros de entrada
    nombre_archivo = "C:\\ATP\\work\\Prueba final tipo rayo Copia 01.lis"
    palabra_clave = "Variable maxima :"
    Numero_fases = 2
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
        plt.xlabel('Corriente [kA]')
        plt.ylabel('Valor máximo de tension vs corriente de descarga')
        plt.title('Tensión máxima de salida')
        plt.grid(True)
        op_1 = Sobretensión_generada1
        op=op+1
        vector_conservado=1
    elif option == 2:
        graficar_variables_de_salida(nombre_archivo, palabra_clave, Numero_fases)
        resultado = graficar_variables_de_salida(nombre_archivo, palabra_clave, Numero_fases)
        Corriente_descarga=resultado[0]
        Sobretensión_generada2=resultado[1]
        plt.plot(Corriente_descarga, Sobretensión_generada2,label= "Torre 2")
        plt.legend()   # Mostrar la leyenda en la gráfica
        plt.xlabel('Corriente [kA]')
        plt.ylabel('Valor máximo de tension vs corriente de descarga')
        plt.title('Tensión máxima de salida')
        plt.grid(True)
        op=op+1
        op_2 = Sobretensión_generada2
        vector_conservado=2
    elif option == 3:
        graficar_variables_de_salida(nombre_archivo, palabra_clave, Numero_fases)
        resultado = graficar_variables_de_salida(nombre_archivo, palabra_clave, Numero_fases)
        Corriente_descarga=resultado[0]
        Sobretensión_generada3=resultado[1]
        plt.plot(Corriente_descarga, Sobretensión_generada3,label= "Torre 3")
        plt.legend()   # Mostrar la leyenda en la gráfica
        plt.xlabel('Corriente [kA]')
        plt.ylabel('Valor máximo de tension vs corriente de descarga')
        plt.title('Tensión máxima de salida')
        plt.grid(True)
        op=op+1
        op_3 = Sobretensión_generada3
        vector_conservado=3
    elif option == 4:
        graficar_variables_de_salida(nombre_archivo, palabra_clave, Numero_fases)
        resultado = graficar_variables_de_salida(nombre_archivo, palabra_clave, Numero_fases)
        Corriente_descarga=resultado[0]
        Sobretensión_generada4=resultado[1]
        plt.plot(Corriente_descarga, Sobretensión_generada4,label= "Torre 4")
        plt.legend()   # Mostrar la leyenda en la gráfica
        plt.xlabel('Corriente [kA]')
        plt.ylabel('Valor máximo de tension vs corriente de descarga')
        plt.title('Tensión máxima de salida')
        plt.grid(True)
        op=op+1
        op_4 = Sobretensión_generada4
        vector_conservado=4
    elif option == 5:
        if op ==1 :
            plt.plot(Corriente_descarga, op_1, label='Sobretensión en torre 1')
            plt.grid(True)
        if op ==2 :
            plt.plot(Corriente_descarga, op_1, label='Sobretensión en torre 1')
            plt.plot(Corriente_descarga, op_2, label='Sobretensión en torre 2')
            plt.grid(True)
        if op ==3 :
            plt.plot(Corriente_descarga, op_1, label='Sobretensión en torre 1')
            plt.plot(Corriente_descarga, op_2, label='Sobretensión en torre 2')
            plt.plot(Corriente_descarga, op_3, label='Sobretensión en torre 3')
            plt.grid(True)
        if op ==4 :
            plt.plot(Corriente_descarga, op_1, label='Sobretensión en torre 1')
            plt.plot(Corriente_descarga, op_2, label='Sobretensión en torre 2')
            plt.plot(Corriente_descarga, op_3, label='Sobretensión en torre 3')
            plt.plot(Corriente_descarga, op_4, label='Sobretensión en torre 4')
            plt.grid(True)
        plt.legend()
        op=0
    elif option == 6:
        if vector_conservado == 1:
            plt.plot(Corriente_descarga, op_1, label='Conservado')
            plt.title('Sobretensión en torre 1 conservada')
            plt.grid(True)
            Tensión_global=op_1
        elif vector_conservado == 2:
            plt.plot(Corriente_descarga, op_2, label='Conservado')
            plt.title('Sobretensión en torre 2 conservada')
            plt.grid(True)
            Tension_global=op_2
        elif vector_conservado == 3:
            plt.plot(Corriente_descarga, op_3, label='Conservado')
            plt.title('Sobretensión en torre 3 conservada')
            plt.grid(True)
            Tension_global=op_3
        elif vector_conservado == 4:
            plt.plot(Corriente_descarga, op_4, label='Conservado')
            plt.title('Sobretensión en torre 4 conservada')
            plt.grid(True)
            Tension_global=op_4
    
    canvas.draw()
    return Tension_global



print(Tension_global)


def generate_buttons(n):
    global canvas
    button_texts = ["Opción {}".format(i) for i in range(1, n+1)]
    buttons = []
    for i in range(n):
        button = tk.Button(root, text=button_texts[i], command=lambda option=i+1: plot_functions(option))
        buttons.append(button)
    for button in buttons:
        button.pack(pady=5)
    button5 = tk.Button(root, text="Simular todo", command=lambda: plot_functions(5))
    button5.pack(pady=5)
    button6 = tk.Button(root, text="Conservar gráfica", command=lambda: plot_functions(6))
    button6.pack(pady=5)

def get_num_graphs():
    global fig, canvas
    num_graphs = int(entry.get())
    if num_graphs >= 1 and num_graphs <= 4:
        fig = plt.figure() # Add this line to create a new figure
        generate_buttons(num_graphs)
        label.destroy()
        entry.destroy()
        submit_button.destroy()
        canvas = FigureCanvasTkAgg(fig, master=root)
        canvas.draw()
        canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)
    else:
        error_label.config(text="Ingrese un número entre 1 y 4")

root = tk.Tk()

label = tk.Label(root, text="Ingrese el número de gráficas que desea (1-4):")
label.pack(pady=10)

entry = tk.Entry(root)
entry.pack(pady=5)

submit_button = tk.Button(root, text="Aceptar", command=get_num_graphs)
submit_button.pack(pady=5)

error_label = tk.Label(root, fg="red")
error_label.pack(pady=5)
x = np.linspace(-np.pi, np.pi, 100)
root.mainloop()