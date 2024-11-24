"""
===========================
#Runge-Kutta 23
===========================
"""

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from scipy.integrate import solve_ivp
import time

# Definimos las constantes
K = 4
C = 2  # Cambiamos a C = 1 para otro análisis
G0 = 4

#Condiciones iniciales
I0 = 15  # Ingreso inicial
S0 = 5   # Tasa de gastos inicial
t_span = (0, 10)  # Tiempo de simulación (0 a 10 unidades)

# Puntos donde evaluaremos la solución, lo utilizamos en caso de que necesitemos
#  evaluar más o menos puntos de los que genera el método automáticamente.
t_eval = np.linspace(0, 10, 100)

# Definimos el sistema de EDOs
def sistema(t, y):
    I, S = y
    dI_dt = I - K * S
    dS_dt = I - C * S - G0
    return [dI_dt, dS_dt]

start_time = time.time()

# Resolvemos el sistema usando Runge-Kutta 23 (solve_ivp)
# Se puede probar con otros métodos de la librería solve_ivp como RK45, DOP853, Radau, BDF y LSODA
sol = solve_ivp(sistema, t_span, [I0, S0], method='RK23') #Aquí se puede utilizar "t_eval"

end_time = time.time()

print(f"Tiempo de ejecución del método: {end_time - start_time} segundos")

# Extraemos las soluciones
t = sol.t
I = sol.y[0]
S = sol.y[1]

#Cálculo de ERRORES
#Error Local I
error_local_I = np.zeros_like(I)
error_local_I[1:] = np.abs(I[1:]-I[:-1])

#Error Local S
error_local_S = np.zeros_like(S)
error_local_S[1:] = np.abs(S[1:]-S[:-1])

#Norma infinita
error_local_norma_infinita = np.maximum(error_local_I, error_local_S)

# Calculamos las derivadas dI/dt y dS/dt
dI_dt = I - K * S
dS_dt = I - C * S - G0

# Creamos un DataFrame para almacenar los resultados
df = pd.DataFrame({
    "Tiempo (t)": t,
    "Ingreso (I)": I,
    "Tasa de Gastos (S)": S,
    "dI/dt": dI_dt,
    "dS/dt": dS_dt,
    "Error Local I": error_local_I,
    "Error Local S": error_local_S,
    "Error Local (Norma Infinita)": error_local_norma_infinita
})

# Mostramos la tabla
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

#Plots de errores locales
fig, axs = plt.subplots(1, 3, figsize=(15, 3))

axs[0].plot(t, error_local_I, 'b-o', label="Error local I", markersize=1)
axs[0].set_xlabel('t')
axs[0].set_ylabel('Error')
axs[0].set_title('Error local I')
axs[0].legend()
axs[0].grid(True)

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
#output_excel = "resultados_simulacion_rk23.xlsx"
#df.to_excel(output_excel, index=False)  # index=False elimina la columna de índices