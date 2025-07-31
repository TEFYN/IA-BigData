import pandas as pd
import numpy as np
import matplotlib.pyplot as plt # Hacer graficos
import seaborn as sns # Hacer graficos


# leer el dataset
df = pd.read_csv("./04_obligatoria_market/market.csv")
print("\ntamaño de dataframe",df.shape)

print("-----------------------------------------------------------------------------------------")
print("----------------------------- Exploración inicial del dataset ---------------------------")
print("-----------------------------------------------------------------------------------------")

print("\n----------------------------- INFO -----------------------------")
print(df.info())

print("\n----------------------------- DESCRIBE -----------------------------")
# print(df.describe(include='all'))
print(df.describe())

print("------------------------------------------------------------------------------------------")
print("--------------------------------- Renombrado de columnas --------------------------------")
print("------------------------------------------------------------------------------------------")

# print(df.loc[0])
# print(df.columns)
columnas = df.columns.tolist()
print(columnas)

nombres_nuevos = [
    "ID_Producto", "peso", "contenido_grasa", "visibilidad", "tipo",
    "precio_maximo", "ID_tienda", "anio_apertura", "tamanio_tienda",
    "ubicacion", "tipo_tienda", "ventas"
]

df.columns = nombres_nuevos

print("\n----------------------------- DESCRIBE -----------------------------")
print(df.describe(include='all'))
