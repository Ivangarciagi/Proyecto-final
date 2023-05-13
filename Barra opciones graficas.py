import tkinter as tk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
import matplotlib.pyplot as plt
import numpy as np

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
def plot_functions(option):
    global fig, canvas, vector_conservado, op, op_1, op_2, op_3, op_4, Tensión_global
    
    x = np.linspace(-np.pi, np.pi, 1000)

    clear_figure()
    plt.title('Funciones trigonométricas')
    plt.xlabel('Eje X')
    plt.ylabel('Eje Y')
    if option == 1:
        q = np.sin(x)
        plt.plot(x, q,label='Seno (x)')
        plt.title('Seno(x)')
        plt.xlabel('Eje X')
        plt.ylabel('Eje Y')
        plt.grid(True)
        op_1 = q
        op=op+1
        vector_conservado=1
    elif option == 2:
        r = np.cos(x)
        plt.plot(x, r,label='Cos (x)')
        plt.title('cos(x)')
        plt.xlabel('Eje X')
        plt.ylabel('Eje Y')
        plt.grid(True)
        op=op+1
        op_2 = r
        vector_conservado=2
    elif option == 3:
        s = np.tan(x)
        plt.plot(x, s,label='Tan (x)')
        plt.title('tan(x)')
        plt.xlabel('Eje X')
        plt.ylabel('Eje Y')
        plt.grid(True)
        op=op+1
        op_3 = s
        vector_conservado=3
    elif option == 4:
        t = np.exp(x)
        plt.plot(x, t,label='e(x)')
        plt.title('e(x)')
        plt.xlabel('Eje X')
        plt.ylabel('Eje Y')
        plt.grid(True)
        op=op+1
        op_4 = t
        vector_conservado=4
    elif option == 5:
        if op ==1 :
            plt.plot(x, op_1, label='Sin(x)')
            plt.grid(True)
        if op ==2 :
            plt.plot(x, op_1, label='Sin(x)')
            plt.plot(x, op_2, label='Cos(x)')
            plt.grid(True)
        if op ==3 :
            plt.plot(x, op_1, label='Sin(x)')
            plt.plot(x, op_2, label='Cos(x)')
            plt.plot(x, op_3, label='Tan(x)')
            plt.grid(True)
        if op ==4 :
            plt.plot(x, op_1, label='Sin(x)')
            plt.plot(x, op_2, label='Cos(x)')
            plt.plot(x, op_3, label='Tan(x)')
            plt.plot(x, op_4, label='exp(x)')
            plt.grid(True)
        plt.legend()
        op=0
    elif option == 6:
        if vector_conservado == 1:
            plt.plot(x, op_1, label='Vector conservado')
            plt.title('Vano 1 conservado')
            plt.grid(True)
            Tensión_global=op_1
        elif vector_conservado == 2:
            plt.plot(x, op_2, label='Vector conservado')
            plt.title('Vano 2 conservado')
            plt.grid(True)
            Tensión_global=op_2
        elif vector_conservado == 3:
            plt.plot(x, op_3, label='Vector conservado')
            plt.title('Vano 3 conservado')
            plt.grid(True)
            Tensión_global=op_3
        elif vector_conservado == 4:
            plt.plot(x, op_4, label='Vector conservado')
            plt.title('Vano 4 conservado')
            plt.grid(True)
            Tensión_global=op_4
    
    canvas.draw()

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