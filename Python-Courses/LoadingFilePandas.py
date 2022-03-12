import pandas as pd
import numpy as np  
Songs=  {
            "Artista": ["Eskorbuto", "Disidencia","La polla","Boikot",   #Creamos un DataFrame en base de la estructura
                        "Los de Marras","RIP","Envidia Koxtina"],        #de un diccionario. 
            "Album":["Anti Todo","Apologia de lo evidente","Vamos Entrando",
                     "Boikotea","Peligro Esperanza","Zuzenean","Kontratiempos"],                        
            "Año":[1980,1999,1994,2006,2020,1978,2005]
        }

songs=pd.DataFrame(Songs)           #Con el metodo pd.DataFrame() convertimos el diccionario a formato de filas y columnas,
                                    #es decir,creamos un DataFrame
print(songs)                        #Mostramos el Marco de datos creado


print(songs["Año"].head(3))                   #mostramos solo los 3 primeros datos de la columna Año
print(songs["Año"].unique())                  #Usamos el metodo .unique() para ver valores unicos (que no se repiten)
canciones=songs[songs["Año"]>=2000]           #Usamos una condicional para mostrar los datos mayores a 2000
print(canciones)

print(songs.iloc[4,0])                   #Con .iloc[] seleccionamos un dato en especifico. El 1er argumento es
                                         #la fila y el 2do argumeto es la colummna                                            
print(songs.loc[4,"Artista"])            #Con .loc[] hacemos lo mismo pero aqui el 2do argumento es el head de la columna

#**********************************************************************************************************
print(songs.loc[0:5,"Artista"])         #Para seleccionar un intervalo del dataframe usamos .loc[], como 1er argumento 
                                        #se indica de que indice a que indice van (filas) y como 2do argumento 
                                        # se especifica el head de la columna
print(songs.iloc[0:5,0])                #con .loc[] hacemos lo mismo pero con indices (aqui la indexacion empieza desde 0)

songs.to_csv("C:/Users/Enrike/Desktop/File/Songs.csv", index=False)

#****************************************** Transform Functions in Pandas *******************************
df=pd.DataFrame(np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]]), columns=['a', 'b', 'c'])
print(df)

df = df.transform(func = lambda x : x + 10)     #con la funcion lambda sumamos 10 a cada valor en el dataframe
print(df)
result = df.transform(func = ["sqrt"])          #Aplicamos la raiz cuadrada a cada valor del dataframe
print(result)