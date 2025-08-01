import pandas as pd
import numpy as np
import matplotlib.pyplot as plt # Hacer graficos
import seaborn as sns # Hacer graficos
from IPython.display import display


# leer el dataset
df = pd.read_csv("./04_obligatoria_market/market.csv")
print("\ntamaño de dataframe",df.shape)

print("-----------------------------------------------------------------------------------------")
print("----------------------------- Exploración inicial del dataset ---------------------------")
print("-----------------------------------------------------------------------------------------")

display(df)


print("\n----------------------------- INFO -----------------------------\n")

print(df.info())

# print("\n----------------------------- DESCRIBE -----------------------------")
# # print(df.describe(include='all'))
# print(df.describe())

print("\n-----------------------------------------------------------------------------------------")
print("--------------------------------- Nombres de las columnas -------------------------------")
print("-----------------------------------------------------------------------------------------\n")

print(df.loc[0])
# print(df.columns)
columnas = df.columns.tolist()
# print(columnas)

nombres_nuevos = [
    "ID_producto", "peso_producto", "contenido_grasa", "visibilidad", "categoria",
    "precio_maximo", "ID_tienda", "anio_apertura_tienda", "tamanio_tienda",
    "tipo_ciudad_tienda", "tipo_tienda", "ventas_producto"
]

print("\n-----------------------------------------------------------------------------------------")
print("---------------------------------- Renombrado columnas ----------------------------------")
print("-----------------------------------------------------------------------------------------\n")

df.columns = nombres_nuevos

print(df.loc[0])

# display(df)

# print("\n----------------------------- DESCRIBE -----------------------------")
# # print(df.describe(include='all'))
# print(df.shape)


print("\n------------------------------------------------------------------------------------------")
print("-------------------------- Convertir columnas numéricas a arrays -------------------------")
print("------------------------------------------------------------------------------------------")

# Convertir columnas numéricas a arrays
peso_productos = df["peso_producto"].to_numpy()
ventas = df["ventas_producto"].to_numpy()
precios = df["precio_maximo"].to_numpy()
visibilidad = df["visibilidad"].to_numpy()

# Mostrar dimensiones y tipos
print("Pesos: ", peso_productos.shape, peso_productos.dtype)
print("Ventas: ", ventas.shape, ventas.dtype)
print("Precios: ", precios.shape, precios.dtype)
print("visibilidad: ", visibilidad.shape, visibilidad.dtype)


print("\n-------------------------------------------------------------------------------------------")
print("------------------------------ Estadisticas basicas con NumPy -----------------------------")
print("-------------------------------------------------------------------------------------------")

print("Peso promedio:", np.nanmean(peso_productos))
print("Desvío estándar de ventas:", np.std(ventas))
print("Precio máximo:", np.max(precios))
print("Visibilidad mínima:", np.min(visibilidad))

print("\n-------------------------------------------------------------------------------------------")
print("----------------------------- Filtrado de datos con condiciones ---------------------------")
print("-------------------------------------------------------------------------------------------")

# Productos con peso mayor a 15 kg
pesados = peso_productos[peso_productos > 15]
print("Productos con peso > 15kg:", pesados.shape[0])

# Ventas mayores a la media
media_ventas = np.mean(ventas) 
ventas_altas = ventas[ventas > media_ventas] # ventas  mayoes a la media
print("Ventas por encima del promedio:", ventas_altas.shape[0])


print("\n-------------------------------------------------------------------------------------------")
print("--------------------------------- Operaciones Vectorizadas --------------------------------")
print("-------------------------------------------------------------------------------------------")


# Precio por kilo estimado
precio_x_kg = precios / peso_productos
print("Precio por kilo (primeros 5):", precio_x_kg[:5])


print("\n-------------------------------------------------------------------------------------------")
print("--------------------------------- Algebra Matricial con NumPy --------------------------------")
print("-------------------------------------------------------------------------------------------")



# Crear matriz de dos variables
matriz = np.vstack((precios[:5], ventas[:5]))  # 2x100  2x5
print("\nMatriz de 2x5:\n-------------------\n", matriz)
matriz_t = matriz.T  # 100x2
print("\nMatriz de 5x2:\n-------------------\n", matriz_t)

# Producto matricial (covarianza básica)
producto = matriz @ matriz_t  # 2x5 * 5x2 = 2x2
print("\nProducto matricial 2x2:\n------------------------\n", producto)  # producto

'''
## 🧠 Desafíos propuestos
💡 Tip: ¡Usá funciones como `np.isnan`, `np.round`, `np.corrcoef`, `np.nanmean`, `np.unique`!
'''

'''
1. Calcular la mediana del peso de los productos usando NumPy.
'''

print("----------------------------------------------------\n")
print("\nMediana del peso de los productos: " , np.nanmedian(peso_productos))
print("----------------------------------------------------\n")

'''
2. ¿Cuál es el valor más frecuente (moda) de `Item_Weight`? --> peso_productos
'''

print("\nEl valor mas frecuente o Moda de peso_productos es " , df["peso_producto"].mode()[0])
print("----------------------------------------------------\n")

'''
3. Filtrar los productos que tengan un precio mayor a $250 y visibilidad menor al 0.02.
'''

productos_mayor_precio = precios[precios > 250]
productos_menor_visibilidad = visibilidad[visibilidad < 0.02]

print("\nCantidad Productos con un precio mayor a $250: ", productos_mayor_precio.shape[0]  )
print("-------------------------------------------------\n")
print(productos_mayor_precio[:10],"\n", productos_mayor_precio.shape,"\n", productos_mayor_precio.dtype)

print("\nCantidad de Productos con visibilidad menor al 0.02: ", productos_menor_visibilidad.shape[0]  )
print("-------------------------------------------------\n")
print(productos_menor_visibilidad[:10],"\n", productos_menor_visibilidad.shape,"\n", productos_menor_visibilidad.dtype)


productos_filtrados =  precios[(precios > 250)&(visibilidad < 0.02)]
print("\nCantidad de Productos con precio mayor a $250 & visibilidad menor al 0.02: ", productos_filtrados.shape[0] )
print("-------------------------------------------------------------------\n")


print(productos_filtrados,"\n", productos_filtrados.shape,"\n", productos_filtrados.dtype)


'''
4. Crear un array que contenga la diferencia entre el precio y las ventas para los primeros 500 productos.
'''
print("\n-------------------------------------------------------------------------------------------")

print("\nPrecios: " )
print("--------------\n")
print( precios[0:4], "\n", precios[0:].shape, "\n", precios[0:].dtype)


print("\nVentas: " )
print("--------------\n")
print(ventas[0:4], "\n", ventas[0:].shape,"\n", ventas[0:].dtype)

diferencia_precio_ventas = precios[0:500] - ventas[0:500]

print("\nDiferencia entre precio y ventas para los primeros 500 productos:" )
print("-----------------------------------------------------------------\n")

display(diferencia_precio_ventas)
print("\nCantidad de elementos sumandos: ", diferencia_precio_ventas.shape[0],"\n", diferencia_precio_ventas.dtype)

'''
5. Normalizar los valores de visibilidad entre 0 y 1.
'''



'''
6. Crear una matriz de 3 columnas: peso, precio y ventas, y calcular su media por columna.
'''
peso_productos = df["peso_producto"]
precios = df["precio_maximo"]
ventas = df["ventas_producto"]

matriz = np.column_stack((peso_productos.round(1), precios.round(1), ventas.round(1))) 
print("\nMatriz de 3 columnas: peso_productos, precios, ventas\n------------------------------------------------------\n")

display(matriz)
print("\n",matriz.shape, matriz.dtype)


print("\nMedia por columnas:" )
print("------------------------------------------------------\n")

print("Media de Pesos Productos: ", np.nanmean(peso_productos).round(2))
print("Media de Precioss: ", np.nanmean(precios).round(2))
print("Media de Ventas: ", np.nanmean(ventas).round(2))


'''
7. ¿Qué productos tienen un valor de peso faltante (`NaN`)? ¿Cuántos hay?
'''

'''
8. Simular 100 precios aleatorios con `np.random.normal()` con media 200 y desvío 30.
'''

'''
9. Calcular la correlación entre precios y ventas (usando `np.corrcoef`).
'''


'''
10. Guardar un nuevo array con los precios redondeados a 2 decimales.
'''




