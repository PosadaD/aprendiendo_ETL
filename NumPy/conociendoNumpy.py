
# Ha llegado el momento de poner a prueba los conocimientos adquiridos durante la lección. Para ello, vamos a utilizar otro conjunto de datos en un desafío que se desarrollará a lo largo del curso. Este conjunto de datos es una versión modificada del archivo disponible en el sitio de Kaggle. Por lo tanto, utilizaremos el archivo raw disponible en Github.

# En esta etapa, debes cargar los datos. Para hacerlo, importa NumPy y utiliza la función loadtxt. Utiliza el enlace de la URL y el parámetro usecols para omitir la primera columna. Puedes usar np.arange para crear la secuencia de números que representan las columnas. Por último, también es necesario incluir el parámetro skiprows=1 para que la primera línea de texto se omita al leer el archivo.

import numpy as np;

datos = np.loadtxt("NumPy/citrus.csv", delimiter=",", skiprows=1, usecols=np.arange(1,6,1));

print(datos.shape);
print(datos.T)

