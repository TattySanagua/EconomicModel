"""
==========================
#Parallel Diagram
==========================

"""

import numpy as np
import pandas as pd
from scipy.integrate import solve_ivp
import plotly.graph_objects as go

# Definimos la función del modelo económico
def modelo_economia(t, y, K, C, G0):
    I, S = y
    dI_dt = I - K * S
    dS_dt = I - C * S - G0
    return [dI_dt, dS_dt]

# Definimos la función para resolver el sistema con el método RK23
# En este caso consideramos t=10 cuando las curvas se estabilizan y tienden a un valor constante,
# pero se puede probar para distintos instantes de tiempo
def resolver_modelo(K, C, G0, I0=15, S0=5, t_final=10):
    #t_eval = np.linspace(0, t_final, 100)
    sol = solve_ivp(
        modelo_economia, [0, t_final], [I0, S0], args=(K, C, G0), method='RK23'
    )
    I, S = sol.y
    return I[-1], S[-1]  # Retornamos solo los valores finales para t=10

# Generamos combinaciones de parámetros, se consideró un rango de valores de 0 a 10
# que creemos mas representativo
K_values = np.linspace(1, 5, 5)
C_values = np.linspace(1, 5, 5)
G0_values = np.linspace(1, 5, 5)

# Creamos el DataFrame con los resultados
data = []
for K in K_values:
    for C in C_values:
        for G0 in G0_values:
            I_final, S_final = resolver_modelo(K, C, G0)
            data.append({
                'K': K,
                'C': C,
                'G0': G0,
                'Ingreso': I_final,
                'Gasto': S_final
            })

df = pd.DataFrame(data)
print(df)

# Plots para ingresos
fig_ingresos = go.Figure(data=go.Parcoords(
    line=dict(color=df['Ingreso'], colorscale='Viridis', showscale=True),
    dimensions=[
        dict(label='K', values=df['K']),
        dict(label='C', values=df['C']),
        dict(label='G0', values=df['G0']),
        dict(label='Ingreso', values=df['Ingreso'])
    ]
))
fig_ingresos.update_layout(title="Modelo Económico: Análisis de Parámetros en Ingresos")
fig_ingresos.show()

# Plots para gastos
fig_gastos = go.Figure(data=go.Parcoords(
    line=dict(color=df['Gasto'], colorscale='Viridis', showscale=True),
    dimensions=[
        dict(label='K', values=df['K']),
        dict(label='C', values=df['C']),
        dict(label='G0', values=df['G0']),
        dict(label='Gasto', values=df['Gasto'])
    ]
))
fig_gastos.update_layout(title="Modelo Económico: Análisis de Parámetros en Gastos")
fig_gastos.show()

#Exportamos los resultados a un archivo Excel si es necesario
#output_excel = "resultados_parallel_diagram.xlsx"
#df.to_excel(output_excel, index=False)  # index=False elimina la columna de índices