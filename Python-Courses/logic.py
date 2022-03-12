#************************************** Valores Booleanos ********************************
'''num = 8
if num < 10:
    num = True
else:
    num = False
print(num)


data = ("John", "Doe", 53.44)
format_string = "Hello %s %s. Your current balance is $%s."

print(format_string % data)

print(2304 % 400)
print(2300 % 100)
print(2304 % 4)

x=[1,2,3]
print("la lista contiene %d elementos" % len(x))

x = object()
y = object()

x_list = [x]*10
y_list = [y]*10
big_list = x_list + y_list

print("x_list contains %d objects" % len(x_list))
print("y_list contains %d objects" % len(y_list))
print("big_list contains %d objects" % len(big_list))

# testing code
if x_list.count(x) == 10 and y_list.count(y) == 10:
    print("Almost there...")
if big_list.count(x) == 10 and big_list.count(y) == 10:
    print("Great!")

num=[]

N = int(input("Ingrese un numero: "))
for n in N:
    num.insert(i,N)
    print(num)
    #num.remove()
    num.sort()
    num.pop()
    num.reverse()

import sys
print(sys.version)

print(10/2)
name = "Enrique is the best"
b = name.replace("Enrique", "Luis")
print(b)
print(name.find("is"))

A=["a","b","C"]
A.extend(["d","E"])
print(A)
A.append([1,2,3])
print(A)



color=["red", "green", "blue"]
for i,colors in enumerate(color):
    print(i,colors)
  

def con(a, b):
    return(a + b)
print(con("hello ","world"))

a=[]
for i in range(4):
    a.append(i**2)
print(a[3])

people=[3,4,8,5]
sd=[]

mean=sum(people)/len(people)
print(mean)
for p in range(len(people)):
    variance=(people[p]-mean)**2
    sd.append(variance)
    print(variance)
print(sd)
d=sum(sd)/len(people)
print(d)

g=25
g=(g)**0.5
print(g)


players = [180, 172, 178, 185, 190, 195, 192, 200, 210, 190]
pb=[]
mean=sum(players)/len(players)
for p in range(len(players)):
    variance=(players[p]-mean)**2
    pb.append(variance)
bas=sum(pb)/len(players)
bas=(bas)**0.5

print(mean)
print("%.2f" % (bas))
a = mean - bas
b = mean + bas
print("(%.2f - %.2f)" % (a,b))

for i in players:
    if i > a and i < b:
        print(i)


n=int(input("Ingrese el numero de arreglos: "))
arr = list(map(int,input("Ingrese los elementos de cada arreglo: ").rstrip().split()))
print(arr)
arr.reverse()
print(arr)'''


