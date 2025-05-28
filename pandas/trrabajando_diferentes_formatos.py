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


# Al igual que Vanessa, tu desafío es obtener un DataFrame de la tabla que contiene la información del número de habitantes de cada país.

url = 'https://es.wikipedia.org/wiki/Anexo:Pa%C3%ADses_y_territorios_dependientes_por_poblaci%C3%B3n'

#obten la primera tabla de la url
datos_wikipedia = pd.read_html(url)[0];

print(datos_wikipedia);

datos_wikipedia.to_csv('datos_wikipedia.csv', index=False);


# Crear la base de datos local con la biblioteca SQLAlchemy.
# Escribir los datos del archivo CSV en esta base de datos local.
# Realizar tres actualizaciones en la base de datos:

import sqlalchemy 
from sqlalchemy import text, create_engine, inspect

engine = create_engine('sqlite:///:memory:');

datos_banco = pd.read_csv("pandas/clientes_banco.csv");

print(datos_banco.head());

#cargar datos a SQL local 
datos_banco.to_sql('clientes', engine, index=False);

# consultar si la tabla se agrego correctamente
print(inspect(engine).get_table_names());


# Actualizar el registro del cliente ID 6840104 cuyo rendimiento anual cambió a 300000.
# Eliminar el registro de cliente ID 5008809, ya que esta persona ya no tiene cuenta en la institución financiera.
# Crear un nuevo registro de cliente siguiendo las especificaciones a continuación:
# ID_cliente: 6850985
# Edad: 33
# Grado_estudio: Doctorado
# Estado_civil: Soltero
# Tamaño_familia: 1
# Categoria_de_renta: Empleado
# Ocupacion: TI
# Años_empleado: 2
# Rendimiento_anual: 290000
# Tiene_carro: 0
# Vivienda: Casa/Departamento propio


with engine.begin() as conn:
    conn.execute(text("UPDATE clientes SET Rendimiento_anual = 300000 WHERE ID_Cliente = 6840104"));
    conn.execute(text("DELETE FROM clientes WHERE ID_Cliente=5008809"));
    conn.execute(text("INSERT INTO clientes(ID_cliente, Edad, Grado_estudio, Estado_civil, Tamaño_familia, Categoria_de_renta, Ocupacion, Años_empleado, Rendimiento_anual, Tiene_carro, Vivienda) VALUES(6850985, 33, 'Doctorado', 'Soltero', 1, 'Empleado', 'TI', 2, 290000, 0, 'Casa/Departamento propio')"))

consulta = pd.read_sql(sql="SELECT * FROM clientes WHERE ID_Cliente=6840104", con=engine.connect());
consulta2 = pd.read_sql(sql="SELECT * FROM clientes WHERE ID_Cliente=5008809", con=engine.connect());
consulta3 = pd.read_sql(sql="SELECT * FROM clientes WHERE ID_Cliente=6850985", con=engine.connect());
print(consulta, consulta2, consulta3);






