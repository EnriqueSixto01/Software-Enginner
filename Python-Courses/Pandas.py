import pandas as pd                             #Importamos la libreria Pandas
import numpy as np

data = "C:/Users/Enrike/Desktop/File/Data.csv"  #Cargamos nuestro archivo .csv desde su ruta de localización
df = pd.read_csv(data,header=None)              #Leemos el archivo asignandole un encabezado de filas y columnas con N°
print(df.head(5))                               #Solo mostramos las primeras 5 filas del marco de datos

headers = ["symboling","normalized-losses","make","fuel-type","aspiration", "num-of-doors","body-style",
         "drive-wheels","engine-location","wheel-base", "length","width","height","curb-weight","engine-type",
         "num-of-cylinders", "engine-size","fuel-system","bore","stroke","compression-ratio","horsepower",
         "peak-rpm","city-mpg","highway-mpg","price"]

df.columns = headers                          #Definimos las cabeceras para cada columna
print(df.head(10))                            #Mostramos las primeras 10 filas

 #Guardamos nuestro archivo con los cambios hechos en nuestro equipo local
df.to_csv("C:/Users/Enrike/Desktop/File/Data_automobile.csv", index=False)   

print(df.dtypes)                              #Mostramos el tipo de dato que es cada columna

print(df.describe())                          #Mostramos un resumen estadistico de los datos (solo datos tipo int y float)

print(df.describe(include = "all"))           #Mostramos el resumen de datos pero incluyendo los datos tipo object

#Podemos seleccionar solo las columnas que deseemos del marco de datos aplicando el metodo .describe() para un resumen
print(df[['symboling','length', 'compression-ratio']].describe())

#Con .info() podemos observar la informacion de las primeras 30 filas y las ultimas 30 filas del marco de datos
print(df.info())    

print(df["price"].tail(5))                          #Mostramos los utimos 5 datos de una columna en especifico

df.replace("?",np.nan,inplace=True)             #Usamos el metodo .replace() para convertir los valores faltantes a NaN
print(df.head(10))