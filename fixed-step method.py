"""
===================================
#EULER (Runge-Kutta 1)
===================================
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import time

# Definimos las constantes
K = 4
C = 2
G0 = 4
I0 = 15
S0 = 5

# Definimos las funciones que representan las ecuaciones diferenciales
def dI_dt(I, S, K):
    return I - K * S

def dS_dt(I, S, C, G0):
    return I - C * S - G0

# Parámetros de simulación
dt = 0.1  # Tamaño del paso de tiempo (primero se probó con un paso grande dt = 0.5)
t_max = 10  # Tiempo máximo de simulación

# Inicializamos los vectores para almacenar los resultados
t = np.arange(0, t_max + dt, dt)
I = np.zeros_like(t)
S = np.zeros_like(t)
dI_values = [0]  # Incluir el valor inicial de la derivada
dS_values = [0]  # Incluir el valor inicial de la derivada

# Condiciones iniciales
I[0] = I0
S[0] = S0

start_time = time.time()

# Método de Euler
for i in range(1, len(t)):
    # Calcular derivadas
    dI = dI_dt(I[i - 1], S[i - 1], K)
    dS = dS_dt(I[i - 1], S[i - 1], C, G0)

    # Almacenar las derivadas
    dI_values.append(dI)
    dS_values.append(dS)

    # Actualizar las variables
    I[i] = I[i - 1] + dt * dI
    S[i] = S[i - 1] + dt * dS

end_time = time.time()

print(f"Tiempo de ejecución: {end_time - start_time} segundos")

#Error Local I
error_local_I = np.zeros_like(I)
error_local_I[1:] = np.abs(I[1:]-I[:-1])

#Error Local S
error_local_S = np.zeros_like(S)
error_local_S[1:] = np.abs(S[1:]-S[:-1])

#Norma infinita
error_local_norma_infinita = np.maximum(error_local_I, error_local_S)

# Creamos un DataFrame con los resultados
data = {
    "Tiempo": t,
    "Ingreso (I)": I,
    "Gastos (S)": S,
    "dI/dt": dI_values,
    "dS/dt": dS_values,
    "Error Local I": error_local_I,
    "Error Local S": error_local_S,
    "Error Local (Norma Infinita)": error_local_norma_infinita
}

df = pd.DataFrame(data)

# Mostramos el DataFrame
print(df)

# Plots de los resultados
plt.figure(figsize=(10, 5))
plt.plot(t, I, label="Ingreso (I)")
plt.plot(t, S, label="Tasa de Gastos (S)")
plt.axhline(G0, color='red', linestyle='--', label="G0")
plt.title("Evolución de la Economía del Gobierno")
plt.xlabel("Tiempo")
plt.ylabel("Valores")
plt.legend()
plt.grid()
plt.show()

#Plots
fig, axs = plt.subplots(1, 3, figsize=(15, 3))

axs[0].plot(t, error_local_I, 'b-o', label="Error local I", markersize=1)
axs[0].set_xlabel('t')
axs[0].set_ylabel('Error')
axs[0].set_title('Error local I')
axs[0].legend()
axs[0].grid(True)

#Plots de errores
axs[1].plot(t, error_local_S, 'r-o', label="Error Local S", markersize=1)
axs[1].set_xlabel("t")
axs[1].set_ylabel("Error")
axs[1].set_title("Error local S")
axs[1].legend()
axs[1].grid(True)

axs[2].plot(t, error_local_norma_infinita, 'g-o', label="Error Local", markersize=1)
axs[2].set_xlabel("t")
axs[2].set_ylabel("Error")
axs[2].set_title("Error local (norma infinita)")
axs[2].legend()
axs[2].grid(True)

plt.tight_layout()
plt.show()

#Exportamos los resultados a un archivo Excel si es necesario
#output_excel = "resultados_simulacion_euler.xlsx"
#df.to_excel(output_excel, index=False)  # index=False elimina la columna de índices