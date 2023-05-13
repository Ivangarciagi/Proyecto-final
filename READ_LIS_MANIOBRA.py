ruta_archivo = 'C:\ATP\work\ENL_BOCMAR_SRP.lis'
Mean = []
Standard_deviation = []

#------------------------------CÁLCULO DE VALOR DE FASE - TIERRA----------------------------------------------------

with open(ruta_archivo, "r") as f:
    for line in f:
        if "Statistical distribution of peak voltage at node" in line:
            print(line)
            for linea in f:
                # Comprobar si la línea contiene el valor específico que buscas
                if 'Standard deviation' in linea:
                    partes = linea.split()
                    Des_lis = float(partes[3])   # Extraer el valor de x de la cuarta parte y convertirlo a un float
                    Standard_deviation.append(Des_lis)   # Agregar el valor de x a la lista de valores
                    # Realizar la acción deseada si se encuentra el valor
                    print(linea)
                    break
print(Standard_deviation)
max_Upt = []
for Sigma_f_e in Standard_deviation:
    #-------------------VALOR REPRESENTATIVO FASE - TIERA
    Ue2 = (Sigma_f_e)/0.25+1
    Uet = 1.25*Ue2-0.25
    max_Upt.append(Uet)

print("Valor máximo fase - tierra", max(max_Upt))

#------------------------------CÁLCULO DE VALOR DE FASE - FASE----------------------------------------------------

Standard_deviation_f_f = []
with open(ruta_archivo, "r") as f:
    for line in f:
        if "Statistical distribution of peak voltage  for branch" in line:
            print(line)
            for linea in f:
                # Comprobar si la línea contiene el valor específico que buscas
                if 'Standard deviation' in linea:
                    partes_ff = linea.split()
                    Des_lis_ff = float(partes_ff[3])   # Extraer el valor de x de la cuarta parte y convertirlo a un float
                    Standard_deviation_f_f.append(Des_lis_ff)   # Agregar el valor de x a la lista de valores
                    # Realizar la acción deseada si se encuentra el valor
                    print(linea)
                    break
print(Standard_deviation_f_f)
max_Upt_f = []
for Sigma_f_f in Standard_deviation_f_f:
    #-------------------VALOR REPRESENTATIVO FASE - FASE
    Up2 = (Sigma_f_f)/0.25+1.73
    Upt = 1.25*Up2-0.43
    max_Upt_f.append(Upt)
    

print("Valor máximo fase - fase",max(max_Upt_f))