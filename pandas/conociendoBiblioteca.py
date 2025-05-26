# 1)Importa el archivo alumnos.csv y almacena su contenido en un DataFrame de Pandas.

import pandas as pd

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