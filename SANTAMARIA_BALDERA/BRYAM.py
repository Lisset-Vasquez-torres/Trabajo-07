#ejercicio 1
# Mostrar los numeros de cero(0) hasta trecientos(300)
n=0
while(n<301):
    print(n)
    n=n+1

#fin_while


# Ejercicio 02
# Mostrar la serie 0,5,10,15,20,25,30,35,40,45,50,55,60,65,70,75
n=0
while(n<=75):
    print(n)
    n=n+5

#fin_while


#ejercicio 03
# Mostrar los numeros del 30 hasta el 10
b=30
while(b>9):
    print(b)
    b=b-1

#fin_while


# Mostrar los numeros desde -7 hasta 7 y luego desde 7 hasta -7
i=-7
n=7
while(i<=7):
    print(i)
    i=i+1
#Fin_while

while(n>-8):
    print(n)
    n=n-1

#Fin_while

# Ejercicio nro 05
# Mostrar los numeros impares que hay desde 10 hasta 40

n=7
while(n<30):
    print(n)
    n+=2
#Fin_while


#Ejercicio nro 01
# pedir una nota de matematicas, donde la nota debe estar entre 0 y 20
# mientras la nota ingresada no es valida debe ingresarce otra vez.
nota=int (input("ingrese nota:"))
while(nota < 0  or nota >20):
    nota=int(input("Ingrese nota"))
#fin_While
print("La nota es:",nota)

nota=-1
nota_invalida=(nota < 0 or nota > 20)
while(nota_invalida):
    nota=int (input("ingrese nota(0-20):"))
    nota_invalida
    lida=(nota < 0 or nota > 20)
# Fin_while

# Ejercicio nro 02
# Mostrar "Intruso" Mientras la clave no sea abc1234.
password=""
password_ivalid=(password!="abc123")
while(password_ivalid):
    print("Intruso")
    password=input("Enter password:")
    password_ivalid=(password!="abc1234")
#fin_while
print("Welcome")


# Ejercicio nro 03
# Ingrese a1 y luego pedir a2, mientras a2 sea menor a a1
# Donde a1 es un numero para entero positivo
a1=1
numero_ivalido=((a1%2)!=0)
a2=0
while(numero_ivalido):
    a1=int(input("Ingrese a1:"))
    numero_ivalido=((a1%2)!=0)
while(a2<a1):
    a2=int(input("Ingrese a2:"))
#Fi_While
print("A1=",a1,"A2=",a2)


# #Ejercicio nro 04
#Pedir la edad de una persona mientras la edad sea valida don la edad
# no puede ser negativa ni mayor a 60
edad=0
edad_inv=(edad < 18 or edad >60)
while(edad_inv):
    edad=int(input("Ingrese Edad:"))
    edad_inv=(edad < 18 or edad > 60)
#Fin_while
print("Edad valida",edad)


# Ejercicio nro 05
# Mostrar "Intruso" Mientras la clave no sea abc1234.
color=""
numero=0
numero_invalido=(numero!="1" or numero!="2")
while(numero_invalido):
    print("no es el color")
    password=input("Ingrese el numero:")
    password_ivalid=(numero!="Blanco", numero!="Negro")
#fin_while
print("color valido")


# iteracion decoficador 01
import os

msg=str(os.sys.argv[1])

for letra in msg:
    if(letra == "F"):
        print("Feliz")
    if (letra == "A"):
        print("Aniversario")
    if (letra == "S"):
        print("Samsung")
#Fin_For


# iteracion decoficador 02
import os

msg=str(os.sys.argv[1])
for letra in msg:
    if(letra == "S"):
        print("Semaforo")
    if (letra == "V"):
        print("Verde")
    if (letra == "A"):
        print("Amarillo")
    if (letra == "R"):
        print("Rojo")

#Fin_For


# iteracion decoficador 03
import os

msg=str(os.sys.argv[1])
for letra in msg:
    if(letra == "M"):
        print("Milagros")
    if (letra == "N"):
        print("Necesito")
    if (letra == "D"):
        print("Dinero")

#Fin_For


# iteracion decoficador 04
import os

msg=str(os.sys.argv[1])
for letra in msg:
    if(letra == "P"):
        print("Profesor")
    if (letra == "F"):
        print("Feliz")
    if (letra == "N"):
        print("Navidad")


#Fin_For


# iteracion decoficador 05
import os

msg=str(os.sys.argv[1])

for letra in msg:
    if(letra == "B"):
        print("Bryan")
    if (letra == "G"):
        print("Ganaste")
    if (letra == "U"):
        print("Un")
    if (letra == "I"):
        print("Iphone11s")
#Fin_For


#Ejerecicio nro 01
# Ingresar 5 numeros y luego pedir la suma y la media de los numeros ingresados
lista=[]
suma=0
media=0
numero=0
for i in range(5):
    numero=float(input("Dame un numero:"))
    lista.append(numero)
    suma+=numero
#fin_for
print("Los numeros son:")
for i in lista:
    print(i)
#Fin_for
media_=suma/len(lista)
print("La suma es",suma)
print("La media es",media)


# Ingrese un contador con un  rango de 100 a 700  y pedir la cantidad de multiplos de 3 y 7
contador=0
for i in range(100,700):
    if(i%3==0 and i%7==0):
        contador+=1
    #Fin_si
#fin_for
        print(i)
print("La cantidad de multiplos de 3 y 7 es:",contador)


# Ingrese el cantidad de empleados, donde el sueldo < 500 y pedir el total a pagar
suma=0
cont1=0
cont2=0
n=int(input("Ingrese cantidad de empleados:"))
for i in range(1,n+1):
    sueldo=float(input("Ingrese sueldo:"))
    suma+=sueldo
    if(sueldo<500):
        cont1+=1
    #Fin_if
#Fin_ford
    else:
        cont2+=1
print("Menos de 500:",cont1)
print("Mas de 500:",cont2)
print("Total en pagar:",suma)



# Crear una Tambla donde al introducir un numero multplice en un rango del 1 al 12 muestre el resultado
n=int(input("Introduce un numero: "))
for i in range (1,13):
#Fin_For
    print(n,"*",i,"=",n*i)
