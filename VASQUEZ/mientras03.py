#Pedir la nota de un alumno mientras la nota sea aprobada don la nota no puede menor de 10.5 ni mayor a 20
nota=0.0
nota_desaprobada=(nota<10.5 or nota >20)
while(nota_desaprobada):
    nota=float(input("Ingrese Nota:"))
    nota_desaprobada=(nota<25 or nota >70)
#fin_while
print("Nota desaprobada",nota)
