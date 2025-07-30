import pandas as pd # Manejar datos
import matplotlib.pyplot as plt # Hacer graficos
import seaborn as sns # Hacer graficos

# Cargar datos
df = pd.read_csv("./03_refugio_animales_austin/aac_shelter_cat_outcome_eng.csv")

# Mostrar las primeras 5 filas
print(df.head())
# Mostrar las últimas 5 filas
print(df.tail())

print("-----------------------------------------------------------------------------------------")
print("----------------------------- Exploración inicial del dataset ---------------------------")
print("-----------------------------------------------------------------------------------------")

print("\n----------------------------- INFO -----------------------------")
# Mostrar columnas, tipos de datos y nulos
print(df.info())

print("\n----------------------------- DESCRIBE -----------------------------")
# Mostrar estadísticas generales (valores únicos, más frecuentes, etc)
print(df.describe(include='all'))


print("------------------------------------------------------------------------------------------")
print("--------------------------------- Limpieza Basica de Datos -------------------------------")
print("------------------------------------------------------------------------------------------")

# Eliminar columnas poco útiles como "Unnamed: 0", si las hubiera (ej: las del indice del CSV)
df = df.drop(columns=["Unnamed: 0"], errors="ignore")
print(df.describe(include='all'))

# Renombrar columnas para mayor claridad
df = df.rename(columns={
    "animal_id": "ID",
    "name": "Nombre",
    "date_of_birth": "FechaNacimiento",
    "outcome_type": "TipoResultado",
    "outcome_subtype": "SubtipoResultado",
    "animal_type": "TipoAnimal",
    "sex_upon_outcome": "Sexo",
    "age_upon_outcome": "Edad",
    "breed": "Raza",
    "color": "Color"
})

print(df.describe(include='all'))

print("------------------------------------------------------------------------------------------")
print("------------------------ Distribucion de resultados de los animales ----------------------")
print("------------------------------------------------------------------------------------------")
# Crea una figura nueva de tamaño 10x5 pulgadas
plt.figure(figsize=(10,5))
# Crea un grafico de barras con Seaborn (Countplot)
sns.countplot(
   data=df, # usa el DataFrame
   x='TipoResultado', # Eje X = tipo de resultado (Adoption, Died, etc)
   order=df['TipoResultado'].value_counts().index, # Organiza las barras por frecuencia (de mayor a menor)
   palette='viridis' # Elige colores de la paleta de colores
   )
# Titulo del grafico
plt.title("Distribución de resultados")
# Nombre del eje y
plt.ylabel("Cantidad")
# Rotacion 45° de las etiquetas del eje x
plt.xticks(rotation=45)
# Ajusta márgenes automaticamente
plt.tight_layout()
# Muestra el grafico en pantalla
plt.show()

print("-----------------------------------------------------------------------------------------")
print("---------------- ¿Qué tipo de animales se registran con mayor frecuencia? ---------------")
print("-----------------------------------------------------------------------------------------")

# Muestra la cantidad de anumales por tipo (ej: Dog, Cat), utiliza otra paleta (set2)
sns.countplot(data=df, x='TipoAnimal', palette='Set2')
# Titulo del gráfico, nombre del eje Y, ajustar márgenes automaticamente y mostrar grafico
plt.title("Distribución por tipo de animal")
plt.ylabel("Cantidad")
plt.tight_layout()
plt.show()


print("-----------------------------------------------------------------------------------------")
print("-------------------- Relación entre el sexo y el resultado del animal -------------------")
print("-----------------------------------------------------------------------------------------")
# Crear una tabla cruzada: mostrar la distribución porcentual de los resultados por sexo
pd.crosstab(
   df['Sexo'], 
   df['TipoResultado'], 
   normalize='index').plot(kind='barh', stacked=True, colormap='Accent')
# Normalize='index' convierte los valores en proporciones (entre 0 y 1) por cada fila (sexo)
#.plot(kind='barh', stacked=True, colormap='Accent') Muestra el resultado como grafico de barras horizontales apiladas
# Cada barra representa un sexo
# Los colores indican el tipo de resultado (adoptados, fallecidos, etc)

# Titulo del gráfico, nombre del eje X, ajustar márgenes automaticamente y mostrar grafico
plt.title("Proporción de resultados por sexo")
plt.xlabel("Proporción")
plt.tight_layout()
plt.show()


print("-----------------------------------------------------------------------------------------")
print("---------------- ¿Qué edades tienen los animales al momento del resultado? --------------")
print("-----------------------------------------------------------------------------------------")

df['Edad'].value_counts().head(10).plot(kind='bar', color='coral')
# Titulo del gráfico, nombre del eje Y
plt.title("Edades más comunes al momento del resultado")
plt.ylabel("Cantidad")
# Rotacion 45° de las etiquetas del eje x
plt.xticks(rotation=45)
# Ajustar márgenes automaticamente y mostrar grafico
plt.tight_layout()
plt.show()

'''
## 🧪 Actividades prácticas y desafíos
> 💡 ¡Podés utilizar todas las herramientas de pandas que practicamos: filtros, agrupaciones, gráficos, funciones lambda, creación de columnas nuevas y más!
'''


'''
1. **Filtrar por especie:** Mostrá sólo los registros correspondientes a gatos (`Cat`). ¿Cuántos hay en total?
'''
# Filtrar solo las filas donde el tipo de animal sea a "Cat" y las guarda en df_gatos
df_gatos = df[df["TipoAnimal"] == "Cat"]
# Mostrar cantidad de registros
print("El total de los gatos es de", len(df_gatos))


'''
2. **Top razas:** ¿Cuáles son las 5 razas más comunes en el dataset? Representalo en un gráfico de barras.
'''
# Contar cuántas veces aparece cada raza y mostrar las 5 razas más comunes
df_razas = df["Raza"].value_counts().head(5)
# Imprimir el conteo de esas 5 razas
print(df_razas)

# Hacer grafico de barras 
df_razas.plot(kind='bar', color='coral') # df_razas.plot.bar(color='coral')
# Titulo del gráfico
plt.title("5 razas más comunes")
# Nombre del eje Y
plt.ylabel("Cantidad")
# Rotacion 45° de las etiquetas del eje x
plt.xticks(rotation=45)
# Ajustar márgenes automaticamente y mostrar gráfico
plt.tight_layout()
plt.show()

'''
3. **Animales con nombre:** ¿Qué proporción de animales tiene nombre? Representalo con un gráfico de torta.
'''
# Contar cuámtos gatos tienen nombre, norna() devuelve True si el valor de la columna nombre NO está vacío, los cuenta con sum()
#  genera una serie de booleanos: True si el nombre NO es nulo, False si está vacío.
con_nombre = df_gatos["Nombre"].notna().sum()
# Contar cuántos gatos no tienen nombre, isna() devuelve True si el valor de la columna Nombre está vacío, los cuenta con sum()
sin_nombre = df_gatos["Nombre"].isna().sum()

print(f"Gatos con nombre: {con_nombre}")
print(f"Gatos sin nombre: {sin_nombre}")

# Crea una figura nueva de tamaño 6x6 pulgadas
plt.figure(figsize=(6, 6))
# Crea un grafico de torta (pie) con 
plt.pie([con_nombre, sin_nombre], # los datos a mostrar
        labels=["Con nombre", "Sin nombre"], # etiquetas para cada porción
        autopct="%1.1f%%", # muestra el porcentaje con 1 decimal.
        startangle=90, # empieza el gráfico desde arriba.
        colors=["lightseagreen", "lightgray"]) # colores personalizados
# Titulo del grafico
plt.title("Proporción de gatos con nombre")
# hacer el gráfico circular (si no, puede verse ovalado).
plt.axis("equal")
# Mostrar grafico
plt.show()

'''
4. **Resultados por raza dominante:** Analizá si hay razas que tienen mayores tasas de adopción. Filtrá las 10 razas más frecuentes y compará los resultados.
'''
# Cuenta cuántas veces aparece cada raza. Toma las 10 más comunes con .head(10) .index.tolist() transforma esos nombres de raza en una lista de strings
top10Razas = df['Raza'].value_counts().head(10).index.tolist()
#  Filtra el DataFrame con las filas donde la raza esté en topRazas y .isin(lista) compara cada valor con la lista.
dfTop10Razas = df[df['Raza'].isin(top10Razas)]
# El value_counts normalize true devuelve las proporciones
# .unstack() convierte resultados en columnas
# .fillna(0) rellena valores faltantes con 0
proporciones = dfTop10Razas.groupby('Raza')['TipoResultado'].value_counts(normalize=True).unstack().fillna(0)

# Extrae la columna "Adoption" (proporción de adopciones por raza). Ordena de mayor a menor.
proporcionPorRaza = proporciones['Adoption'].sort_values(ascending=False)
print("Proporción de adopciones por las 10 razas más frecuentes:", proporcionPorRaza)

proporciones.head(10)

'''
5. **Edad más común:** ¿Cuál es la edad al momento del resultado más frecuente para los animales adoptados?
'''
# df[df['TipoResultado'] == 'Adoption'] filtra solo los animales adoptados
# ['Edad'] accede a la columna de edad
#.mode() calcula la edad más frecuente.
# .tolist() convierte el resultado en una lista.
print(f"La edad más común al momento de adopcion es:",  df[df['TipoResultado'] == 'Adoption']['Edad'].mode().tolist())


'''
6. **Nombres más comunes:** ¿Cuáles son los 10 nombres de animales más comunes en el dataset?
'''
# Contar los nombres más frecuentes. Mostrar los 10 primeros.
top10Nombres= df['Nombre'].value_counts().head(10)
print("Los 10 nombres más comunes son:")
print(top10Nombres)

'''
7. **Cruza o no cruza:** Agregá una nueva columna que indique si el animal es de raza pura o mestizo, en base a la columna de raza (`Raza`).
'''

# Si 'domestic' aparece en la columna raza, retorna 'mestizo'. Sino retorna 'Raza pura'.
def cruza_nocruza(raza):
    if 'domestic' in raza :
      return 'mestizo'
    else:
        return 'Raza pura'
    
# Aplica la función cruza_nocruza() a cada fila de la columna "Raza" usando .apply().
#  El resultado se guarda en una nueva columna llamada "tipo" (con valores 'mestizo' o 'Raza pura').
df['tipo']=df['Raza'].apply(cruza_nocruza)
df.head(11)

'''
8 Tendencia de adopciones: Convertí la columna de fecha de nacimiento a datetime y tratá de analizar si hay alguna relación entre el año de nacimiento y la probabilidad de adopción.
'''
# Convierte la columna "FechaNacimiento" a formato de fecha (datetime).
# Si algún valor es inválido, lo reemplaza por NaT (Not a Time) gracias a errors='coerce'.
df['FechaNacimiento'] = pd.to_datetime(df['FechaNacimiento'], errors='coerce')

#Extrae solo el año de cada fecha de nacimiento y lo guarda en una nueva columna "año_nacimiento".
df['año_nacimiento'] = df['FechaNacimiento'].dt.year

# Agrupa los datos por "año_nacimiento" y cuenta cuántos animales nacieron en cada año
total_por_año = df.groupby('año_nacimiento').size()

# Filtra solo los animales que fueron adoptados, y de ellos, cuenta cuántos nacieron cada año.
adoptados_por_año = df[df['TipoResultado'] == 'Adoption'].groupby('año_nacimiento').size()

#  Calcula el porcentaje de animales adoptados por año: (adoptados / nacidos ese año) * 100
# .dropna() elimina años con datos faltantes.
# Calculamos el porcentaje de adopción adoptados por año dividido el total de adoptados por año y lo transformamos en porcentaje ignorando nulos
porcentaje_adopcion = (adoptados_por_año / total_por_año * 100).dropna()

# Graficar
plt.figure(figsize=(12, 6))
# Crea un gráfico de línea: marker='o': marca cada punto con un círculo.color='orange': color de línea.
porcentaje_adopcion.plot(marker='o', color='orange')
plt.title("Tasa de adopción según año de nacimiento")
plt.xlabel("Año de nacimiento")
plt.ylabel("Probabilidad de adopción (%)")
plt.grid(True)
plt.tight_layout()
plt.show()

# Calcula la correlación estadística entre: el año de nacimiento (x) y la tasa de adopción (y)
# Valor cerca de 1: positiva - a mayor año, más adopciones (animales más jóvenes = más adoptados).
# Valor cerca de 0: sin relación.

correlacion = porcentaje_adopcion.index.to_series().corr(porcentaje_adopcion)
print(f"La relacion entre el año de nacimiento y las adopciones son de: {correlacion:.3f}")
##Basicamente los animales nacidos en años más recientes tienen mayor posibilidad de ser adoptados, la tendencia es que se adoptan más animales "jovenes"

'''
9. **Relación entre edad y resultado:** Explorá si existe una diferencia en el tipo de resultado según la edad del animal.

'''
# Asegura que ambas columnas estén en formato de fecha.
df['datetime'] = pd.to_datetime(df['datetime'], errors='coerce')
df['FechaNacimiento'] = pd.to_datetime(df['FechaNacimiento'], errors='coerce')

##Calculamos la edad al mmomento del resultado
# Calcula la edad al momento del resultado (adopción, transferencia, etc.) en años: Resta fechas y divide los días entre 365.
df['edad_al_resultado'] = ((df['datetime'] - df['FechaNacimiento']).dt.days // 365)

##Agrupamos por edad y por tipo de resultado
tabla = df.groupby(['edad_al_resultado', 'TipoResultado']).size().unstack(fill_value=0)

##Limitamos la edad a 15 años para que se entienda el grafico
tabla = tabla[tabla.index <= 15]

tabla.plot(kind='bar', stacked=True, figsize=(14, 7), colormap='tab10')
plt.title("Diferencia en el tipo de resultado según la edad del animal")
plt.xlabel("Edad del animal (años)")
plt.ylabel("Cantidad de animales")
plt.xticks(rotation=0)
plt.legend(title="Tipo de Resultado")
plt.tight_layout()
plt.grid(True)
plt.show()

'''
10. **Exportar datos filtrados:** Filtrá los animales que fueron adoptados y guardalos en un nuevo archivo CSV llamado `adoptados.csv`.
'''
# adoptados = df[df["TipoResultado"] == "Adoption"]
# adoptados.to_csv("./03_refugio_animales_austin/adoptados.csv", index=False)

df_clean_resultados = df[df['TipoResultado'].notna()]
adoptados =df_clean_resultados[df_clean_resultados['TipoResultado'] == 'Adoption']
adoptados.to_csv('./03_refugio_animales_austin/adoptados.csv', index=False)

print("Archivo 'adoptados.csv' creado con éxito.")