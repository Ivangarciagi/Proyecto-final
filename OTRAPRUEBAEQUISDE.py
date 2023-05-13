import numpy as np
import scipy.stats as stats
import matplotlib.pyplot as plt
from scipy.stats import weibull_min
# Generar datos aleatorios
media = 700
desviacion_estandar = 1
num_datos = 8000
datos = np.random.normal(media, desviacion_estandar, num_datos)

# Ajustar la distribución Weibull
shape, loc, scale = stats.weibull_min.fit(datos, floc=0)

# Crear la distribución Weibull
dist_weibull = stats.weibull_min(shape, loc=loc, scale=scale)

# Calcular la función de densidad de probabilidad de la distribución Weibull
x = np.linspace(stats.weibull_min.ppf(0.01, shape, loc=loc, scale=scale),
                stats.weibull_min.ppf(0.99, shape, loc=loc, scale=scale), 8000)
pdf = dist_weibull.pdf(x)

# Crear histograma
hist, bins = np.histogram(datos, bins=10)

# Calcular los valores medios de cada bin del histograma
x_hist = (bins[:-1] + bins[1:]) / 2

# Interpolar la distribución Weibull en los puntos medios de cada bin
pdf_interp = np.interp(x_hist, x, pdf)

# Calcular el coeficiente de correlación de Pearson y el valor p
r, p = stats.pearsonr(hist, pdf_interp)

# Obtener la media y la desviación estándar de la distribución ajustada
media_ajustada = weibull_min.mean(shape ,loc=loc, scale=scale)
desv_std_ajustada = weibull_min.std(shape, loc=loc, scale=scale)

# Comparar la media y la desviación estándar de la distribución ajustada con los valores de la lista de sobretensiones
media_real = np.mean(datos)
desv_std_real = np.std(datos)

print("Media real:", media_real)
print("Media ajustada:", media_ajustada)
print("Desviación estándar real:", desv_std_real)
print("Desviación estándar ajustada:", desv_std_ajustada)
# Mostrar los resultados
print(f"Coeficiente de correlación de Pearson: {r}")
print(f"Valor p: {p}")

# Graficar el histograma y la distribución Weibull ajustada
fig, ax = plt.subplots()
plt.text(0.01, 0.95, 'Índice de coreclacción = {:.2f}'.format(r), transform=plt.gca().transAxes,
         fontsize=9, verticalalignment='top')
plt.text(0.01, 0.85, 'Media R.= {:.2f}'.format(media_real), transform=plt.gca().transAxes,
         fontsize=9, verticalalignment='top')
plt.text(0.01, 0.8, 'Media A.= {:.2f}'.format(media_ajustada), transform=plt.gca().transAxes,
         fontsize=9, verticalalignment='top')
plt.text(0.01, 0.75, 'Desviación estándar R.= {:.2f}'.format(desv_std_real), transform=plt.gca().transAxes,
         fontsize=9, verticalalignment='top')
plt.text(0.01, 0.7, 'Desviación estándar A.= {:.2f}'.format(desv_std_ajustada), transform=plt.gca().transAxes,
         fontsize=9, verticalalignment='top')

ax.hist(datos, bins=10, alpha=0.5, density=True)
ax.plot(x, pdf, 'r-', lw=2, label='Weibull')
plt.legend()
plt.show()