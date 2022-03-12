#An exception is an error that occurs during the execution of code. This error causes the code to raise an exception and 
# if not prepared to handle it will halt the execution of the code.

#******************************************* Try Except *****************************************************
a = 1

try:                                                        #En este caso planteamos una operación en try: si llegara a
    b = int(input("Please enter a number to divide a: "))   #ocurrir un error en la division except ejecutara lo que 
    a = a/b                                                 #hay en su bloque y todo lo que hubiera mas adelante también
    print("Success a=",a)                                   #se ejecutará
except:
    print("There was an error")
        
#**************************************** Try Except Specific **********************************************
a = 1

try:
    b = int(input("Please enter a number to divide a"))
    a = a/b
    print("Success a=",a)
except ZeroDivisionError:
    print("The number you provided cant divide 1 because it is 0")
except ValueError:
    print("You did not provide a number")
except:
    print("Something went wrong")

#************************************** Try Except Else ***********************************************
#else allows one to check if there was no exception when executing the try block. This is useful when we want 
# to execute something only if there were no errors.
a = 1

try:
    b = int(input("Please enter a number to divide a"))
    a = a/b
except ZeroDivisionError:
    print("The number you provided cant divide 1 because it is 0")
except ValueError:
    print("You did not provide a number")
except:
    print("Something went wrong")
else:                                                       #se imprime el valor de a solo si no hay error
    print("success a=",a)

#************************************ Try Except Else and Finally *************************************
#finally allows us to always execute something even if there is an exception or not. This is usually used to
#  signify the end of the try except.
a = 1

try:
    b = int(input("Please enter a number to divide a"))
    a = a/b
except ZeroDivisionError:
    print("The number you provided cant divide 1 because it is 0")
except ValueError:
    print("You did not provide a number")
except:
    print("Something went wrong")
else:
    print("success a=",a)
finally:                            #se imprime lo que hay en finally exista o no un error
    print("Processing Complete")

