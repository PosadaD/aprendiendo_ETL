# 1)Importa el archivo alumnos.csv y almacena su contenido en un DataFrame de Pandas.

import pandas as pd
import matplotlib.pyplot as plt

URL="https://gist.githubusercontent.com/ahcamachod/807a2c1cf6c19108b2b701ea1791ab45/raw/fb84f8b2d8917a89de26679eccdbc8f9c1d2e933/alumnos.csv"

datos = pd.read_csv(URL);

# 2)Visualiza las primeras 7 filas del DataFrame y las últimas 5.

print(datos.head(7));
print(datos.tail(5));

# 3)Verifica la cantidad de filas y columnas en este DataFrame.

print(datos.shape);

# 4)Explora las columnas del DataFrame y analiza los tipos de datos presentes en cada columna.

print(datos.info());

# Extra: Calcula algunas estadísticas descriptivas básicas de los datos en el DataFrame (media, desviación estándar, etc.). Pista: busca el método "describe".

print(datos.describe());


# El equipo de ML ha llegado con algunas demandas de última hora que debemos resolver en este momento de análisis exploratorio. Estas demandas son las siguientes:
# Tipo Colonia  Habitaciones  Garages  Suites  Area    Valor  Condominio  Impuesto

URL_inmobiliaria = "https://gist.githubusercontent.com/ahcamachod/a572cfcc2527046db93101f88011b26e/raw/ffb13f45a79d31223e645611a119397dd127ee3c/alquiler.csv"

datos_inmobiliaria = pd.read_csv(URL_inmobiliaria, sep=";");

# Calcular el promedio de habitaciones por departamento.

opcion_1 = datos_inmobiliaria.groupby("Tipo")["Habitaciones"].mean().loc["Departamento"];
print(opcion_1);

opcion_2 = datos_inmobiliaria.query("['Departamento'] in Tipo")["Habitaciones"].mean()
print(opcion_2);

# Verificar cuántas colonias únicas existen en nuestra base de datos.

colonia = datos_inmobiliaria['Colonia'].unique();
print(colonia);

# Analizar qué colonias tienen el promedio de alquiler más alto.

valor_mas_alto = datos_inmobiliaria.groupby('Colonia')['Valor'].mean().sort_values();
print(valor_mas_alto);

# Crear un gráfico de barras horizontales que muestre las 5 colonias con los promedios de alquiler más altos.

grafico_5_primeros = valor_mas_alto.head(5);
grafico_5_primeros.plot(kind="bar", figsize=(15, 11), color="blue");
plt.savefig("5_colonias");
plt.close();