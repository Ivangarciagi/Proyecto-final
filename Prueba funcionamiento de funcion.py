from ReadATP import graficar_variables_de_salida
import matplotlib.pyplot as plt

# Definimos los parámetros de entrada
nombre_archivo = "C:\\ATP\\work\\Prueba final tipo rayo Copia 01.lis"
palabra_clave = "Variable maxima :"
Numero_fases = 2
# Llamamos a la función y guardamos el resultado en una variable
resultado  = graficar_variables_de_salida(nombre_archivo, palabra_clave, Numero_fases)
Corriente_descarga=resultado[0]
Sobretensión_generada=resultado[1]
plt.plot(Corriente_descarga, Sobretensión_generada,label= "Torre 4")
plt.legend()   # Mostrar la leyenda en la gráfica
plt.xlabel('Corriente [kA]')
plt.ylabel('Valor máximo de tension vs corriente de descarga')
plt.title('Tensión máxima de salida')
plt.show()