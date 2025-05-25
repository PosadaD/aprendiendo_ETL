
# Ha llegado el momento de poner a prueba los conocimientos adquiridos durante la lección. Para ello, vamos a utilizar otro conjunto de datos en un desafío que se desarrollará a lo largo del curso. Este conjunto de datos es una versión modificada del archivo disponible en el sitio de Kaggle. Por lo tanto, utilizaremos el archivo raw disponible en Github.

# En esta etapa, debes cargar los datos. Para hacerlo, importa NumPy y utiliza la función loadtxt. Utiliza el enlace de la URL y el parámetro usecols para omitir la primera columna. Puedes usar np.arange para crear la secuencia de números que representan las columnas. Por último, también es necesario incluir el parámetro skiprows=1 para que la primera línea de texto se omita al leer el archivo.

import numpy as np;

datos = np.loadtxt("NumPy/citrus.csv", delimiter=",", skiprows=1, usecols=np.arange(1,6,1));

# print(datos.shape);
# print(datos.T)


# Ha llegado el momento de poner a prueba los conocimientos adquiridos durante la lección. Continuando con el proyecto de las naranjas/toronjas, ahora debes seleccionar parte de los datos. Las columnas que evaluaremos son el diámetro y el peso. Crea arrays específicos para almacenar el diámetro y el peso de la naranja y la toronja. El diámetro está en la columna cero y el peso en la columna uno. Los datos de las naranjas van hasta la fila 4999 y los datos de las toronjas comienzan en la fila 5000 del archivo.

# Después de seleccionar los datos, importa la biblioteca matplotlib y crea un gráfico para el peso en función del diámetro tanto para las naranjas como para las toronjas.

import matplotlib.pyplot as plt;

# diameter,weight,red,green,blue

diametroN = datos[:4999, 0];
pesoN = datos[:4999, 1];

diametroT = datos[5000:, 0];
pesoT = datos[5000:, 1];

plt.plot(pesoN, diametroN);
plt.plot(pesoT, diametroT);
plt.xlabel("Peso")
plt.ylabel("Diametro")
plt.legend(["Naranjas", "Toronjas"])
plt.savefig("grafico.png") 
plt.close()  



# Ha llegado el momento de poner a prueba los conocimientos adquiridos durante la lección. Continuando con el proyecto de las naranjas/toronjas, ahora debes calcular el coeficiente angular y lineal para la recta de las naranjas y para la recta de las toronjas. Utiliza la fórmula de mínimos cuadrados para encontrar cada uno.

xN = datos[:4999, 0];
yN = datos[:4999, 1];
pendiente, interseccion = np.polyfit(xN, yN, 1);

y_ajustadaN = pendiente * xN + interseccion;



xT = datos[5000:, 0];
yT = datos[5000:, 1];
pendiente, interseccion = np.polyfit(xT, yT, 1);

y_ajustadaT = pendiente * xT + interseccion;

plt.plot(xT, yT, 'o');
plt.plot(xT, y_ajustadaT, 'r-');
plt.legend(['Datos originales N', 'Ajuste lineal N','Datos originales T', 'Ajuste lineal T'])
plt.savefig("pendiente-linel-T.png");
plt.close();



plt.plot(xN, yN, 'o');
plt.plot(xN, y_ajustadaN, 'r-');
plt.legend(['Datos originales N', 'Ajuste lineal N','Datos originales T', 'Ajuste lineal T'])
plt.savefig("pendiente-linel-N.png");
plt.close();




# Ha llegado el momento de poner a prueba los conocimientos adquiridos durante la lección. Continuando con el proyecto de las naranjas/toronjas, ahora debes calcular el coeficiente angular utilizando la generación de números aleatorios. Supongamos que ya conoces el valor de b y que este es igual a 17.
