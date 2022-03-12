#creamos una lista
Colores = ["Red",   #0
           "Blue",  #1
           "Green", #2
           "Black", #3
           "White"  #4
           ]


print(Colores)
#for element in colection:

for d in range(len(Colores)):
    print(d)                    #imprime secuencialmente los indices de cada elemento

for c in range(len(Colores)):    #para cada elemento en la lista iteramos secuencialmente los indices de cada elemento
    print(c,"-", Colores[c])     #sobre la longitud de la lista e imprimimos los indices y el elemento
                  
for i, color in enumerate(Colores): #Accedemos al indice y al elemento paralelamente.
    print(i,color)                           
                              



for color in Colores:
    color_n=color.upper()
    print(color_n)

for i in range(8):          #El tipo range() es una lista inmutable de números enteros en sucesión aritmética.
    print((i + 1)* "*")

Colores.append("Grey")
for d in range(len(Colores)):
    print(Colores[d])

#print(list(range(1, 11)))

#***************************************************************************************
'''gatitos = ["https://sumedico.lasillarota.com/mascotas/5-cuidados-basicos-que-los-gatitos-bebe-necesitan/321817"]

from IPython.display import Image
Image(url=gatitos[0])
print(id(gatitos))
print(type(gatitos))
'''
#****************************************** Tabla de Multiplicar con f-string *********************************
n = int(input("ingrese un numero entero: "))
for m in range(1,11):
    print(f"{n} x {m} = {m*n}")

#***************************************** Tabla de Multiplicar con String Formatting *************
n = int(input("ingrese un numero entero: "))
for m in range(1,11):
    print("%d x %d = %d" % (n,m,n*m))

#**************************************** Secuenciade numeros en cadena de caracteres **************
n = int(input("Ingresa un numero entero: "))
for d in (range(n)):
    #print(d)
    print(d+1, end="")

#**************************************** WHILE *****************************************************
print(" ")
dates = [1982, 1980, 1973, 2000]      #Definimos una lista de elementos

i = 0                                 #Declaramos e inicializamos la variable 'i' en cero, la cual sustituira a cada indice 
                                      #de los elementos.
year = dates[0]                       #Asignamos a la var 'year' la lista empezando con el primer indice para que 
                                      #itere desde el principio.
while(year != 1973):                  #Aplicamos la condición
    print(year)
    i = i + 1                         #Siempre se tiene que actualizar el valor de la variable ya que de no hacerlo
                                      #no se cumplira con la condicion del while y se hará un loop infinito.
    year = dates[i]                   #Iteramos el valor de cada indice y lo asignamos a la var year
    
    

print("It took ", i ,"repetitions to get out of loop.")

#************************************************************************************************
PlayListRatings = [10, 9.5, 10, 8, 7.5, 5, 10, 10]
i = 0
Rating = PlayListRatings[0]
while(i < len(PlayListRatings) and Rating >= 6):
   
    print(Rating)
    i = i + 1
    Rating = PlayListRatings[i]
print("It took ", i ,"repetitions to get out of loop.")

#***********************************************************************************************
squares = ['orange', 'orange', 'purple', 'blue ', 'orange']
new_squares = []
i=0
while(i<len(squares) and squares[i]=="orange"):
    new_squares.append(squares[i])
    i+=1
    print(new_squares)

#********************************************************************************************

x = 2
while x < 10:
    if x %2 == 0:
        print(str(x) + " is even")
    else:
        print(str(x) + " is odd")
    break
x+=1
#*****************************************************************************************
i = 8
while True:                     #while true es una manera facil de hacer un loop infinito
    print(i)
    i=i+1   
    if i >=5:
        print("Breaking")
    break                       #break obliga al loop a detenerse
print("Finished")

y = 5

while(y < 15):
    print(y)
    y += 1

