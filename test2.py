import numpy as np
import matplotlib.pyplot as plt

lower_bound = -32.768
upper_bound = 32.768

# Cantidad de valores
size = 50
# Parámetros de la primera campana gaussiana
mu_1, sigma_1 = lower_bound/2, abs(lower_bound/4+1)
size_1 = size//2  # Dividimos n en dos para generar la mitad de valores en cada campana

# Parámetros de la segunda campana gaussiana
mu_2, sigma_2 = upper_bound/2, (upper_bound/4+1)
size_2 = size-size_1 # La otra mitad de valores

# Generar valores aleatorios para cada campana
cells_1 = np.random.normal(loc=mu_1, scale=sigma_1, size=size_1)
cells_2 = np.random.normal(loc=mu_2, scale=sigma_2, size=size_2)

# Combinar ambas campanas en un solo vector
cells = np.concatenate((cells_1, cells_2))

cells[cells < lower_bound] = lower_bound
cells[cells > upper_bound] = upper_bound

print(cells)

# Graficar las campanas gaussianas
plt.hist(cells, bins=30, density=True, alpha=0.6, color='b')
plt.xlabel('Valores Aleatorios')
plt.ylabel('Frecuencia')
plt.title('Sample gauss s')
plt.grid(True)
plt.show()
