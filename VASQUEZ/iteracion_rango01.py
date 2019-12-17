#Ingresar 10 numeros y luego pedir la suma y la media de los numeros ingresados
lista=[]
suma=0
media=0
numero=0
for i in range(10):
    numero=float(input("Dame un numero:"))
    lista.append(numero)
    suma+numero
#fin_for
print("Los numeros son:")
for i in lista:
    print(i)
#fin_for
media_=suma/len(lista)
print("La suma es",suma)
print("La media es",media)
