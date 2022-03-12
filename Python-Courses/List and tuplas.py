#***************************************** LISTA ******************************************************
#Una lista es una estructura de datos utilizada para almacenar múltippes valores en secuencia, ordenada por indices.
Colores = ["Red",   #0
           "Blue",  #1
           "Green", #2
           "Black", #3
           "White",  #4
           "White"  #4
           ]
print(Colores)
print(Colores[3])

print(len(Colores))   #len() devuelve la longitud de una cadena de caracteres 
                      #o el número de elementos de una lista

print(Colores[0])
Colores[0] = "Gold"
print(Colores[0])

print(Colores.index("Green"))  #.index() retorna el indice de la primera ocurrencia elemento de la lista.
print(Colores.count("Blue"))   #.count() indica cuantas instatncias de un mismo elemnto hay en la lista
print(Colores.pop())           #.pop() elimina el último elemento y lo retorna. (Es un metódo de cadena de caracteres)
Colores.insert(2,"Brown")      #.insert() agrega un elemento en un indice especifico.
Colores.append("Grey")         #.append() agrega un elemento al final de la lista. 2 o más items se agregan como una 2da list
Colores.remove("Gold")         #.remove() elimina un elemento de la lista.
Colores.reverse()              #.reverse() cambia el orden de los elementos
Colores.extend(["Yellow", "Orange"])  #.extend() agrega elementos a la lista dentro de la primera dimensión
print(Colores)

#******************************************************* TUPLA *******************************************************
Colores_t = (   "Red",   #0
                "Blue",  #1
                "Green", #2
                "Black", #3
                "White"  #4
                )
print(Colores_t)
print(Colores_t[3])
print(list(range(5,9)))      
print(len(range(1,20,7)))

#Una TUPLA no te permite reasignar un nuevo valor a una variable, es inmutable.
#print(Colores_t[0])
#Colores_t[0] = "Gold"
#print(Colores_t[0])
#***************************************************************************
#Slicing
#[inicio:fin-1:salto]
print(Colores_t[0:len(Colores):2])

#********************************************** SORT & SORTED ***************************************************
L=[9,2,5,4,1]
L.sort()        #sort() devuelve los elementos de una lista de forma ascendente
print(L)
E=sorted(L)     #sorted() devuelve una nueva lista con todos los elementos, de forma ascendente
print(E)

#********************************************** Array Bidimensionales ***********************************
l = [[1,2,3,["e","g"]],
     [5,6,7]]
print(l[0][3][0])