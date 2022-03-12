#Creamos un archivo .txt y lo guardamos en una carpeta en el escritorio de nuestra PC
#Con la funcion open() abrimos el archivo
file = open("C:/Users/Enrike/Desktop/File/Ejemplo.txt","r")
print(file.name)                #Podemos obtener el nombre del archivo con .name
print(file.mode)                #Podemos obtener el modeo del archivo con .mode
print(file.read())              #Leemos el contenido del archivo con .read()
file.close()                    #Es importante cerrar el archivo, si ya no lo estamos utilizando
                                #Aqui lo cerramos manualmente
texto = "texto.txt"
#file1=open(texto,"r")
#print(file1.name)

with open(texto,"r") as file1:
    print(file1.read(4))               #Leemos el contenido del archivo pero solo los primeros 4 caracteres.
    print(file1.read(4))               #Si llamamos por 2da vez al metodo los sig 4 caracteres seran imprimidos
    #print(file1.readline(25))         #.readlines() imprime el archivo en tipo lista
    #print(file1.readline())           #.readline() lousamos para leer toda una linea del archivo 
    
#****************************** A better way to open a file *********************
with open("C:/Users/Enrike/Desktop/File/Ejemplo.txt","r") as file:  #Usando la declaración 'with', automaticamente 
    archivo = file.read()                                           #cerrará el archivo incluso si el codigo observa
    print(archivo)                                                  #alguna excepción.
                                                                    
print(file.closed)                                               #Verificamos que el archivo esta cerrado, despues de
                                                                 #esto ya no se puede leer
#print(archivo)                                                  #Podemos ver lo que hay en el archivo despues de cerrado
                                               
#******************************************** WRITING FILES ***********************************************

Lines=["Escribiendo lineas en python con open\n", "Luis Enrique Sixto Lopez\n","Ciencia de Datos\n"]
with open("C:/Users/Enrike/Desktop/File/Ejemplo2.txt","w") as file_w:  #Con la funcion open y el argumento 'w' podemos 
                                                                       #crear un archivo dentro de la ruta establecida
    #file_w.write("This is the line A")                     #Agregamos contenido al archivo creado con el metodo .writes

    for line in Lines:
        file_w.write(line)

with open("C:/Users/Enrike/Desktop/File/Ejemplo2.txt","a") as test_file_w:   #con el argumento 'a' podemos escribir en
    test_file_w.write("Agregando otra linea al archivo")                 #el archivo sin que se sobreescriba el contenido

with open("C:/Users/Enrike/Desktop/File/Ejemplo2.txt","r") as test_file_w: #mostramos el nuevo contenido en el archivo
    print(test_file_w.read())
    
#****************************************** Copiar archivo a otro archivo ***********************************

with open("C:/Users/Enrike/Desktop/File/Ejemplo2.txt","r") as readfile:      #leemos el archivo Ejemplo2
    with open("C:/Users/Enrike/Desktop/File/Ejemplo1.txt","w") as writefile: #escribimos en archivo Ejemplo1
        for line in readfile:                                                #copeamos las lineas que hay en Ejemplo2 
            writefile.write(line)                                            #a Ejemplo1. (se sobreescribirá el archivo)
                                                                             
#********************************************** Aditional Modes ***********************************************
# r+ : Reading and writing
with open("C:/Users/Enrike/Desktop/File/Ejemplo.txt","r+") as rw:
    rw.write("Prueba de modo r+")

# w+ : Writing and Reading
with open("C:/Users/Enrike/Desktop/File/W&R.txt","w+") as wr:
    wr.write("Prueba de escribir\n")
    wr.write("Sendas de leyenda\n")   
    
# a+: Append and Reading
with open("C:/Users/Enrike/Desktop/File/Ejemplo.txt","a+") as a:
    a.write("\nAgregando una segunda linea")
    
                                                                 