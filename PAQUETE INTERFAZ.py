import tkinter as tk
from tkinter import ttk
import random
import matplotlib.pyplot as plt
from PIL import ImageTk, Image
import numpy as np
from ctypes import windll, byref, Structure, c_long, c_int
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
import threading
from matplotlib.figure import Figure
from ReadATP import graficar_variables_de_salida
import scipy.stats as stats
from scipy.stats import rv_histogram, weibull_min, spearmanr
import numpy as np
import math
import scipy.stats as stats
import matplotlib.pyplot as plt
from scipy.stats import rv_histogram, weibull_min
from scipy.stats import spearmanr
from scipy.integrate import quad
import numpy as np
from scipy.special import gamma, gammainc
global PV, Riesgo_int, Confiabilidad_int, N_int, Simulaciones, NDSU_int, Años_int, TFIL_int, T_total_int
canvas = None
vector_conservado = None
I1 = []
I2 = []
I3 = []
I4 = []
I = []
op=0
op_1 = None
op_2 = None
op_3 = None
op_4 = None
Corriente = []
PV = []
Pt = []
PV1 = []
PV2 = []
PV3 = []
PV4 = []
PV_sin_ceros=[]
Riesgo_int=0
Confiabilidad_int=0
N_int=0
NDSU_int=0
Años_int=0
TFIL_int=0
T_total_int=0

Riesgo_ext=0
Confiabilidad_ext=0
N_ext=0
NDSU_ext=0
Años_ext=0
TFIL_ext=0
T_total_ext=0
Proteccion_maniobra = 0
Proteccion_rayo = 0
Distancia_min_ff = 0
Distancia_min_fe = 0
Up2 = 0
Upt = 0 
Ue2 = 0
Uet = 0
def simular():
    global Corriente, I, Simulaciones, Ancho_Impacto, Longitud_línea,Longitud_vano1,Longitud_vano2,Longitud_vano3,Longitud_vano4, I1, I2, I3, I4
    # Capturar los valores de los entry boxes
    Simulaciones = int(entry_sim.get())
    Ancho_Impacto = float(entry_ancho.get())
    Longitud_línea = float(entry_long.get())
    Longitud_vano1 = float(entry_long1.get())
    Longitud_vano2 = float(entry_long2.get())
    Longitud_vano3 = float(entry_long3.get())
    Longitud_vano4 = float(entry_long4.get())
    Ancho_ImpactoLinea=Ancho_Impacto*0.5
    Impacto=0
    Impacto_torre1=0
    Impacto_torre2=0
    Impacto_torre3=0
    Impacto_torre4=0
    # Crear una nueva figura con tamaño personalizado
    plt.figure(figsize=(10, 6))
    # Lista para almacenar los valores de la variable aleatoria
    I_valor_variable_aleatoria = []
    # Habilitar el modo interactivo para mostrar el gráfico en la misma ventana
    for i in range(Simulaciones):
        #1 Generación aleatoria de P(I), determinar mediante el método de monte Carlo la probabilidad de ocurrencia de una variable:
        Probabilidad_de_ocurrencia = random.uniform(0, 1)
        #2 Cálculo de I (kA) y de S [m]: determina el valor de la variable aleatoria a generarse dependiendo de la probabilidad
        I_valor_variable_aleatoria = ((((1/Probabilidad_de_ocurrencia-1)) ** (2/5))) * 20
        #3 El radio S asociado a cada descarga generada, se obtiene de la siguiente expresión:
        S_aleatorio=8*(I_valor_variable_aleatoria)**(0.65)
        #4 Polaridad de la descarga:
        valores = [-1, 1]  # los valores a asignar probabilidades de ocurrencia de las descargas atmosféricas
        probabilidades_polaridad= [0.98, 0.02]  # las probabilidades correspondientes a cada valor
        resultado = random.choices(valores, probabilidades_polaridad)[0]  # genero un valor aleatorio según las probabilidades
        #5 Definición aleatoria de x,y y de distancia de la línea de transmisión:
        x = random.randint(0, Longitud_línea)
        y = random.randint(0, Ancho_Impacto)
        #6  Verificación de que la descarga entre o no al c. de guarda:  El criterio para definir si 
        #una descarga impacta sobre el cable de guarda es:S ≥ Dis
        RAIZ=float((Ancho_ImpactoLinea-y)**(2))
        DIS=RAIZ**(1/2)
        DIS = float(DIS)
        if not S_aleatorio>=DIS:
            # código a ejecutar si la condición es falsa
            plt.scatter(x, y,label='Descargas atmosféricas', s=5, alpha=0.3, color='blue')
        else:
            # código a ejecutar si la condición es verdadera
            plt.scatter(x, Ancho_ImpactoLinea,label='Descargas atmosféricas', s=2, alpha=0.3, color='blue')
            Impacto=Impacto+1
            D1=(Longitud_línea - Longitud_vano1)
            D2=D1 - (Longitud_vano2)
            D3=D2 - (Longitud_vano3)
            D4=D3-(Longitud_vano4)
            if D1 <= x <= Longitud_línea:
                I1.append(round( I_valor_variable_aleatoria))
                Impacto_torre1 = Impacto_torre1+1
            if D2 <= x < D1:
                I2.append(round( I_valor_variable_aleatoria))
                Impacto_torre2 = Impacto_torre2+1
            if D3 <= x < D2:
                Impacto_torre3 = Impacto_torre3+1
                I3.append(round( I_valor_variable_aleatoria))
            if x < D3:
                Impacto_torre4 = Impacto_torre4+1
                I4.append(round( I_valor_variable_aleatoria))
        #Prueba para los valores de longitud
        # Ajustamos los límites del eje y a 0 y 311 metros, y el eje x a 0 y 1000 metros
        plt.ylim(0, Ancho_Impacto)
        plt.xlim(0, Longitud_línea)

    # Añadimos una línea recta en la mitad del eje Y, de color rojo y ancho 1 para simular la línea de transmisión
    # Creamos un widget Label para mostrar la variable de salida con las descargas que impactaron las torres
    label_Impacto_torre1 = tk.Label(tab1, text="Impacto_torre1: {}".format(Impacto_torre1))
    label_Impacto_torre1.place(x=50, y=50)
    label_Impacto_torre2 = tk.Label(tab1, text="Impacto_torre2: {}".format(Impacto_torre2))
    label_Impacto_torre2.place(x=50, y=100)
    label_Impacto_torre3 = tk.Label(tab1, text="Impacto_torre3: {}".format(Impacto_torre3))
    label_Impacto_torre3.place(x=50, y=150)
    label_Impacto_torre4 = tk.Label(tab1, text="Impacto_torre4: {}".format(Impacto_torre4))
    label_Impacto_torre4.place(x=50, y=200)
    
    plt.axhline(y=Ancho_ImpactoLinea, color='red', linewidth=1)
    # Añadimos título, etiquetas y grid
    plt.title("Generación aleatoria de descargas")
    plt.xlabel("Longitud del tramo de la línea (metros)")
    plt.ylabel("Distancia del ancho atractivo")
    plt.grid(True)

    # Añadimos un cuadro de texto para mostrar el número de repeticiones
    # Añadimos un cuadro de texto para mostrar el número de repeticiones y el número de impactos
    textstr = f'Número de repeticiones: {Simulaciones}\nNúmero de impactos: {Impacto}'
    props = dict(boxstyle='round', facecolor='white', alpha=0.5)
    props = dict(boxstyle='round', facecolor='white', alpha=0.5)
    plt.text(0.05, 0.95, textstr,transform=plt.gca().transAxes, fontsize=10,
            verticalalignment='top', bbox=props)

    # Mostramos el plot
    Corriente = I
    plt.show()
    return (Corriente)



# Crear la ventana y los entry boxes
ventana = tk.Tk()

# Obtenemos la altura de la barra de tareas en Windows
class RECT(Structure):
    _fields_ = [('left', c_long), ('top', c_long), ('right', c_long), ('bottom', c_long)]
rect = RECT()
windll.user32.SystemParametersInfoW(0x0030, 0, byref(rect), 0)
barra_tareas_alto = ventana.winfo_screenheight() - rect.bottom

# Establecemos la geometría de la ventana
ancho = ventana.winfo_screenwidth() - 100
alto = ventana.winfo_screenheight() - barra_tareas_alto - 100
ventana.geometry(f"{ancho}x{alto}+50+50")  # con margen de 50 pixeles en cada lado
ventana.minsize(ancho, alto)  # tamaño mínimo de la ventana

def clear_figure():
    global fig, canvas
    if fig is not None:
        fig.clf()
        canvas.draw()
op=0
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
    plt.ylabel('Sobretensión generada [V]')
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
            print("Tension_global1:",Tension_global1, len(Tension_global1))
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
        elif vector_conservado == 2:
            plt.plot(Corriente_descarga, Tension_global2, label='Conservado')
            plt.title('Sobretensión en torre 2 conservada')
            plt.grid(True)
        elif vector_conservado == 3:
            plt.plot(Corriente_descarga, Tension_global3, label='Conservado')
            plt.title('Sobretensión en torre 3 conservada')
            plt.grid(True)
        elif vector_conservado == 4:
            plt.plot(Corriente_descarga, Tension_global4, label='Conservado')
            plt.title('Sobretensión en torre 4 conservada')
            plt.grid(True)
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
        canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=30, padx=1, pady=1) 
    else:
        error_label.config(text="Ingrese un número entre 1 y 4")
        

def ejecutar_histograma():
    index = 0 # Inicializar la variable index
    # Copia y pega aquí el código que proporcionaste
    global PV
    for i in I1:
        if i in Corriente_descarga:
            index = Corriente_descarga.index(i)
            index2 = I1.index(i)
        if index < len(Tension_global1):
            PV1.append(Tension_global1[index])
    for i in I2:
        if i in Corriente_descarga:
            index = Corriente_descarga.index(i)
            index2 = I2.index(i)
        if index < len(Tension_global2):
            PV2.append(Tension_global2[index])

    for i in I3:
        if i in Corriente_descarga:
            index = Corriente_descarga.index(i)
            index2 = I3.index(i)
        if index < len(Tension_global3):
            PV3.append(Tension_global3[index])

    for i in I4:
        if i in Corriente_descarga:
            index = Corriente_descarga.index(i)
            index2 = I4.index(i)
        if index < len(Tension_global4):
            PV4.append(Tension_global4[index])
    PV=PV1+PV2+PV3+PV4
    PV_sin_ceros = [x for x in PV if x != 0]
    n, bins, patches = plt.hist(PV_sin_ceros, range=(min(PV_sin_ceros), max(PV_sin_ceros)), edgecolor='black', color='navy', alpha=0.8, linewidth=1.5, zorder=2)
    # Crear una figura de Matplotlib
    fig = plt.Figure(figsize=(8, 6), dpi=100)
    # Agregar un subplot a la figura
    ax = fig.add_subplot(1, 1, 1)
    
    # Crear la gráfica
    ax.hist(PV_sin_ceros, bins=10, alpha=0.75, edgecolor='black')
    # Asignar zorder mayor a las columnas del histograma que al grid
    ax.set_xlim((min(PV_sin_ceros), max(PV_sin_ceros)))
    ax.set_xticks(np.arange(min(PV_sin_ceros), max(PV_sin_ceros)+1, 100000))
    ax.set_xticklabels(['{:,.3f}'.format(x/1000) for x in ax.get_xticks()])
    for i, patch in enumerate(ax.patches):
        bin_center = (patch.xy[0] + patch.get_width() / 2)
        ax.text(bin_center, patch.get_height(), str(int(n[i])), ha='center', va='bottom', fontsize=14, fontweight='bold')

    ax.set_title('Histograma de Sobretensiones', fontsize=14, fontweight='bold')
    ax.set_xlabel('Sobretensión [kV]', fontsize=12, fontweight='bold')
    ax.set_ylabel('Número de veces', fontsize=12, fontweight='bold')
    ax.grid(axis='y', alpha=0.75)
    ax.grid(axis='x', alpha=0.75)


    # Crear un objeto de lienzo de tkinter para la figura
    canvas = FigureCanvasTkAgg(fig, master=tab3)
    canvas.draw()

    # Posicionar el lienzo en el centro de la ventana
    canvas.get_tk_widget().place(relx=0.5, rely=0.5, anchor=tk.CENTER)

 
def ejecutar_Weibull():
    global PV
    PV=[val/(1e3) for val in PV]
    # Crear la ventana principal
    def weib_f(x):

        x=(x-loc)/scale
        term1= (1-np.exp(-1*(x**c)))
        term2= np.exp(-1*(x**c))
        term3= x**(c-1)
        fx = a*c*((term1)**(a-1))*term2*term3
        
        return (fx/scale)* bins_diff
    fig, ax = plt.subplots(figsize=(8, 6))
    x=np.linspace(min(PV),max(PV),10000)
    weights=np.ones(len(PV))/len(PV)
    count, bins, bars = ax.hist(PV, weights=weights, bins=10, alpha=0.6, ec="black", label="Histograma")
    ax.legend()
    bins_diff= np.diff(bins)[0]
    #Cear weibull 
    weibull_data = stats.exponweib.fit(sorted(PV), loc=0)
    a= weibull_data[0]
    c= weibull_data [1]
    loc= weibull_data [2]
    scale= weibull_data [3]
# -----------------CALCULO Y COMPARACIÓN DE MEDIA Y DESVIACIÓN ESTANDAR
    PV_mean = np.mean(PV)  
#------------------ DEFINICIÓN DE FUNCION WEIBULL
    ax.annotate(f"Media R.= {PV_mean:.2f}", xy=(0.05, 0.95), xycoords='axes fraction')
    ax.grid(True)
    ax.plot(x,  weib_f(x), label="Weibull" )
    ax.set_xlabel('Sobretensiones')
    ax.set_ylabel('Densidad de probabilidad')
    ax.set_title('Distribución de probabilidad')
    ax.legend()
    canvas = FigureCanvasTkAgg(fig, master=tab3)
    canvas.draw()
    # Posicionar el lienzo en el centro de la ventana
    canvas.get_tk_widget().place(relx=0.5, rely=0.5, anchor=tk.CENTER)

def Aislamiento_Interno():
    global PV, Riesgo_int, Confiabilidad_int, N_int, Simulaciones, NDSU_int, Años_int, TFIL_int, T_total_int
    plt.close('all')
    Aislamiento_Int = int(Entry_Ais_Int.get())
    def weib_f(x):

        x=(x-loc)/scale
        term1= (1-np.exp(-1*(x**c)))
        term2= np.exp(-1*(x**c))
        term3= x**(c-1)
        fx = a*c*((term1)**(a-1))*term2*term3
        
        return (fx/scale)* bins_diff

    #----------------------------DEFINICION DE DATOS DEL HISTOGRAMA
    x=np.linspace(min(PV),max(PV),10000)
    weights=np.ones(len(PV))/len(PV)
    count, bins, bars = plt.hist(PV, weights=weights, bins=10, alpha=0.6, ec="black", label="Histograma sobretensiones")
    bins_diff= np.diff(bins)[0]

    #---------------------------DEFINICION DE PARÁMETROS WEIBULL SEGUN DATOS ORIGINALES
    weibull_data = stats.exponweib.fit(sorted(PV), loc=0)
    a= weibull_data[0]
    c= weibull_data [1]
    loc= weibull_data [2]
    scale= weibull_data [3]
    #--------------------------- INTEGRACIÓN DE WEIBULL PARA CALCULAR EL RIESGO ASOCIADO A UN NIVEL DE AISLAMIENTO
    #--------------------------- NO REGENERATIVO
    def integrand(x):
        x=(x-loc)/scale
        term1= (1-np.exp(-1*(x**c))) 
        term2= np.exp(-1*(x**c))
        term3= x**(c-1)
        fx = a*c*((term1)**(a-1))*term2*term3
        
        return ((fx/scale)* bins_diff)

    #----------------------------DEFINICIÓN DE NIVEL DE TENSIÓN DE SOPORTABILIDAD UCW
    A_NR=Aislamiento_Int
    A_NR=A_NR/1.15
    #----------------------------LLAMADA A LA FUNCIÓN PARA INTEGRARLA EN LOS LÍMITES ESTABLECIDOS
    result, error = quad(integrand, A_NR, max(PV))
    #----------------------------CÁLCULO DE LOS RESULTADOS DE LA COORDINACIÓN DE AISLAMIENTO
    Riesgo_int = result
    Riesgo_int=round(Riesgo_int, 4)
    Confiabilidad_int = 100-Riesgo_int
    Confiabilidad_int=round( Confiabilidad_int, 4)
    N_int = Simulaciones
    NDSU_int = N_int * (Riesgo_int)/100
    NDSU_int=round(NDSU_int, 4)
    Años_int = Simulaciones /((0.3)*(0.000001)*(Ancho_Impacto*Longitud_línea))
    Años_int=round(Años_int, 4)
    TFIL_int = Años_int/NDSU_int
    TFIL_int=round(TFIL_int, 4)
    T_total_int = 1/(TFIL_int)
    T_total_int=round(T_total_int, 4)
    # Obtener los valores actuales del item "I001"
    current_values = two.item("I001")["values"]
    current_values2 = two.item("I002")["values"]
    current_values3 = two.item("I003")["values"]
    current_values4 = two.item("I004")["values"]
    current_values5 = two.item("I005")["values"]
    current_values6 = two.item("I006")["values"]
    #----------------------------REMPLAZAR LOS VALORES DE LA LISTA EN LA TABLA DE TKINTER
    new_Riesgo=[Riesgo_int,current_values[1]]
    two.item(("I001"), values=new_Riesgo)
    new_Confiabilidad=[Confiabilidad_int,current_values2[1]]
    two.item(("I002"), values=new_Confiabilidad)
    new_NDSU=[NDSU_int,current_values3[1]]
    two.item(("I003"), values=new_NDSU)
    new_Años=[Años_int,current_values4[1]]
    two.item(("I004"), values=new_Años)
    new_Fallas=[TFIL_int,current_values5[1]]
    two.item(("I005"), values=new_Fallas)
    new_Tasas=[T_total_int,current_values6[1]]
    two.item(("I006"), values=new_Tasas)
    #----------------------------DEFINICIÓN DE LA INFORMACIÓN MOSTRADA EN EL PLOT
   
    plt.plot(x,  weib_f(x), label="Función weibull" )
    plt.text(0.6, 0.8, f'Riesgo: {result}', transform=plt.gca().transAxes, va='top')
    plt.title("Gráfica de sobretensiones")
    plt.xlabel("Sobretensiones [KV]")
    plt.ylabel("Probabilidad")
    plt.legend()
    plt.axvline(x=Aislamiento_Int, color='r', label="LIWL")
    plt.legend()
    plt.grid(True)
    plt.show()
    
def Aislamiento_Externo():
    global PV, Riesgo_ext, Confiabilidad_ext, N_ext, Simulaciones, NDSU_ext, Años_ext, TFIL_ext, T_total_ext
    plt.close('all')
    Aislamiento_ext = int(Entry_Aislamiento_ext.get())
    Altura = int(Entry_Altura_mar.get())
    # Crear la ventana principal
    def weib_f(x):

        x=(x-loc)/scale
        term1= (1-np.exp(-1*(x**c)))
        term2= np.exp(-1*(x**c))
        term3= x**(c-1)
        fx = a*c*((term1)**(a-1))*term2*term3
        
        return (fx/scale)* bins_diff
    fig, ax = plt.subplots()
    x=np.linspace(min(PV),1500,10000)
    weights=np.ones(len(PV))/len(PV)
    bins= np.linspace(np.min(PV), np.max(PV), 11)
    bins_diff= np.diff(bins)[0]
    #Cear weibull 
    weibull_data = stats.exponweib.fit(sorted(PV), loc=0)
    a= weibull_data[0]
    c= weibull_data [1]
    loc= weibull_data [2]
    scale= weibull_data [3]
    ax.grid(True)
    ax.plot(x,  weib_f(x), label="Distribución Weibull" )
    ax.legend()
    ax.set_ylim(bottom=0)
    #---------------------------FUNCION QUE REPRESENTA LA PROBABILIDAD DE FALLO DEL AISLAMIENTO
    AR=Aislamiento_ext
    KSE = 1.05
    H=Altura
    KAT = 1*np.exp((H)/(8150)) 
    U10=AR/((KSE)*(KAT))
    U50=U10/(1-1.28*(3/100))
    Z=0.03*U50
    U0=U50-4*Z
    U=np.linspace(U0,max(PV),1000)
    x=(U-U50)/Z
    PU_R=1-0.5**((1+(x/4))**5)


    def integrand(x):
            global AR, KSE
            AR=int(Entry_Aislamiento_ext.get())
            KSE = 1.05
            H= int(Entry_Altura_mar.get())
            KAT = 1*np.exp((H)/(8150)) 
            U10=AR/((KSE)*(KAT))
            U50=U10/(1-1.28*(3/100))
            Z=0.03*U50
            PU_R=1-0.5**((1+(((x-U50)/Z)/4))**5)   
            
            x=(x-loc)/scale
            term1= (1-np.exp(-1*(x**c))) 
            term2= np.exp(-1*(x**c))
            term3= x**(c-1)
            fx = a*c*((term1)**(a-1))*term2*term3
    
            return ((fx/scale)* bins_diff)*PU_R
    max_val = 1500
    Riesgo_ext, error = quad(integrand,U50-4*Z, max(PV))
    Riesgo_ext=round(Riesgo_ext, 4)
    Confiabilidad_ext = 100-Riesgo_ext
    N_ext = Simulaciones
    NDSU_ext = N_ext * (Riesgo_ext)/100
    NDSU_ext=round(NDSU_ext, 4)
    Años_ext = Simulaciones /((0.3)*(0.000001)*(Ancho_Impacto*Longitud_línea))
    Años_ext=round(Años_ext, 4)
    TFIL_ext = Años_ext/NDSU_ext
    T_total_ext = 1/(TFIL_ext)
    T_total_ext=round(T_total_ext, 5)
    #---------------------------------ACTUALIZACION DE VALORES PARA EL AISLAMIENTO EXTERNO DE LA SUBESTACIÓN
    # Obtener los valores actuales del item "I001"
    current_values = two.item("I001")["values"]
    current_values2 = two.item("I002")["values"]
    current_values3 = two.item("I003")["values"]
    current_values4 = two.item("I004")["values"]
    current_values5 = two.item("I005")["values"]
    current_values6 = two.item("I006")["values"]
    #----------------------------REMPLAZAR LOS VALORES DE LA LISTA EN LA TABLA DE TKINTER
    new_Riesgo=[current_values[0],Riesgo_ext]
    two.item(("I001"), values=new_Riesgo)
    new_Confiabilidad=[current_values2[0],Confiabilidad_ext]
    two.item(("I002"), values=new_Confiabilidad)
    new_NDSU=[current_values3[0],NDSU_ext]
    two.item(("I003"), values=new_NDSU)
    new_Años=[current_values4[0],Años_ext]
    two.item(("I004"), values=new_Años)
    new_Fallas=[current_values5[0],TFIL_ext]
    two.item(("I005"), values=new_Fallas)
    new_Tasas=[current_values6[0],T_total_ext]
    two.item(("I006"), values=new_Tasas)   
        #----------------------------CÁLCULO DE LOS RESULTADOS DE LA COORDINACIÓN DE AISLAMIENTO
    plt.plot(U,PU_R, label="Prob. Falla aislamiento")
    plt.text(0.6, 0.8, f'Riesgo Externo: {Riesgo_ext}', transform=plt.gca().transAxes, va='top')
    plt.legend()
    plt.show()
    
def Representativas_Fase_pico():
    Sigma_f_f = 1.65546908E-01
    Sigma_f_e = 1.36632140E-01
    global Up2, Upt, Ue2, Uet
#-------------------VALOR REPRESENTATIVO FASE - FASE
    Up2 = (Sigma_f_f)/0.25+1.73
    Upt = 1.25*Up2-0.43
#-------------------VALOR REPRESENTATIVO FASE - TIERRA
    Ue2 = (Sigma_f_e)/0.25+1
    Uet = 1.25*Ue2-0.25
    print(Upt, Uet)

def Representativas_Caso_pico():
    Sigma_f_f = 1.65546908E-01
    Sigma_f_e = 1.36632140E-01
    global Up2, Upt, Ue2, Uet
#-------------------VALOR REPRESENTATIVO FASE - FASE
    Up2 = (Sigma_f_f)/0.25+1.73
    Upt = 1.14*Up2-0.24
#-------------------VALOR REPRESENTATIVO FASE - TIERRA
    Ue2 = (Sigma_f_e)/0.17+1
    Uet = 1.13*Up2-0.13
    print(Upt, Uet)
    
def Distancias_mínimas():
    global Up2, Upt, Ue2, Uet
    #--------------------------SOBRETENSIONES FASE - FASE VOLTAJE PICO---------------------------------------------
    #--------------------------SOBRETENSIONES FASE - TIERRA VOLTAJE PICO---------------------------------------------
    # ----------------------CÁLCULO DE SOBRETENSIONES REPRESENTATIVAS
    Aislamiento_rayo_int = 1550
    Aislamiento_rayo_ext = 1425
    Us = 500
#--------------DEFINICIÓN DE CONSTANTES DE SEGURIDAD Y ATMOSFÉRICA PARA EL CÁLCULO DEL AISLAMIENTO PARA MANIOBRA------
    k_int = 1.15
    k_ext = 1.05
    K_atm = 1
    Kfalla = 1.15
#--------------DEFINICIÓN DEL AISLAMIENTO--------------------------------------------------------------
    U_rw_interno = Ue2*Us*((math.sqrt(2))/(math.sqrt(3)))*Kfalla*k_int
    U_rw_externo = Ue2*Us*((math.sqrt(2))/(math.sqrt(3)))*Kfalla*k_ext*K_atm
    print(U_rw_interno)
    print(U_rw_externo)
    U_rw_interno_f_F = Up2*Us*((math.sqrt(2))/(math.sqrt(3)))*k_int
    U_rw_externo_f_t = Up2*Us*((math.sqrt(2))/(math.sqrt(3)))*k_ext*K_atm
    print(U_rw_interno_f_F)
    print(U_rw_externo_f_t)
#--------------VALORES INICIALES PARA EL AISLAMIENTO-----------------------------
    Proteccion_rayo = 0
    Proteccion_maniobra = 0
    Dis_min_ff = 0
    Dis_min_fe = 0
    #------------------- NIVEL DE 362KV DADO POR NORMA IEC 60071-1
    UR1_362_M1 = 950
    UR2_362_M1 = 1050
    UR1_362_M2 = 1050
    UR2_362_M2 = 1175
    UM1_362 = 850
    UM2_362 = 950


    #------------------- NIVEL DE 420KV DADO POR NORMA IEC 60071-1
    UR1_420_M1 = 1050
    UR2_420_M1 = 1175
    UR1_420_M2 = 1175
    UR2_420_M2 = 1300
    UR1_420_M3 = 1300
    UR2_420_M3 = 1425
    UM1_420 = 850
    UM2_420 = 950
    UM3_420 = 950




    #------------------- NIVEL DE 550KV DADO POR NORMA IEC 60071-1
    UR1_M1 = 1175
    UR2_M1 = 1300
    UR1_M2 = 1300
    UR2_M2 = 1425
    UR1_M3 = 1425
    UR2_M3 = 1550
    UM1 = 950
    UM2 = 1050 
    UM3 = 1175

    #------------------- NIVEL DE 800KV DADO POR NORMA IEC 60071-1
    UR1_800_M1 = 1675
    UR2_800_M1 = 1800
    UR1_800_M2 = 1800
    UR2_800_M2 = 1950
    UR1_800_M3 = 1950
    UR2_800_M3 = 2100
    UM1_800 = 1300
    UM2_800 = 1425
    UM3_800 = 1550
    #---------------------VALIDACIÓN NIVEL DE AISLAMIENTO NORMALIZADO DE 362KV
    if Aislamiento_rayo_int <= UR1_362_M1 and Aislamiento_rayo_ext <= UR1_362_M1 and U_rw_externo <= UM1_362 and U_rw_interno <= UM1_362 and U_rw_interno_f_F <= UM1_362 and U_rw_externo_f_t <= UM1_362:
        print("El nivel de aislamiento normalizado escogido para tipo rayo es : ",UR1_362_M1, "El nivel de aislamiento normalizado escogido para maniobra es: ", UM1_362)
        Proteccion_rayo = UR1_362_M1
        Proteccion_maniobra = UM1_362
    elif Aislamiento_rayo_int <=UR2_362_M1 and Aislamiento_rayo_ext <= UR2_362_M1 and U_rw_externo <= UM1_362 and U_rw_interno <= UM1_362 and U_rw_interno_f_F <= UM1_362 and U_rw_externo_f_t <= UM1_362:
        print("El nivel de aislamiento normalizado escogido para tipo rayo es : ",UR2_362_M1, "El nivel de aislamiento normalizado escogido para maniobra es: ", UM1_362)
        Proteccion_rayo = UR2_362_M1
        Proteccion_maniobra = UM1_362   
        
    elif Aislamiento_rayo_int <= UR1_362_M2 and Aislamiento_rayo_ext <= UR1_362_M2 and U_rw_externo <= UM2_362 and U_rw_interno <= UM2_362 and U_rw_interno_f_F <= UM2_362 and U_rw_externo_f_t <= UM2_362:
        print("El nivel de aislamiento normalizado escogido para tipo rayo es : ",UR1_362_M2, "El nivel de aislamiento normalizado escogido para maniobra es: ", UM2_362)
        Proteccion_rayo = UR1_362_M2
        Proteccion_maniobra = UM2_362    
    elif Aislamiento_rayo_int <= UR2_362_M2 and Aislamiento_rayo_ext <= UR2_362_M2 and U_rw_externo <= UM2_362 and U_rw_interno <= UM2_362 and U_rw_interno_f_F <= UM2_362 and U_rw_externo_f_t <= UM2_362:
        print("El nivel de aislamiento normalizado escogido para tipo rayo es : ", UR2_362_M2, "El nivel de aislamiento normalizado escogido para maniobra es: ", UM2_362)
        Proteccion_rayo = UR2_362_M2
        Proteccion_maniobra = UM2_362
        
    #---------------------VALIDACIÓN NIVEL DE AISLAMIENTO NORMALIZADO DE 420KV
    elif  Aislamiento_rayo_int <= UR1_420_M1 and Aislamiento_rayo_ext <= UR1_420_M1 and U_rw_externo <= UM1_420 and U_rw_interno <= UM1_420 and U_rw_interno_f_F <= UM1_420 and U_rw_externo_f_t <= UM1_420:
        print("El nivel de aislamiento normalizado escogido para tipo rayo es : ",UR1_420_M1, "El nivel de aislamiento normalizado escogido para maniobra es: ", UM1_420)
        Proteccion_rayo = UR1_420_M1
        Proteccion_maniobra = UM1_420
    elif Aislamiento_rayo_int <= UR2_420_M1 and Aislamiento_rayo_ext <= UR2_420_M1 and U_rw_externo <= UM1_420 and U_rw_interno <= UM1_420 and U_rw_interno_f_F <= UM2_362 and U_rw_externo_f_t <= UM1_420:
        print("El nivel de aislamiento normalizado escogido para tipo rayo es : ",UR2_420_M1, "El nivel de aislamiento normalizado escogido para maniobra es: ", UM1_420)
        Proteccion_rayo = UR2_420_M1
        Proteccion_maniobra = UM1_420
        
    elif Aislamiento_rayo_int <= UR1_420_M2 and Aislamiento_rayo_ext <= UR1_420_M2 and U_rw_externo <= UM2_420 and U_rw_interno <= UM2_420 and U_rw_interno_f_F <= UM2_420 and U_rw_externo_f_t <= UM2_420:
        print("El nivel de aislamiento normalizado escogido para tipo rayo es : ",UR1_420_M2, "El nivel de aislamiento normalizado escogido para maniobra es: ", UM2_420)
        Proteccion_rayo = UR1_420_M2
        Proteccion_maniobra = UM2_420    
    elif Aislamiento_rayo_int <= UR2_420_M2 and Aislamiento_rayo_ext <= UR2_420_M2 and U_rw_externo <= UM2_420 and U_rw_interno <= UM2_420 and U_rw_interno_f_F <=  UM2_420 and U_rw_externo_f_t <=  UM2_420:
        print("El nivel de aislamiento normalizado escogido para tipo rayo es : ", UR2_420_M2, "El nivel de aislamiento normalizado escogido para maniobra es: ", UM2_420)
        Proteccion_rayo = UR2_420_M2
        Proteccion_maniobra = UM2_420    
            
    elif Aislamiento_rayo_int <= UR1_420_M3 and Aislamiento_rayo_ext <= UR1_420_M3 and U_rw_externo <= UM3_420 and U_rw_interno <= UM3_420 and U_rw_interno_f_F <=  UM3_420 and U_rw_externo_f_t <=  UM3_420:
        print("El nivel de aislamiento normalizado escogido para tipo rayo es : ", UR1_420_M3, "El nivel de aislamiento normalizado escogido para maniobra es: ", UM3_420)
        Proteccion_rayo = UR1_420_M3
        Proteccion_maniobra = UM3_420
    elif Aislamiento_rayo_int <= UR2_420_M3 and Aislamiento_rayo_ext <= UR2_420_M3 and U_rw_externo <= UM3_420 and U_rw_interno <= UM3_420 and U_rw_interno_f_F <= UM3_420 and U_rw_externo_f_t <=  UM3_420:
        print("El nivel de aislamiento normalizado escogido para tipo rayo es : ",UR2_420_M3, "El nivel de aislamiento normalizado escogido para maniobra es: ", UM3_420)
        Proteccion_rayo = UR2_420_M3
        Proteccion_maniobra = UM3_420
    #---------------------VALIDACIÓN NIVEL DE AISLAMIENTO NORMALIZADO DE 550KV
    elif Aislamiento_rayo_int <= UR1_M1 and Aislamiento_rayo_ext <= UR1_M1 and U_rw_externo <= UM1 and U_rw_interno <= UM1 and U_rw_interno_f_F <= UM1 and U_rw_externo_f_t <=  UM1:
        print("El nivel de aislamiento normalizado escogido para tipo rayo es : ",UR1_M1, "El nivel de aislamiento normalizado escogido para maniobra es: ", UM1)
        Proteccion_rayo = UR1_M1
        Proteccion_maniobra = UM1  
    elif Aislamiento_rayo_int <= UR2_M1 and Aislamiento_rayo_ext <= UR2_M1 and U_rw_externo <= UM1 and U_rw_interno <= UM1 and U_rw_interno_f_F <= UM1 and U_rw_externo_f_t <=  UM1:
        print("El nivel de aislamiento normalizado escogido para tipo rayo es : ",UR2_M1, "El nivel de aislamiento normalizado escogido para maniobra es: ", UM1)
        Proteccion_rayo = UR2_M1
        Proteccion_maniobra = UM1   
        
    elif Aislamiento_rayo_int <= UR1_M2 and Aislamiento_rayo_ext <= UR1_M2 and U_rw_externo <= UM2 and U_rw_interno <= UM2 and U_rw_interno_f_F <= UM2 and U_rw_externo_f_t <=  UM2:
        print("El nivel de aislamiento normalizado escogido para tipo rayo es : ",UR1_M2, "El nivel de aislamiento normalizado escogido para maniobra es: ", UM2)
        Proteccion_rayo = UR1_M2
        Proteccion_maniobra = UM2  
    elif Aislamiento_rayo_int <= UR2_M2 and Aislamiento_rayo_ext <= UR2_M2 and U_rw_externo <= UM2 and U_rw_interno <= UM2 and U_rw_interno_f_F <= UM2 and U_rw_externo_f_t <=  UM2:
        print("El nivel de aislamiento normalizado escogido para tipo rayo es : ",UR2_M2, "El nivel de aislamiento normalizado escogido para maniobra es: ", UM2)
        Proteccion_rayo = 0
        Proteccion_maniobra = 0   
            
    elif Aislamiento_rayo_int <= UR1_M3 and Aislamiento_rayo_ext <= UR1_M3 and U_rw_externo <= UM3 and U_rw_interno <= UM3 and U_rw_interno_f_F <= UM3 and U_rw_externo_f_t <=  UM3:
        print("El nivel de aislamiento normalizado escogido para tipo rayo es : ",UR1_M3, "El nivel de aislamiento normalizado escogido para maniobra es: ", UM3)
        Proteccion_rayo = UR1_M3
        Proteccion_maniobra = UM3
    elif Aislamiento_rayo_int <= UR2_M3 and Aislamiento_rayo_ext <= UR1_M3 and U_rw_externo <= UM3 and U_rw_interno <= UM3 and U_rw_interno_f_F <= UM3 and U_rw_externo_f_t <=  UM3:
        print("El nivel de aislamiento normalizado escogido para tipo rayo es : ",UR2_M3, "El nivel de aislamiento normalizado escogido para maniobra es: ", UM3)
        Proteccion_rayo = UR2_M3
        Proteccion_maniobra = UM3
    #---------------------VALIDACIÓN NIVEL DE AISLAMIENTO NORMALIZADO DE 800KV
    elif Aislamiento_rayo_int <= UR1_800_M1 and Aislamiento_rayo_ext <= UR1_800_M1 and U_rw_externo <= UM1_800 and U_rw_interno <= UM1_800 and U_rw_interno_f_F <= UM1_800 and U_rw_externo_f_t <=  UM1_800:
        print("El nivel de aislamiento normalizado escogido para tipo rayo es : ",UR1_800_M1, "El nivel de aislamiento normalizado escogido para maniobra es: ", UM1_800)
        Proteccion_rayo = UR1_800_M1
        Proteccion_maniobra = UM1_800   
    elif Aislamiento_rayo_int <= UR2_800_M1 and Aislamiento_rayo_ext <= UR2_800_M1 and U_rw_externo <= UM1_800 and U_rw_interno <= UM1_800 and U_rw_interno_f_F <= UM1_800 and U_rw_externo_f_t <=  UM1_800:
        print("El nivel de aislamiento normalizado escogido para tipo rayo es : ",UR2_800_M1, "El nivel de aislamiento normalizado escogido para maniobra es: ", UM1_800)
        Proteccion_rayo = UR2_800_M1
        Proteccion_maniobra = UM1_800    
    elif Aislamiento_rayo_int <= UR1_800_M2 and Aislamiento_rayo_ext <= UR1_800_M2 and U_rw_externo <= UM2_800  and U_rw_interno <= UM2_800 and U_rw_interno_f_F <= UM2_800 and U_rw_externo_f_t <=  UM2_800:
        print("El nivel de aislamiento normalizado escogido para tipo rayo es : ",UR1_800_M2, "El nivel de aislamiento normalizado escogido para maniobra es: ", UM2_800 )
        Proteccion_rayo = UR1_800_M2
        Proteccion_maniobra = UM2_800    
    elif Aislamiento_rayo_int <= UR2_800_M2 and Aislamiento_rayo_ext <= UR2_800_M2 and U_rw_externo <= UM2_800  and U_rw_interno <= UM2_800 and U_rw_interno_f_F <= UM2_800 and U_rw_externo_f_t <=  UM2_800:
        print("El nivel de aislamiento normalizado escogido para tipo rayo es : ",UR2_800_M2, "El nivel de aislamiento normalizado escogido para maniobra es: ", UM2_800 )
        Proteccion_rayo = UR2_800_M2
        Proteccion_maniobra = UM2_800        
    elif Aislamiento_rayo_int <= UR1_800_M3 and Aislamiento_rayo_ext <= UR1_800_M3 and U_rw_externo <= UM3_800 and U_rw_interno <= UM3_800 and U_rw_interno_f_F <= UM3_800 and U_rw_externo_f_t <= UM3_800:
        print("El nivel de aislamiento normalizado escogido para tipo rayo es : ",UR1_800_M3, "El nivel de aislamiento normalizado escogido para maniobra es: ", UM3_800)
        Proteccion_rayo = UR1_800_M3
        Proteccion_maniobra = UM3_800
    elif Aislamiento_rayo_int <= UR2_800_M3 and Aislamiento_rayo_ext <= UR2_800_M3 and U_rw_externo <= UM3_800 and U_rw_interno <= UM3_800 and U_rw_interno_f_F <= UM3_800 and U_rw_externo_f_t <= UM3_800:
        print("El nivel de aislamiento normalizado escogido para tipo rayo es : ",UR2_800_M3, "El nivel de aislamiento normalizado escogido para maniobra es: ", UM3_800)
        Proteccion_rayo = UR2_800_M3
        Proteccion_maniobra = UM3_800
    else:
        print("Ninguna de las condiciones se cumple")

    #--------------------TABLA DE DISTANCIAS MÍNIMAS SEGUN LA NORMA IEC 60071-1----------------

    #-------------------------------DETERMINACIÓN DE NIVEL DE DISTANCIAS MÍNIMAS DE LA SUBESTACIÓN
    if Proteccion_rayo == 850:
        print("Distancia mínima fase - fase: ", 1700, "Distancia mínima fase - tierra:", 1600)
        Dis_min_ff = 1700
        Dis_min_fe = 1600
    elif Proteccion_rayo == 950:
        print("Distancia mínima fase - fase: ", 1900, "Distancia mínima fase - tierra:", 1700)
        Dis_min_ff = 1900
        Dis_min_fe = 1700
    elif Proteccion_rayo == 1050:
        print("Distancia mínima fase - fase: ", 2100, "Distancia mínima fase - tierra:", 1900)
        Dis_min_ff = 2100
        Dis_min_fe = 1900
    elif Proteccion_rayo == 1175:
        print("Distancia mínima fase - fase: ", 2350, "Distancia mínima fase - tierra:", 2200)
        Dis_min_ff = 2350
        Dis_min_fe = 2200
    elif Proteccion_rayo == 1300:
        print("Distancia mínima fase - fase: ",2600, "Distancia mínima fase - tierra:", 2400)
        Dis_min_ff = 2600
        Dis_min_fe = 2400
    elif Proteccion_rayo == 1425:
        print("Distancia mínima fase - fase: ", 2850, "Distancia mínima fase - tierra:", 2600)
        Dis_min_ff = 2850
        Dis_min_fe = 2600
    elif Proteccion_rayo == 1550:
        print("Distancia mínima fase - fase: ", 3100, "Distancia mínima fase - tierra:", 2900)
        Dis_min_ff = 3100
        Dis_min_fe = 2900
    elif Proteccion_rayo == 1675:
        print("Distancia mínima fase - fase: ", 3350, "Distancia mínima fase - tierra:", 3100)
        Dis_min_ff = 3350
        Dis_min_fe = 3100
    elif Proteccion_rayo == 1800:
        print("Distancia mínima fase - fase: ", 3600, "Distancia mínima fase - tierra:", 3300)
        Dis_min_ff = 3600
        Dis_min_fe = 3300
    elif Proteccion_rayo == 1950:
        print("Distancia mínima fase - fase: ", 3900, "Distancia mínima fase - tierra:", 3600)
        Dis_min_ff = 3900
        Dis_min_fe = 3600
    elif Proteccion_rayo == 2100:
        print("Distancia mínima fase - fase: ", 4200, "Distancia mínima fase - tierra:", 3900)
        Dis_min_ff = 4200
        Dis_min_fe = 3900
    # Obtener los valores actuales del item "I001" 
    new_Riesgo_aislamiento=[Proteccion_rayo,Proteccion_maniobra,Dis_min_ff,Dis_min_fe]
    table.item(("I001"), values=new_Riesgo_aislamiento)  
# Establecer tamaño de fuente y espaciado
fuente = ("Arial", 12)
espaciado = 10

# Título de la ventana
ventana.title("Aplicación para la coordinación de aislamiento por el método estadístico")

# Creamos un widget Notebook (pestañas)
notebook = ttk.Notebook(ventana)
notebook.pack(fill='both', expand='yes')

# Creamos dos pestañas
tab1 = ttk.Frame(notebook)
tab2 = ttk.Frame(notebook)
tab3 = ttk.Frame(notebook)
tab4 = ttk.Frame(notebook)
tab5 = ttk.Frame(notebook)

notebook.add(tab1, text='Paso 1  Simulación Monte Carlo')
notebook.add(tab2, text='Paso 2  Sobretensiones ATP')
notebook.add(tab3, text='Paso 3  Gráficas y riesgos')
notebook.add(tab4, text='Paso 4  Resultados tipo rayo')
notebook.add(tab5, text='Paso 5  Resultados tipo maniobra')

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
# Marco principal
marco = tk.Frame(tab1)
marco.pack(pady=20)

# Submarco para las simulaciones
submarco_sim = tk.Frame(marco)
submarco_sim.pack(padx=20, pady=10)

# Elementos del submarco de simulaciones
label_sim = tk.Label(submarco_sim, text="Simulaciones:")
label_sim.grid(row=0, column=0, padx=5, pady=5)
entry_sim = tk.Entry(submarco_sim)
entry_sim.grid(row=0, column=1, padx=5, pady=5)

# Submarco para las medidas
submarco_medidas = tk.Frame(marco)
submarco_medidas.pack(padx=20, pady=10)

# Elementos del submarco de medidas
label_ancho = tk.Label(submarco_medidas, text="Ancho_Impacto:")
label_ancho.grid(row=0, column=0, padx=5, pady=5)
entry_ancho = tk.Entry(submarco_medidas)
entry_ancho.grid(row=0, column=1, padx=5, pady=5)

label_long = tk.Label(submarco_medidas, text="Longitud_línea:")
label_long.grid(row=1, column=0, padx=5, pady=5)
entry_long = tk.Entry(submarco_medidas)
entry_long.grid(row=1, column=1, padx=5, pady=5)

label_long1 = tk.Label(submarco_medidas, text="Longitud_vano1:")
label_long1.grid(row=2, column=0, padx=5, pady=5)
entry_long1 = tk.Entry(submarco_medidas)
entry_long1.grid(row=2, column=1, padx=5, pady=5)

label_long2 = tk.Label(submarco_medidas, text="Longitud_vano2:")
label_long2.grid(row=3, column=0, padx=5, pady=5)
entry_long2 = tk.Entry(submarco_medidas)
entry_long2.grid(row=3, column=1, padx=5, pady=5)

label_long3 = tk.Label(submarco_medidas, text="Longitud_vano3:")
label_long3.grid(row=4, column=0, padx=5, pady=5)
entry_long3 = tk.Entry(submarco_medidas)
entry_long3.grid(row=4, column=1, padx=5, pady=5)

label_long4 = tk.Label(submarco_medidas, text="Longitud_vano4:")
label_long4.grid(row=5, column=0, padx=5, pady=5)
entry_long4 = tk.Entry(submarco_medidas)
entry_long4.grid(row=5, column=1, padx=5, pady=5)

# Crear los cuadros de texto
Aislamiento = tk.Label(tab3, text="LIWL:")
Aislamiento.place(x=25, y=210)  # Colocar la etiqueta en la posición (50, 50)
Entry_Ais_Int = tk.Entry(tab3)
Entry_Ais_Int.place(x=25, y=260)  # Colocar la caja en la posición (250, 50)

Aislamiento_ext = tk.Label(tab3, text="LIWL:")
Aislamiento_ext.place(x=25, y=350)  # Colocar la etiqueta en la posición (50, 100)
Entry_Aislamiento_ext = tk.Entry(tab3)
Entry_Aislamiento_ext.place(x=25, y=400)  # Colocar la caja en la posición (250, 100)

Altura_mar = tk.Label(tab3, text="H [msnm]:")
Altura_mar.place(x=25, y=450)  # Colocar la etiqueta en la posición (50, 100)
Entry_Altura_mar = tk.Entry(tab3)
Entry_Altura_mar .place(x=25, y=500)  # Colocar la caja en la posición (250, 100)
# Crear el botón y asociarlo a la función
boton_simular = tk.Button(tab1, text="Simular", command=simular)
boton_simular.pack()
label = tk.Label(tab2, text="Ingrese el número de gráficas que desea (1-4):")
label.pack(pady=10)
entry = tk.Entry(tab2)
entry.pack(pady=5)
submit_button = tk.Button(tab2, text="Aceptar", command=get_num_graphs)
submit_button.pack(pady=5)
error_label = tk.Label(tab2, fg="red")
error_label.pack(pady=5)
# Crear botón en la pestaña "tab3"
button_Histograma = tk.Button(tab3, text='Ejecutar histograma', command=ejecutar_histograma)
button_Histograma.place(x=25, y=60)
button_Weiubull = tk.Button(tab3, text='Ejecutar Weibull', command=ejecutar_Weibull)
button_Weiubull.place(x=30, y=110)
button_Aisl_Int = tk.Button(tab3, text='Aislamiento Interno', command=Aislamiento_Interno)
button_Aisl_Int.place(x=25, y=160)
button_Aisl_Ext = tk.Button(tab3, text='Aislamiento Externo', command=Aislamiento_Externo)
button_Aisl_Ext.place(x=25, y=300)
button_Tipo_maniobra = tk.Button(tab5, text='Representativas maniobra Fase pico', command=Representativas_Fase_pico)
button_Tipo_maniobra.place(x=550, y=50)
button_Tipo_maniobra = tk.Button(tab5, text='Representativas maniobra Caso pico ', command=Representativas_Caso_pico)
button_Tipo_maniobra.place(x=550, y=100)
button_Tipo_maniobra = tk.Button(tab5, text='Determinar nivel de aislamiento y distancias mínimas', command=Distancias_mínimas)
button_Tipo_maniobra.place(x=500, y=150)
# ------------------------------ Crear widgets en la pestaña 4 "tab4"------------------
two = ttk.Treeview(tab4, style="Custom.Treeview")

# Define el estilo personalizado
style = ttk.Style()
style.configure("Custom.Treeview", padding=(20, 5), borderwidth=2)
style.configure("Custom.Treeview.Heading", padding=(15, 15))
style.configure("Custom.Treeview.Cell", padding=(15, 10))  # Agrega padding a las celdas

# Configura las columnas de la tabla
two["columns"] = ("one", "two")
two.heading("one", text="Aislamiento interno")
two.heading("two", text="Aislamiento externo")

# Configura el ancho y la alineación de las columnas
two.column("one", width=100, anchor="center")
two.column("two", width=100, anchor="center")

# Agrega filas a la tabla
two.insert("", 0, text="Riesgo (%)", values=(Riesgo_int, Riesgo_ext))
two.insert("", 1, text="Confiabilidad (%) ", values=(Confiabilidad_int, Confiabilidad_ext))
two.insert("", 2, text="NDSU", values=(NDSU_int, NDSU_ext))
two.insert("", 3, text="Años", values=(Años_int, Años_ext))
two.insert("", 4, text="Fallas por año por descargas en línea", values=(TFIL_int , TFIL_ext))
two.insert("", 5, text="Tasas de falla total para la subestación", values=(T_total_int, T_total_ext))

# Asigna el estilo personalizado a las filas y celdas
two.tag_configure("Custom.Treeview.Cell", font=("Helvetica", 11), background="white")
two.tag_configure("Custom.Treeview", background="#F6F6F6", font=("Helvetica", 12))

# Agrega la tabla a la ventana principal
two.pack(padx=10, pady=10, fill="both", expand=True)
item_names = [two.item(item)["text"] for item in two.get_children()]
for item in two.get_children():
    print(item)
print(two.item("I001")["text"])
style.configure("Custom.Treeview.Heading", font=("Arial", 18))
style.configure("Custom.Treeview", font=("Arial", 14), rowheight=40)
#-----------------------------Tabla de resultados coordinación de aislamiento y distancias mínimas
# Crear un nuevo estilo y establecer la fuente
style = ttk.Style()
style.configure("Custom.Treeview", font=('Arial', 14))

# Crear el objeto Treeview y aplicar el nuevo estilo
table = ttk.Treeview(tab5, columns=('col1', 'col2', 'col3', 'col4'), show='headings', style="Custom.Treeview")

# Agregar encabezados de columna
table.heading('col1', text='Ais. Impulso maniobra')
table.heading('col2', text='Ais. Impulso rayo')
table.heading('col3', text='Dis. mínima (f - f)')
table.heading('col4', text='Dis. mínima (f - e)')
# Ancho de columna
table.column('col1', width=220, anchor="center")
table.column('col2', width=160, anchor="center")
table.column('col3', width=160, anchor="center")
table.column('col4', width=170, anchor="center")
# Agregar filas
table.insert('', 'end', values=(Proteccion_maniobra, Proteccion_rayo, Distancia_min_ff, Distancia_min_fe))

# Mostrar la tabla
table.pack()
# Muestra la tabla en la ventana
table.place(relx=0.1, rely=0.5, relwidth=0.8, relheight=0.3)
item_names = [table.item(item)["text"] for item in table.get_children()]
for item in table.get_children():
    print(item)
print(table.item("I001")["text"])
# Muestra la tabla en la ventana
two.place(relx=0.5, rely=0.5, relwidth=0.75, relheight=0.75, anchor="center")
# ------------------------------ Crear widgets en la pestaña 5 "tab5"------------------

# Correr la ventana
ventana.mainloop()