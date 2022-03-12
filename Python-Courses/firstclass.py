'''************************************************************************************************
import random  # libreria que te imprime valores aleatorios
print(random.randint(1,100))

def tiro_dado():
    return random.randint(1,6)
print("El dado dio: " + str(random.randint(1,6)))
print("\n")

def tiro_dado2(cantidad_dados):
    for dado in range(cantidad_dados):
        print("El dado " + str(dado +1) + " dio: " + str(random.randint(1,6)))
        print(range(cantidad_dados))
tiro_dado2(5)'''

'''*************************************************************************************************'''
slicin = "Enrique"
print(slicin[:3]) #Hasta que indice del caracter quieres que termine
print(slicin[1:]) #Desde que indice del caracter quieres iniciar
print(slicin[:])  #Realiza una copia de toda la cadena que se imprime

'''************************************* METODOS DE CADENA DE CARACTERES ****************************'''
nombre = "enrIqUe"
print(nombre.capitalize()) #Retorna una copia de la cadena con el primer caracter en mayuscula y el resto en minuscula
print(nombre.upper()) #Retorna una copia de la cadena con toda la cadena en mayusculas
print(nombre.lower()) #Retorna una copia de la cadena con toda la cadena en minusculas

num=int(input("Ingresa un numero: "))
print(num)

print(num:=int(input("ingresa un numero: "))) #warlus operator simplifica el codigo anterior