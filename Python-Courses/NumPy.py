import numpy as np               #Importamos la libreria Numpy
import matplotlib.pyplot as plt

array = np.array([[[0,1,9],    #Siempre los arrays deben contener el mismo numero de elementos y mismo tipo de dato
                  [7,8,9]]])   #Para manipular el arreglo con la lib Numpy la definimos con el metodo np.array
print(array)    
print(type(array))              #Mostramos el typo de objeto que es el arreglo
print(array.dtype)              #Mostramos el tipo de dato que contiene el arreglo

#*********Attributes**********
print("El arreglo contiene",array.size, "elementos")   # .size nos muestra el numero de elementos del arreglo
print("El arreglo es de dimension: ", array.ndim)      # .ndim nos muestra el tamaño de dimension del arreglo
print(array.shape)                                     # .shape muestra en una tupla los elementos de cada dimension
                                                       #el pimer numero representa el nuemero de listas anidadas (filas)
                                                       #y el 2do el tamaño del array (columnas)

#**************************************** BASIC OPERATIONS (VECTORS) *********************************************
u = np.array([1,2])
v = np.array([2,2])
z =[]
z_1=[]
z_2=[]
#******** Adittion *********
for n,m in zip(u,v):
    z.append(n+m)
print(z)
#******** Substraction *****
for n,m in zip(u,v):
    z_1.append(n-m)
print(z_1)
#******** Product **********
for n,m in zip(u,v):
    z_2.append(n*m)
print(z_2)
#********* Multipling with a scalar ***
y = [1,2]
x = []
for n in y:
    x.append(3*n)
print(x)
#********** Dot Product *************
result = np.dot(u,v)
print("EL producto de la matriz es:",result)

#********** Universal Functions ******
edades = np.array([22,25,26,25])
edades = np.append(edades,29)       #Como con las listas podemos usar .append() para agregar un elemento al array
mean=edades.mean()                  #Con .mean() podemos obtener el promedio de los valores dentro del array
standar_desviation = edades.std()   #Con .std() podemos obteer la desviacion estandar
max = edades.max()
min = edades.min()
print("El valor primedio es:",mean)
print("La desviacion estandar es:",standar_desviation)
print("El valor maximo es ",max, "y el valor minimo es ", min)
print(np.linspace(-2,2,num=9))      #Con .linespace() podemos mostrar intervalos muestreados.

#*************************************** Function Sen *************************************
x=np.linspace(0,2*np.pi,100)
y=np.sin(x)
plt.plot(x,y)
#plt.show()
#*************************************** Array 2D ******************************************
C = np.array([[1,1],[2,2],[3,3]])
print(C)
print(C.T)                          #Usamos el atributo .T para invertir la matriz

X=np.array([[1,0],[0,1]])
Y=np.array([[2,1],[1,2]])
Z=np.dot(X,Y)
print(Z)

#****************
x = np.arange(2,8,2)            #La funcion .arange() funciona con la funcion .range()
print(x)
x = np.append(x,x.size)
print(x)
x = np.sort(x)
print(x)
print(x[1])