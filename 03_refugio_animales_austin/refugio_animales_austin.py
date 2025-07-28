import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Cargar datos
df = pd.read_csv("./03_refugio_animales_austin/aac_shelter_cat_outcome_eng.csv")
print(df.head())

# Visualizar datos
# sns.pairplot(df)
# plt.show()df.info()

print("-----------------------------------------------------------------------------------------")
print("----------------------------- Exploración inicial del dataset ---------------------------")
print("-----------------------------------------------------------------------------------------")

print("\n----------------------------- INFO -----------------------------")
print(df.info())

print("\n----------------------------- DESCRIBE -----------------------------")
print(df.describe(include='all'))


print("------------------------------------------------------------------------------------------")
print("--------------------------------- Limpieza Basica de Datos -------------------------------")
print("------------------------------------------------------------------------------------------")
print(df.describe(include='all'))
# Eliminar columnas poco informativas si las hubiera
df = df.drop(columns=["Unnamed: 0"], errors="ignore")
print(df.describe(include='all'))

# Renombramos columnas para mayor claridad
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

print(df.head())
print(df.tail())

print("------------------------------------------------------------------------------------------")
print("------------------------ Distribucion de resultados de los animales ----------------------")
print("------------------------------------------------------------------------------------------")

plt.figure(figsize=(10,5))
sns.countplot(data=df, x='TipoResultado', order=df['TipoResultado'].value_counts().index, palette='viridis')
plt.title("Distribución de resultados")
plt.ylabel("Cantidad")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

print("-----------------------------------------------------------------------------------------")
print("---------------- ¿Qué tipo de animales se registran con mayor frecuencia? ---------------")
print("-----------------------------------------------------------------------------------------")

sns.countplot(data=df, x='TipoAnimal', palette='Set2')
plt.title("Distribución por tipo de animal")
plt.ylabel("Cantidad")
plt.tight_layout()
plt.show()


print("-----------------------------------------------------------------------------------------")
print("-------------------- Relación entre el sexo y el resultado del animal -------------------")
print("-----------------------------------------------------------------------------------------")

pd.crosstab(df['Sexo'], df['TipoResultado'], normalize='index').plot(kind='barh', stacked=True, colormap='Accent')
plt.title("Proporción de resultados por sexo")
plt.xlabel("Proporción")
plt.tight_layout()
plt.show()


print("-----------------------------------------------------------------------------------------")
print("---------------- ¿Qué edades tienen los animales al momento del resultado? --------------")
print("-----------------------------------------------------------------------------------------")

df['Edad'].value_counts().head(10).plot(kind='bar', color='coral')
plt.title("Edades más comunes al momento del resultado")
plt.ylabel("Cantidad")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

'''
## 🧪 Actividades prácticas y desafíos
> 💡 ¡Podés utilizar todas las herramientas de pandas que practicamos: filtros, agrupaciones, gráficos, funciones lambda, creación de columnas nuevas y más!
'''


'''
1. **Filtrar por especie:** Mostrá sólo los registros correspondientes a gatos (`Cat`). ¿Cuántos hay en total?
'''
df_gatos = df[df["TipoAnimal"] == "Cat"]
print("El total de los gatos es de", len(df_gatos))


'''
2. **Top razas:** ¿Cuáles son las 5 razas más comunes en el dataset? Representalo en un gráfico de barras.
'''
df_razas = df["Raza"].value_counts().head(5)
print(df_razas)
df_razas.plot(kind='bar', color='coral')
plt.title("5 razas más comunes")
plt.ylabel("Cantidad")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

'''
3. **Animales con nombre:** ¿Qué proporción de animales tiene nombre? Representalo con un gráfico de torta.
'''
con_nombre = df_gatos["Nombre"].notna().sum()
sin_nombre = df_gatos["Nombre"].isna().sum()

print(f"Gatos con nombre: {con_nombre}")
print(f"Gatos sin nombre: {sin_nombre}")

plt.figure(figsize=(6, 6))
plt.pie([con_nombre, sin_nombre],
        labels=["Con nombre", "Sin nombre"],
        autopct="%1.1f%%",
        startangle=90,
        colors=["lightseagreen", "lightgray"])
plt.title("Proporción de gatos con nombre")
plt.axis("equal")
plt.show()


'''
4. **Resultados por raza dominante:** Analizá si hay razas que tienen mayores tasas de adopción. Filtrá las 10 razas más frecuentes y compará los resultados.
'''
top10Razas = df['Raza'].value_counts().head(10).index.tolist()
dfTop10Razas = df[df['Raza'].isin(top10Razas)]
#El value_counts normalize true devuelve las proporciones
proporciones = dfTop10Razas.groupby('Raza')['TipoResultado'].value_counts(normalize=True).unstack().fillna(0)
proporcionPorRaza = proporciones['Adoption'].sort_values(ascending=False)
print("Proporción de adopciones por las 10 razas más frecuentes:", proporcionPorRaza)

proporciones.head(10)
#dfTop10Razas.head(10)

'''
5. **Edad más común:** ¿Cuál es la edad al momento del resultado más frecuente para los animales adoptados?
'''
print(f"La edad más común al momento de adopcion es:",  df[df['TipoResultado'] == 'Adoption']['Edad'].mode().tolist())


'''
6. **Nombres más comunes:** ¿Cuáles son los 10 nombres de animales más comunes en el dataset?
'''
top10Nombres= df['Nombre'].value_counts().head(10)
print("Los 10 nombres más comunes son:")
print(top10Nombres)

'''
7. **Cruza o no cruza:** Agregá una nueva columna que indique si el animal es de raza pura o mestizo, en base a la columna de raza (`Raza`).
'''

def cruza_nocruza(raza):
    if 'domestic' in raza :
      return 'mestizo'
    else:
        return 'Raza pura'
df['tipo']=df['Raza'].apply(cruza_nocruza)
df.head(11)

'''
8 Tendencia de adopciones: Convertí la columna de fecha de nacimiento a datetime y tratá de analizar si hay alguna relación entre el año de nacimiento y la probabilidad de adopción.
'''
df['FechaNacimiento'] = pd.to_datetime(df['FechaNacimiento'], errors='coerce')

# Creamos una columna año de nacimiento
df['año_nacimiento'] = df['FechaNacimiento'].dt.year

# Contamos cuántos animales nacieron por año
total_por_año = df.groupby('año_nacimiento').size()

# Contamos el total de cuántos de esos fueron adoptados
adoptados_por_año = df[df['TipoResultado'] == 'Adoption'].groupby('año_nacimiento').size()

# Calculamos el porcentaje de adopción adoptados por año dividido el total de adoptados por año y lo transformamos en porcentaje ignorando nulos
porcentaje_adopcion = (adoptados_por_año / total_por_año * 100).dropna()

# Graficar
plt.figure(figsize=(12, 6))
porcentaje_adopcion.plot(marker='o', color='orange')
plt.title("Tasa de adopción según año de nacimiento")
plt.xlabel("Año de nacimiento")
plt.ylabel("Probabilidad de adopción (%)")
plt.grid(True)
plt.tight_layout()
plt.show()
correlacion = porcentaje_adopcion.index.to_series().corr(porcentaje_adopcion)
print(f"La relacion entre el año de nacimiento y las adopciones son de: {correlacion:.3f}")
##Basicamente los animales nacidos en años más recientes tienen mayor posibilidad de ser adoptados, la tendencia es que se adoptan más animales "jovenes"

'''
9. **Relación entre edad y resultado:** Explorá si existe una diferencia en el tipo de resultado según la edad del animal.

'''
df['datetime'] = pd.to_datetime(df['datetime'], errors='coerce')
df['FechaNacimiento'] = pd.to_datetime(df['FechaNacimiento'], errors='coerce')

##Calculamos la edad al mmomento del resultado
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