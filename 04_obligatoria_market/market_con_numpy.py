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

print("\n-----------------------------------------------------------------------------------------")
print("--------------------------------- Renombrado de columnas --------------------------------")
print("-----------------------------------------------------------------------------------------")

# print(df.loc[0])
# print(df.columns)
columnas = df.columns.tolist()
print(columnas)

nombres_nuevos = [
    "ID_producto", "peso_producto", "contenido_grasa", "visibilidad", "categoria",
    "precio_maximo", "ID_tienda", "anio_apertura_tienda", "tamanio_tienda",
    "tipo_ciudad_tienda", "tipo_tienda", "ventas_producto"
]

df.columns = nombres_nuevos

print("\n----------------------------- DESCRIBE -----------------------------")
print(df.describe(include='all'))




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
print("\nMediana del peso de los productos: " , np.median(peso_productos), "-  sin-nan: ", np.nanmedian(peso_productos))
print("----------------------------------------------------\n")
# print("-  sin-nan: ", np.isnan(peso_productos).value_counts())
# print("-  total: ", peso_productos.shape)
# print("-  nan media: ", np.nanmean(peso_productos).shape)
# print("-  media ",np.mean(peso_productos).shape)


print("----------------------------------------------------\n")
# print("Mediana del peso de los productos::", np.median(peso_productos))

'''
2. ¿Cuál es el valor más frecuente (moda) de `Item_Weight`? --> peso_productos
'''
# print("El valor mas frecuente o Moda es: ", np.unique(peso_productos, return_counts=True))

print("\nEl valor mas frecuente o Moda es: " , np.unique(peso_productos, return_counts=True) )
print("----------------------------------------------------\n")



'''
3. Filtrar los productos que tengan un precio mayor a $250 y visibilidad menor al 0.02.
'''


productos_mayor_precio = precios[precios > 250]
productos_menor_visibilidad = visibilidad[visibilidad < 0.02]

print("\nProductos con un precio mayor a $250:\n" )
print("-------------------------------------------------\n")
print(productos_mayor_precio,"\n", productos_mayor_precio.shape,"\n", productos_mayor_precio.dtype)

print("\nProductos con visibilidad menor al 0.02:\n" )
print("-------------------------------------------------\n")
print(productos_menor_visibilidad,"\n", productos_menor_visibilidad.shape,"\n", productos_menor_visibilidad.dtype)


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

'''si voy a sumar 2 listas, las listas deben tener la  misma cantidad de elementos'''

print("\nDiferencia entre precio y ventas para los primeros 500 productos:" )
print("-----------------------------------------------------------------\n")
print(diferencia_precio_ventas,"\n", diferencia_precio_ventas.shape,"\n", diferencia_precio_ventas.dtype)



'''
5. Normalizar los valores de visibilidad entre 0 y 1.
'''



'''
6. Crear una matriz de 3 columnas: peso, precio y ventas, y calcular su media por columna.
'''

matriz = np.column_stack((peso_productos, precios, ventas))
# matriz = np.column_stack((['peso_productos'], ['precios'], ['ventas']))
print("\nMatriz de 3 columnas: peso_productos, precios, ventas\n------------------------------------------------------\n", matriz[:])


print("\nMedia por columnas: peso_productos, precios, ventas\n------------------------------------------------------\n")
print("Media Peso Productos: ", (np.nanmean(matriz, axis=0)))    



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




