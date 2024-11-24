# EconomicModel
Resolución de un modelo económico de ingresos y gastos basado en ecuaciones diferenciales ordinarias (EDO) utilizando métodos numéricos.

Descripción general
Este repositorio contiene la resolución de un modelo económico de ingresos y gastos basado en Ecuaciones Diferenciales Ordinarias (EDO). El modelo utiliza métodos numéricos como el método de Euler, Runge-Kutta y otros para resolver el sistema de ecuaciones y analizar el comportamiento de la economía en el tiempo.

Objetivo
El objetivo principal es simular y analizar la evolución dinámica de los ingresos y gastos de una economía, utilizando métodos numéricos para aproximar soluciones a ecuaciones diferenciales ordinarias que describan el comportamiento del sistema. El proyecto se centra en comprender cómo evolucionan los ingresos y gastos en función de diferentes parámetros (K, C, G0) a lo largo de un periodo de tiempo determinado.

Características principales
*Métodos numéricos : Implementaciones del método de Euler y Runge-Kutta para resolver EDO.
*Análisis de modelos : estudia la relación entre ingresos, gastos y parámetros.
*Análisis de errores : cálculo de errores locales para cada método para evaluar la precisión de las soluciones.
*Visualización : Representación gráfica de los ingresos y gastos a lo largo del tiempo, así como el error asociado a cada método.

Requisitos
*Python 3.11.5
*Bibliotecas: 
	*numpy
	*pyplot
	*pandas
	*solve_ivp
	*plotly

Instalación

Para comenzar a utilizar este repositorio, primero clone el repositorio en su máquina local:
git clone https://github.com/TattySanagua/EconomicModel.git

Luego, navegue hasta el directorio del proyecto:
cd EconomicModel

Instale las bibliotecas de Python necesarias (si aún no las tiene)
pip install biblioteca


Uso
1. Ejecutar la simulación: tiene 3 scripts disponibles 
	*"fixed-step method.py": método de paso fijo implementado con EULER explícito.
	*"variable-step method.py": método de paso variable implementado con RK23 (puede probar con otros métodos de la librería solve_ivp).
	*"parallel diagram.py": diagrama de coordenadas paralelas para ver la combinación de parámetros.
2. Modificar parámetros: puede ajustar los parámetros K, C y G0 para explorar como los diferentes valores afectan el comportamiento de los ingresos y gastos.
3. Analizar resultados: los resultados se muestran tanto en gráficos como en archivos excel.

Integrantes del proyecto:
*Juan Ignacio Ruiz
*María Tatiana Sanagua

Materia: Métodos Numéricos II (Licenciatura en Informática) - Computación Científica (Ingeniería en Informática)

Año: 2024