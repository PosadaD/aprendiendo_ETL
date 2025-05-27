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



# Este archivo es el mismo que se utilizó para resolver los desafíos de la lección 1 y contiene datos de estudiantes de un curso superior.
# Basándonos en esto, resolvamos los problemas propuestos a continuación utilizando los conocimientos adquiridos hasta ahora.

# Verifica si la base de datos contiene datos nulos y, en caso de tenerlos, realiza el tratamiento de estos datos nulos de la manera que consideres más coherente con la situación.

nulos = datos.isnull().sum();
print(nulos);

datos['Nota'] = datos['Nota'].fillna(0);
print(datos.isnull().sum());

# Los estudiantes "Alicia" y "Carlos" ya no forman parte del grupo. Por lo tanto, elimínalos de la base de datos.

query = datos.query("Nombre=='Carlos' | Nombre == 'Alicia'").index;

copia_datos = datos.drop(query, axis=0);

print(copia_datos)

# Aplica un filtro que seleccione solo a los estudiantes que fueron aprobados.

datos.loc[datos["Aprobado"] == 'Verdadero', "Aprobado"] = 'True';
datos["Aprobado"] = datos["Aprobado"]

datos_aprobados = datos[datos['Aprobado'] == 'True'];
print(datos_aprobados)


# Extra: Al revisar las calificaciones de los estudiantes aprobados, notamos que algunas calificaciones eran incorrectas. Las estudiantes que obtuvieron una calificación de 7.0, en realidad tenían un punto extra que no se contabilizó. Por lo tanto, reemplaza las calificaciones de 7.0 en la base de datos por 8.0. Consejo: busca el método replace.

datos.loc[datos["Nota"] >= 7, "Nota"] += 1;
datos.loc[datos["Nota"] > 10, "Nota"] = 10;
print(datos[datos["Aprobado"] == 'True']);

# Guarda el DataFrame que contiene solo a los estudiantes aprobados en un archivo CSV llamado "alumnos_aprobados.csv".

datos.to_csv('alumnos_aprobados.csv', index=False);