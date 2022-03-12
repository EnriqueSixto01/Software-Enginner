
#************************************* Function Restaurant *******************************************
def solve(meal_cost,tip_percent,tax_percent):
    m = ((meal_cost/100)*tip_percent)
    t =((meal_cost)*tax_percent/100)
    print(round(meal_cost + m + t))

meal = float(input("ingrese un precio: "))
tip = int(input("Ingrese el " "%" " de propina: "))
tax = int(input("Ingrese el " "%" " de impuesto: "))

print("The total cost is: ")
solve(meal,tip,tax)
#*********************************************************************************************************
print('"First Line\n\t\Second Line"')
#*********************************** Función Segunda Ley de Newton ***************************************
def F(masa):
    a=9.81
    print(masa * a)
   
F(int(input("Ingrese un valor: \n")))
F(70)
F(54)
#*********************************** Función Ley de Ohm ***************************************************
def Ohm(I, R):
    V = I * R
    print("El voltaje en la resistencia es: ")
    return V

print(Ohm(0.0025,1000))

#*********************************** Función Año bisiesto y No bisiesto ************************************
def año_bisiesto(año):
    if año % 400 == 0:
        bisiesto = True
    elif año % 100 == 0:
        bisiesto = False
    elif año % 4 == 0:
        bisiesto = True
    else:
        bisiesto = False
    print("El año:",año,"es:")
    return bisiesto
  
año = int(input("Ingrese un año:"))
print(año_bisiesto(año))


#***********************************************************************************************************
def AddDC(x):
    x=x+"DC"
    print(x)
    return x

x="AC"
AddDC(x)
#************************************************** GLOBAL VARIABLE *****************************************
artist = "Michael Jackson"

def printer(artist):
    global internal_var 
    internal_var= "Whitney Houston"
    print(artist,"is an artist")

printer(artist) 
printer(internal_var)

#************************************************ Collections ********************************************
def printAll(*args): # Todos los argumentos son 'packed' dentro de args que pueden ser tratados como una tupla
    print("No of arguments:", len(args)) 
    for argument in args:
        print(argument)
#printAll with 3 arguments
printAll('Horsefeather','Adonis','Bone')
#printAll with 4 arguments
printAll('Sidecar','Long Island','Mudslide','Carriage')

#Similarmente, los argumentos pueden ser agregados dentro de un diccionario
def printDictionary(**args):
    for key in args:
        print(key + " : " + args[key])

printDictionary(Country='Canada',Province='Ontario',City='Toronto')

#********************************* Serie de Fibonacci *************************************************
#Caso Recursivo: donde llamamos a la funcion dentro de la misma funcion
def fibonacci(n):
    if n == 0 or n == 1:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)

print(fibonacci(3))
