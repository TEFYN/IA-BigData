import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns



# Configuración estética
plt.style.use('ggplot')
sns.set(font_scale=1.1)

# Cargar el dataset
df = pd.read_csv("./05_estadistica_descriptiva_y/CAR DETAILS FROM CAR DEKHO.csv")

# Mostrar las primeras filas
print(df.head(5))

print("----------------------------------------Medidas de tendencia central-------------------------------------------------")

# Dimensiones
print("Filas y columnas:", df.shape)

# Nombres de columnas
print("Columnas:", df.columns)

# Tipos de datos
print(df.info())

# Estadísticas básicas
print(df.describe())


print("----------------------------------------Medidas de tendencia central-------------------------------------------------")
# Precio de venta
print("Media precio:", df['selling_price'].mean())
print("Mediana precio:", df['selling_price'].median())
print("Moda precio:", df['selling_price'].mode()[0])

# Kilometraje
print("Media km:", df['km_driven'].mean())
print("Mediana km:", df['km_driven'].median())
print("Moda km:", df['km_driven'].mode()[0])


print("----------------------------------------Medidas de dispersion -------------------------------------------------")

# Rango
print("Rango precio:", df['selling_price'].max() - df['selling_price'].min())

# Varianza y desviación estándar
print("Varianza precio:", df['selling_price'].var())
print("Desviación estándar precio:", df['selling_price'].std())

print("Varianza km:", df['km_driven'].var())
print("Desviación estándar km:", df['km_driven'].std())

print("----------------------------------------Visualizacion de variables numericas -------------------------------------------------")

# Histograma de precios
plt.figure(figsize=(8,5))
sns.histplot(df['selling_price'], bins=30, kde=True)
plt.title('Distribución del Precio de Venta')
plt.xlabel('Precio (INR)')
plt.ylabel('Cantidad de autos')
plt.show()

# Boxplot para detectar outliers
plt.figure(figsize=(8,5))
sns.boxplot(x=df['selling_price'])
plt.title('Boxplot del Precio de Venta')
plt.show()

# Histograma del kilometraje
plt.figure(figsize=(8,5))
sns.histplot(df['km_driven'], bins=30, kde=True)
plt.title('Distribución del Kilometraje')
plt.xlabel('Km recorridos')
plt.show()

print("---------------------------------------- Relacion entre variables -------------------------------------------------")



# Precio vs Año
plt.figure(figsize=(8,6))
sns.scatterplot(data=df, x='year', y='selling_price', hue='fuel')
plt.title('Precio vs Año del Vehículo')
plt.show()

# Correlación numérica
df[['selling_price', 'year', 'km_driven']].corr()

'''
## ✅ Actividades Prácticas

1. ¿Cuál es el promedio de autos listados por año? Graficá la cantidad de autos por año.
2. Calculá la media, mediana y moda del `year` (año del vehículo).
3. Realizá un boxplot del kilometraje recorrido (`km_driven`) para detectar outliers.
4. Calculá el rango, varianza y desviación estándar del `year`.
5. Hacé un histograma del `selling_price` para autos que usan combustible "Diesel".
6. Graficá la distribución de autos por tipo de transmisión (`manual` vs `automatic`).
7. ¿Cuál es la relación entre el tipo de combustible (`fuel`) y el precio promedio de venta?
8. Usando un `groupby`, obtené el precio medio por año de fabricación.
9. Mostrá en un gráfico de barras cuántos autos pertenecen a cada número de dueños (`owner`).
10. Calculá las medidas de dispersión para el precio de autos automáticos únicamente.
'''