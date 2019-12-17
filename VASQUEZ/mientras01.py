#Pedir la edad de una persona mientras la edad sea valida don la edad no puede ser negativo ni mayor a 60
edad=0
edad_inv=(edad<20 or edad >80)
while(edad_inv):
    edad=int(input("Ingrese Edad:"))
    edad_inv=(edad<20 or edad >80)
#fin_while
print("Edad valida",edad)
