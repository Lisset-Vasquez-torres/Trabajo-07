#Pedir el peso de un adulto mientras el peso sea normal don el peso no puede ser menor de 30 ni mayor a 90
peso=0
peso_elevado=(peso<30 or peso >90)
while(peso_elevado):
    peso=int(input("Ingrese Peso:"))
    peso_elevado=(peso<30 or peso >90)
#fin_while
print("Peso Elevado",peso)
