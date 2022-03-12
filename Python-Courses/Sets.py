
conjunto = {"Enrique", "Yio", 25, 26, "Enrique", 25}    #Un conjunto es una unica colección de objetos en python, 
                                                        #si hay algun elemento repetido en la lista python 
                                                        #automaticamente lo eliminará 
print(conjunto)   

colores_list = ["negro","azul",8.5,12.78]               #Podemos convertir una lista a un conjunto
colores_set = set(colores_list)
print(colores_set)

#****************************************** Set Operations *********************************
Bandas = {"celtian","evanecense","eluviete"}
Bandas.add("saurom")                            #agregamos un elemento mas al set con .add()
#print(Bandas)
Bandas.remove("evanecense")                     #eliminamos un elemento del set con .remove()
#print(Bandas)

#************************************** Intersection ***********************************

Bandas_1 = {"celtian","evanecense","eluviete"}
Bandas_2 = {"evanecense","celtian","saurom"}

intersection = Bandas_1 & Bandas_2               #con la intersection solo obtendremos los elementos que se encuentren
print(intersection)                              #en ambos conjuntos

print(Bandas_1.difference(Bandas_2))            #Podemos encontrar los elementos que diferencian a un conjunto del otro
print(Bandas_2.difference(Bandas_1))
print(Bandas_1.union(Bandas_2))                 #Pdemos unir todos los elementos de ambos sets en uno solo

print((Bandas_1).issuperset(Bandas_2))          #Podemos revisar si los elemntos de un conjunto estan dentro 
print((Bandas_2).issubset(Bandas_1))            #de otro conjunto o si un conjunto tiene elementos de otro conjunto
                                                #con las funciones .issupset() y .issubset
  