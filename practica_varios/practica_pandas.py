import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

'''Lectria de CSV'''
df = pd.read_csv("./03_refugio_animales_austin/aac_shelter_cat_outcome_eng.csv")

'''Visuzlizar datos'''
print("-------------- Primeras 5 filas del DataFrame\n",df.head(), "\n\n")

print("-------------- Ultimas 10 filas del DataFrame\n",df.tail(10), "\n\n")

print("-------------- Nombres de todas las columnas del DataFrame.\n",df.columns, "\n\n")

print("-------------- Dimension del dataframe(filas, columnas)",df.shape, "\n\n")

print("-------------- Informacion del dataframe (indice, el tipo de datos y las columnas, los valores no nulos y el uso de memoria)\n",df.info(), "\n\n")

print("--------------Muestra estadísticas por columna: (Para columnas numéricas: promedio, máximo, mínimo, etc., Para texto: cuántos valores únicos, el valor más común (frecuente), \n",df.describe(include='all'), "\n\n")

print("--------------cuenta valores faltantes (NaN) por columna. Si mayor a 0, significa que hay datos perdidos\n",df.isna().sum(), "\n\n")

print("--------------detecta si hay filas duplicadas completas (todas las columnas iguales). El .sum() indica cuántas hay\n",df.duplicated().sum(), "\n\n")

print("--------------¿Cuántas veces se repite el mismo animal_id?\n",df.duplicated(subset=['animal_id']).sum(), "\n\n")

print("-------------- ¿Cuántos animales tienen el mismo nombre? (¡pueden llamarse igual pero ser distintos!)\n",df.duplicated(subset=['name']).sum(), "\n\n")

print("-------------- ¿Cuántos animales tienen la misma fecha de nacimiento?\n",df.duplicated(subset=['date_of_birth']).sum(), "\n\n")

print(df.duplicated(subset=['outcome_type']).sum(), "\n\n")

print(df.duplicated(subset=['outcome_subtype']).sum(), "\n\n")

print(df.duplicated(subset=['animal_type']).sum(), "\n\n")

print(df.duplicated(subset=['sex_upon_outcome']).sum(), "\n\n")

print(df.duplicated(subset=['age_upon_outcome']).sum(), "\n\n")

print(df.duplicated(subset=['breed']).sum(), "\n\n")

print(df.duplicated(subset=['color']).sum(), "\n\n")





'''✅   ¿Qué hacer con datos duplicados?'''
# 🔸 1. Ver duplicados completos (toda la fila igual)
df[df.duplicated()]


'''🔸 2. Eliminar duplicados completos'''
df = df.drop_duplicates()
print(df)

# 🔸 3. Ver duplicados por una columna (ej: ID repetido)
df[df.duplicated(subset=["ID"])]

# 🔸 4. Eliminar duplicados por una columna, dejando solo el primero
df = df.drop_duplicates(subset=["ID"], keep="first")

# 🔸 5. O eliminar, dejando el último
df = df.drop_duplicates(subset=["ID"], keep="last")

# 🔸 6. O eliminar todos los duplicados (no se queda con ninguno)
df = df[~df.duplicated(subset=["ID"], keep=False)]

'''✅ ¿Qué hacer con datos faltantes? (NaN, None, Null)'''
# 🔸 1. Ver si hay valores faltantes por columna
df.isna().sum()

# 🔸 2. Eliminar filas que tengan algún valor faltante
df = df.dropna()

# 🔸 3. Eliminar filas solo si falta un dato en una columna específica
df = df.dropna(subset=["ID"])

# 🔸 4. Rellenar valores faltantes con un texto o número
df["Edad"] = df["Edad"].fillna("Desconocido")
df["ID"] = df["ID"].fillna("SIN-ID")


''' ✅ ¿Cómo filtrar solo lo que sirve?'''
# 🔸 1. Filtrar filas que no tienen NaN en columna ID
df = df[df["ID"].notna()]


# 🔸 2. Filtrar filas donde ID no esté duplicado
df = df[~df["ID"].duplicated(keep=False)]

# 🔸 3. Combinar filtros: solo animales con ID válido, sin duplicados
df = df[df["ID"].notna()]
df = df.drop_duplicates(subset=["ID"])

# ✅ Resumen práctico: limpieza paso a paso

import pandas as pd

# Cargar datos
df = pd.read_csv("animales.csv")

# Renombrar columnas (opcional, si lo necesitás)
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

# 1. Eliminar filas con ID vacío
df = df[df["ID"].notna()]

# 2. Eliminar filas duplicadas por ID (te quedás con la primera)
df = df.drop_duplicates(subset=["ID"], keep="first")

# 3. Eliminar filas que tienen datos faltantes en otras columnas clave
df = df.dropna(subset=["Nombre", "FechaNacimiento", "TipoResultado"])

# 4. (opcional) Eliminar duplicados completos
df = df.drop_duplicates()

# Ver cómo quedó
print(df.info())
print(df.head())


# ✅ ¿Querés ver solo los datos "útiles"?
# Podés mostrar solo los datos que cumplen con tus condiciones:

# Ejemplo: mostrar solo los gatos adoptados con nombre no vacío
filtro = (df["TipoAnimal"] == "Cat") & (df["TipoResultado"] == "Adoption") & (df["Nombre"].notna())
df_filtrado = df[filtro]

print(df_filtrado.head())



# Visualizar datos
# sns.pairplot(df)
# plt.show()df.info()

# print("-----------------------------------------------------------------------------------------")
# print("----------------------------- Exploración inicial del dataset ---------------------------")
# print("-----------------------------------------------------------------------------------------")

# print("\n----------------------------- INFO -----------------------------")
# print(df.info())

# print("\n----------------------------- DESCRIBE -----------------------------")
# print(df.describe(include='all'))


# print("------------------------------------------------------------------------------------------")
# print("--------------------------------- Limpieza Basica de Datos -------------------------------")
# print("------------------------------------------------------------------------------------------")
# print(df.describe(include='all'))
# # Eliminar columnas poco informativas si las hubiera
# df = df.drop(columns=["Unnamed: 0"], errors="ignore")
# print(df.describe(include='all'))

# # Renombramos columnas para mayor claridad
# df = df.rename(columns={
#     "animal_id": "ID",
#     "name": "Nombre",
#     "date_of_birth": "FechaNacimiento",
#     "outcome_type": "TipoResultado",
#     "outcome_subtype": "SubtipoResultado",
#     "animal_type": "TipoAnimal",
#     "sex_upon_outcome": "Sexo",
#     "age_upon_outcome": "Edad",
#     "breed": "Raza",
#     "color": "Color"
# })

# print(df.describe(include='all'))

# print(df.head())
# print(df.tail())

# print("------------------------------------------------------------------------------------------")
# print("------------------------ Distribucion de resultados de los animales ----------------------")
# print("------------------------------------------------------------------------------------------")

# plt.figure(figsize=(10,5))
# sns.countplot(data=df, x='TipoResultado', order=df['TipoResultado'].value_counts().index, palette='viridis')
# plt.title("Distribución de resultados")
# plt.ylabel("Cantidad")
# plt.xticks(rotation=45)
# plt.tight_layout()
# plt.show()

# print("-----------------------------------------------------------------------------------------")
# print("---------------- ¿Qué tipo de animales se registran con mayor frecuencia? ---------------")
# print("-----------------------------------------------------------------------------------------")

# sns.countplot(data=df, x='TipoAnimal', palette='Set2')
# plt.title("Distribución por tipo de animal")
# plt.ylabel("Cantidad")
# plt.tight_layout()
# plt.show()


# print("-----------------------------------------------------------------------------------------")
# print("-------------------- Relación entre el sexo y el resultado del animal -------------------")
# print("-----------------------------------------------------------------------------------------")

# pd.crosstab(df['Sexo'], df['TipoResultado'], normalize='index').plot(kind='barh', stacked=True, colormap='Accent')
# plt.title("Proporción de resultados por sexo")
# plt.xlabel("Proporción")
# plt.tight_layout()
# plt.show()


# print("-----------------------------------------------------------------------------------------")
# print("---------------- ¿Qué edades tienen los animales al momento del resultado? --------------")
# print("-----------------------------------------------------------------------------------------")

# df['Edad'].value_counts().head(10).plot(kind='bar', color='coral')
# plt.title("Edades más comunes al momento del resultado")
# plt.ylabel("Cantidad")
# plt.xticks(rotation=45)
# plt.tight_layout()
# plt.show()

# '''
# ## 🧪 Actividades prácticas y desafíos
# > 💡 ¡Podés utilizar todas las herramientas de pandas que practicamos: filtros, agrupaciones, gráficos, funciones lambda, creación de columnas nuevas y más!
# '''


# '''
# 1. **Filtrar por especie:** Mostrá sólo los registros correspondientes a gatos (`Cat`). ¿Cuántos hay en total?
# '''
# df_gatos = df[df["TipoAnimal"] == "Cat"]
# print("El total de los gatos es de", len(df_gatos))


# '''
# 2. **Top razas:** ¿Cuáles son las 5 razas más comunes en el dataset? Representalo en un gráfico de barras.
# '''
# df_razas = df["Raza"].value_counts().head(5)
# print(df_razas)
# df_razas.plot(kind='bar', color='coral')
# plt.title("5 razas más comunes")
# plt.ylabel("Cantidad")
# plt.xticks(rotation=45)
# plt.tight_layout()
# plt.show()

# '''
# 3. **Animales con nombre:** ¿Qué proporción de animales tiene nombre? Representalo con un gráfico de torta.
# '''
# con_nombre = df_gatos["Nombre"].notna().sum()
# sin_nombre = df_gatos["Nombre"].isna().sum()

# print(f"Gatos con nombre: {con_nombre}")
# print(f"Gatos sin nombre: {sin_nombre}")

# plt.figure(figsize=(6, 6))
# plt.pie([con_nombre, sin_nombre],
#         labels=["Con nombre", "Sin nombre"],
#         autopct="%1.1f%%",
#         startangle=90,
#         colors=["lightseagreen", "lightgray"])
# plt.title("Proporción de gatos con nombre")
# plt.axis("equal")
# plt.show()


# '''
# 4. **Resultados por raza dominante:** Analizá si hay razas que tienen mayores tasas de adopción. Filtrá las 10 razas más frecuentes y compará los resultados.
# '''
# top10Razas = df['Raza'].value_counts().head(10).index.tolist()
# dfTop10Razas = df[df['Raza'].isin(top10Razas)]
# #El value_counts normalize true devuelve las proporciones
# proporciones = dfTop10Razas.groupby('Raza')['TipoResultado'].value_counts(normalize=True).unstack().fillna(0)
# proporcionPorRaza = proporciones['Adoption'].sort_values(ascending=False)
# print("Proporción de adopciones por las 10 razas más frecuentes:", proporcionPorRaza)

# proporciones.head(10)
# #dfTop10Razas.head(10)

# '''
# 5. **Edad más común:** ¿Cuál es la edad al momento del resultado más frecuente para los animales adoptados?
# '''
# print(f"La edad más común al momento de adopcion es:",  df[df['TipoResultado'] == 'Adoption']['Edad'].mode().tolist())


# '''
# 6. **Nombres más comunes:** ¿Cuáles son los 10 nombres de animales más comunes en el dataset?
# '''
# top10Nombres= df['Nombre'].value_counts().head(10)
# print("Los 10 nombres más comunes son:")
# print(top10Nombres)

# '''
# 7. **Cruza o no cruza:** Agregá una nueva columna que indique si el animal es de raza pura o mestizo, en base a la columna de raza (`Raza`).
# '''

# def cruza_nocruza(raza):
#     if 'domestic' in raza :
#       return 'mestizo'
#     else:
#         return 'Raza pura'
# df['tipo']=df['Raza'].apply(cruza_nocruza)
# df.head(11)

# '''
# 8 Tendencia de adopciones: Convertí la columna de fecha de nacimiento a datetime y tratá de analizar si hay alguna relación entre el año de nacimiento y la probabilidad de adopción.
# '''
# df['FechaNacimiento'] = pd.to_datetime(df['FechaNacimiento'], errors='coerce')

# # Creamos una columna año de nacimiento
# df['año_nacimiento'] = df['FechaNacimiento'].dt.year

# # Contamos cuántos animales nacieron por año
# total_por_año = df.groupby('año_nacimiento').size()

# # Contamos el total de cuántos de esos fueron adoptados
# adoptados_por_año = df[df['TipoResultado'] == 'Adoption'].groupby('año_nacimiento').size()

# # Calculamos el porcentaje de adopción adoptados por año dividido el total de adoptados por año y lo transformamos en porcentaje ignorando nulos
# porcentaje_adopcion = (adoptados_por_año / total_por_año * 100).dropna()

# # Graficar
# plt.figure(figsize=(12, 6))
# porcentaje_adopcion.plot(marker='o', color='orange')
# plt.title("Tasa de adopción según año de nacimiento")
# plt.xlabel("Año de nacimiento")
# plt.ylabel("Probabilidad de adopción (%)")
# plt.grid(True)
# plt.tight_layout()
# plt.show()
# correlacion = porcentaje_adopcion.index.to_series().corr(porcentaje_adopcion)
# print(f"La relacion entre el año de nacimiento y las adopciones son de: {correlacion:.3f}")
# ##Basicamente los animales nacidos en años más recientes tienen mayor posibilidad de ser adoptados, la tendencia es que se adoptan más animales "jovenes"

# '''
# 9. **Relación entre edad y resultado:** Explorá si existe una diferencia en el tipo de resultado según la edad del animal.

# '''
# df['datetime'] = pd.to_datetime(df['datetime'], errors='coerce')
# df['FechaNacimiento'] = pd.to_datetime(df['FechaNacimiento'], errors='coerce')

# ##Calculamos la edad al mmomento del resultado
# df['edad_al_resultado'] = ((df['datetime'] - df['FechaNacimiento']).dt.days // 365)

# ##Agrupamos por edad y por tipo de resultado
# tabla = df.groupby(['edad_al_resultado', 'TipoResultado']).size().unstack(fill_value=0)

# ##Limitamos la edad a 15 años para que se entienda el grafico
# tabla = tabla[tabla.index <= 15]

# tabla.plot(kind='bar', stacked=True, figsize=(14, 7), colormap='tab10')
# plt.title("Diferencia en el tipo de resultado según la edad del animal")
# plt.xlabel("Edad del animal (años)")
# plt.ylabel("Cantidad de animales")
# plt.xticks(rotation=0)
# plt.legend(title="Tipo de Resultado")
# plt.tight_layout()
# plt.grid(True)
# plt.show()

# '''
# 10. **Exportar datos filtrados:** Filtrá los animales que fueron adoptados y guardalos en un nuevo archivo CSV llamado `adoptados.csv`.
# '''
# # adoptados = df[df["TipoResultado"] == "Adoption"]
# # adoptados.to_csv("./03_refugio_animales_austin/adoptados.csv", index=False)

# df_clean_resultados = df[df['TipoResultado'].notna()]
# adoptados =df_clean_resultados[df_clean_resultados['TipoResultado'] == 'Adoption']
# adoptados.to_csv('./03_refugio_animales_austin/adoptados.csv', index=False)

# print("Archivo 'adoptados.csv' creado con éxito.")