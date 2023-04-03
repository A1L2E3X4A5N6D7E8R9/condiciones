print("CURSO DE PYTHON")
print("NOMBRE: SANDRO SANCHEZ")
print("FECHA: 31/03/2023")
#Determinar el mayor de tres números:
a=int(input("Ingrese el primer numero: "))
b=int(input("Ingrese el segundo numero: "))
c=int(input("Ingrese el tercer numero: "))

if a>b and a >c :
    print ("el numero ",a ," es mayor al segundo y tercer numero")
elif b>a and b >c :
    print ("el numero ",b ," es mayor al primer y tercer numero")
elif c>b and c >a :
    print ("el numero ",c ," es mayor al primer y segundo numero")
else :
    print ("Ninguno es mayor ")
