edad=input("Ingrese su edad: ") #la funcion input siempre te retornará un tipo de dato: string
#Casting: cuando transformas el tipo de una variable a otro tipo
edad = int(edad)
print(type(edad))
if edad > 25 and edad <= 99:
    print(f"Su edad es: {edad}")
    print("Eres viejo, roto y oxidado")
elif edad > 1 and edad <= 25:
    print(f"Su edad es: {edad}")
    print("Eres de la Xaviza")
elif edad < 0:
    print("Eres la mamada mijo!!!")
else:
    print("Usted es un eternal")

#******************************************************************************************************
domestico = {"gato", "perro"}

ad = input("Ingrese un animal domestico: ")
pd = int(input("Ingrese el numero de patas del animal: "))
if ad == domestico:
    if pd == 4:
        print("Es animal domestico")
    else:
        print("No es ni perro ni gato, no sea mamon. Es un animal mutante")
else:
    print("No es Animal Domestico!!.")

#*********************************************************************************************************
animal = "caballo"
color = "cafe"

animal_granja = input("Ingrese un animal de granja montable: ")
animal_color = input("Ingrese un color para el animal: ")
if animal_granja == animal:
    if animal_color == color:
        print("Efectivamente.")
    else:
        print("Error.")
else:
    print("No mame, como va a ser un animal montable!!.")

#********************************************************************************************************
#z= 2 + 3j
#print(z.__dir__())
#print(z.real, z.imag)
#print(z.conjugate())


masa = float(input("Ingrese el valor de la masa: "))
aceleracion = float(input("Ingrese el valor de la aceleracion: "))


F=masa*aceleracion

print(f"La Fuerza es: {F} N")


#****************************************** Condicionales Anidados *********************************************
N = int(input("Ingresa un numero del rango del 1 al 100: "))
n = N%2
if N>=1 and N<=100:
    if(N >= 6) and (N <= 20):
        if n == 0:
            print("Weird")
        else:
            print("Not weird")
    elif n == 1:
        print("Weird")
    else:
        print("Not Weird")
else:
    print("El número no está dentro del rango!")

#**************************************************************************************
print("Selecciona un numero \n", "1. I love python", "2. You're the best", sep="\n")
userInput = int(input())
if userInput == 1:
    print("\nI love too")
elif userInput == 2:
    print("\nNo, you're the best")
else:
    print("\nSorry I don't understand")

print(list(range(8)))

#******************************************* Nesting *******************************************

num = 3
if num == 5:
    print("five")
else:
    if num == 7:
        print("seven")
    else:
        if num == 2:
            print("two")
        else:
            print("Something else")