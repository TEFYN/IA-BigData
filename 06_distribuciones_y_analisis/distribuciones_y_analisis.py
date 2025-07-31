import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import zscore, skew, kurtosis

# Cargar datos
df = pd.read_csv("./06_distribuciones_y_analisis/customer.csv")

# Vista previa
df.head()

print("-------------------------------- Ejercicio 1: histogra ma y curv a de densidad  --------------------------------")

sns.histplot(df["CustomerLifetimeValue"], kde=True)
plt.title("Distribución del Customer Lifetime Value")
plt.show()

print("-------------------------------- Ejercicio 2: Detección de Outliers --------------------------------")

sns.boxplot(x=df["ClaimAmount"])
plt.title("Boxplot del Claim Amount")
plt.show()


print("-------------------------------- Ejercicio 3: Detección de Outliers con IQR --------------------------------")

Q1 = df["CustomerLifetimeValue"].quantile(0.25)
Q3 = df["CustomerLifetimeValue"].quantile(0.75)
IQR = Q3 - Q1

outliers_iqr = df[(df["CustomerLifetimeValue"] < Q1 - 1.5 * IQR) | 
                  (df["CustomerLifetimeValue"] > Q3 + 1.5 * IQR)]

print(f"Cantidad de outliers detectados por IQR: {outliers_iqr.shape[0]}")


print("-------------------------------- Ejercicio 4: Detección de Outliers con Z-score --------------------------------")

z_scores = zscore(df["ClaimAmount"])
outliers_z = df[np.abs(z_scores) > 3]

print(f"Cantidad de outliers detectados por Z-score: {outliers_z.shape[0]}")

print("-------------------------------- Ejercicio 5: Botplot por cobertura --------------------------------")

# Histograma de precios
sns.boxplot(x="Coverage", y="ClaimAmount", data=df)
plt.title("Claim Amount según tipo de Coverage")
plt.show()


print("-------------------------------- Ejercicio 5: Violinplot por clase de vehiculo --------------------------------")

sns.violinplot(x="VehicleClass", y="CustomerLifetimeValue", data=df)
plt.xticks(rotation=45)
plt.title("Customer Lifetime Value por tipo de vehículo")
plt.show()


print("-------------------------------- Ejercicio 7: Asimetría --------------------------------")


skew_clv = skew(df["CustomerLifetimeValue"].dropna())
print(f"Asimetría (CustomerLifetimeValue): {skew_clv}")


print("-------------------------------- Ejercicio 8: Curtosis --------------------------------")



'''
## 📝 Parte final: Actividades para resolver

1. ¿Cuál es el tipo de distribución que presenta `ClaimAmount`?
2. Identificá si hay outliers en `CustomerLifetimeValue` usando visualización.
3. Usá el método del IQR para detectar outliers en `MonthlyPremiumAuto`.
4. Usá el método del Z-score en `TotalClaimAmount` y reportá cuántos outliers hay.
5. Compará `ClaimAmount` según `Education` con un boxplot.
6. ¿Qué diferencias ves entre `VehicleSize` y `CustomerLifetimeValue`?
7. Calculá y analizá la asimetría de `MonthlyPremiumAuto`.
8. ¿Qué indica la curtosis de `TotalClaimAmount`?
9. Usá un `pairplot` con variables numéricas del dataset.
10. ¿Cómo puede afectar la presencia de outliers en un modelo predictivo?

'''

'''
1. ¿Cuál es el tipo de distribución que presenta `ClaimAmount`?
'''
sns.histplot(df["ClaimAmount"], kde=True)
plt.title("Distribución de ClaimAmount")
plt.show()
print("Distribuci+on sesgada hacia la derecha)")


'''
2. Identificá si hay outliers en `CustomerLifetimeValue` usando visualización.
'''

sns.boxplot(x=df["CustomerLifetimeValue"])



'''
3. Usá el método del IQR para detectar outliers en `MonthlyPremiumAuto`.
'''



'''
4. Usá el método del Z-score en `TotalClaimAmount` y reportá cuántos outliers hay.
'''



'''
5. Compará `ClaimAmount` según `Education` con un boxplot.
'''




'''
6. ¿Qué diferencias ves entre `VehicleSize` y `CustomerLifetimeValue`?
'''



'''
7. Calculá y analizá la asimetría de `MonthlyPremiumAuto`.
'''




'''
8. ¿Qué indica la curtosis de `TotalClaimAmount`?
'''






'''
9. Usá un `pairplot` con variables numéricas del dataset.
'''




'''
10. ¿Cómo puede afectar la presencia de outliers en un modelo predictivo?
'''


# sns.violinplot(x="VehicleClass", y="CustomerLifetimeValue", data=df)
# plt.xticks(rotation=45)
# plt.title("Customer Lifetime Value por tipo de vehículo")
# plt.show()