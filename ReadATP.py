import matplotlib.pyplot as plt

def graficar_variables_de_salida(nombre_archivo, palabra_clave, opcion):
    valores = []   # Crear una lista vacía para almacenar los valores máximos de x, y, z
    CONTL=[]
    with open(nombre_archivo, "r") as archivo:
        CONT=0
        for linea in archivo:
            if palabra_clave in str(linea):
                CONT=CONT+1
                partes = linea.split()   # Dividir la línea en varias partes utilizando el espacio como separador
                if len(partes) >= 6:
                    if opcion == 1:
                        x = float(partes[3])   # Extraer el valor de x de la cuarta parte y convertirlo a un float
                        valores.append(x)   # Agregar el valor de x a la lista de valores
                        y = 0
                        z = 0
                        valor_maximo = max(x,y,z)   # Encontrar el valor máximo entre x y z
                    elif opcion == 2:
                        x = float(partes[3])   # Extraer el valor de x de la cuarta parte y convertirlo a un float
                        y = float(partes[4])   # Extraer el valor de y de la quinta parte y convertirlo a un float
                        z = 0
                        valor_maximo = max(x, y,z)   # Encontrar el valor máximo entre x y z   
                        valores.append(valor_maximo)   # Agregar una tupla con los valores de x e y a la lista de valores
                    elif opcion == 3:
                        
                        x = float(partes[3])   # Extraer el valor de x de la cuarta parte y convertirlo a un float
                        y = float(partes[4])   # Extraer el valor de y de la quinta parte y convertirlo a un float
                        z = float(partes[5])   # Extraer el valor de z de la sexta parte y convertirlo a un float
                        valor_maximo = max(x, z, y)   # Encontrar el valor máximo entre x y z
                        valores.append(valor_maximo)   # Agregar una tupla con los valores de x, y, y z a la lista de valores
                    CONTL.append(CONT)
    return (CONTL,valores)
##resultado = graficar_variables_de_salida(nombre_archivo, palabra_clave, Numero_fases)
##x=resultado[0]
##y=resultado[1]
##print(y)
# Obtener la dimensión del vector
##dimension = x
##print(y)
##print(x)
##plt.plot(x, y,label="Torre 4")   # Agregar una etiqueta para identificar el archivo
##plt.legend()   # Mostrar la leyenda en la gráfica
##plt.xlabel('Corriente [kA]')
##plt.ylabel('Valor máximo de tension vs corriente de descarga')
##plt.title('Tensión máxima de salida')
##plt.show()