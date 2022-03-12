import matplotlib.pyplot as plt
#%matplotlib inline                    comando magico para habilitar el trazado en un notebook

class Circle(object):                   #Definimos la clase 

#Inicializamos el objeto con el construtor "_init_"
    def __init__ (self,radius,color):   
        self.radius=radius;             #Definimos los atributos de la clase/objetos del tipo
        self.color=color;               #El termino self contiene todos los atributos en el conjunto

 #Metodo usado para agregar un valor r al atributo de radius
    def add_radius(self,r):            
        self.radius=self.radius + r
        return(self.radius)

 #Metodo para graficar el objeto
    def drawCircle(self):              
        plt.gca().add_patch(plt.Circle((0, 0), radius=self.radius, fc=self.color))
        plt.axis('scaled')
        plt.title("Class Circle", fontsize = 20)
        plt.xlabel("X numbers")
        plt.ylabel("Y numbers")
        plt.show()  

RedCircle = Circle(10,"red")            #Creamos una instancia/objeto de la clase Circle y le damos parametros
BlueCircle = Circle(20,"blue")          #Creamos una segunda instancia/objeto de la clase Circle y le damos parametros
print("El radio del 1er circulo es: ", RedCircle.radius)
print("El color del 1er circulo es: ", RedCircle.color)
print("El radio del 2do circulo es: ", BlueCircle.radius)
print("El color del 2do circulo es: ", BlueCircle.color)

RedCircle.radius=5                      #Asignamos un nuevo valor para el radio del circulo

print("El nuevo radio del circulo rojo es: ", RedCircle.radius)
RedCircle.add_radius(8)
print("El radio del circulo ahora es: ", RedCircle.radius)
RedCircle.add_radius(5)
print("El radio del circulo final es: ", RedCircle.radius)

#RedCircle.drawCircle()
#BlueCircle.drawCircle()