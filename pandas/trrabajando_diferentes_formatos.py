# Su desafío aquí será leer este archivo usando la función read_csv de la biblioteca Pandas. Se deben agregar algunos parámetros para que la lectura se realice correctamente. Entonces, aquí hay algunos consejos:

import pandas as pd
import chardet
import json 
import requests

# Asegúrese de que el archivo CSV esté separado por una coma o punto y coma.
# La codificación del archivo es ISO-8859-1.
# Las primeras tres líneas del archivo se pueden ignorar, ya que el encabezado sólo comienza en la cuarta línea.
# Las últimas 9 líneas también se pueden ignorar, ya que son sólo información sobre dónde se tomaron los datos.
# Para eliminar las últimas líneas es necesario agregar el parámetro engine='python'.


with open('pandas/datos_sus.csv', 'rb') as file:
    print(chardet.detect(file.read()))

datos = pd.read_csv("pandas/datos_sus.csv", sep=";", encoding='ISO-8859-1', skiprows=3, skipfooter=9, engine='python');

print(datos.head());

# Es el momento de poner a prueba tus conocimientos adquiridos durante la clase. El DataFrame que se muestra a continuación se generó después de obtener los datos de la API de Fruitvice:
# El desafío ahora es normalizar este DataFrame.
url_api = 'https://fruityvice.com/api/fruit/all'

res_datos = requests.get(url_api);

datos_fruit = json.loads(res_datos.text);

datos = pd.DataFrame(datos_fruit);

print(datos.head())

datos_normalizados = pd.json_normalize(datos['nutritions']);

print(datos_normalizados.head())

# En este punto hay un problema y es que a la hora de normalizar los datos solamente retorna un data frame de la columna normalizada en este caso es 'nutritions' lo que tenemos que hacer es eliminar la columna y concatenar el nuevo data frame al de los datos

todos_los_datos = pd.concat([datos.drop('nutritions', axis=1), datos_normalizados], axis=1,);

print(todos_los_datos.head());

