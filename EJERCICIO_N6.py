print("CURSO DE PYTHON")
print("NOMBRE: SANDRO SANCHEZ")
print("FECHA: 31/03/2023")

#Realiza un programa que lea dos números por teclado y permita elegir entre 3 opciones en un menú:

#- Mostrar una suma de los dos números
#- Mostrar una resta de los dos números (el primero menos el segundo)
#- Mostrar una multiplicación de los dos números
#- En caso de introducir una opción inválida, el programa informará de que no es correcta.

n1= int(input("ingrese el primer numero"))
n2= int(input("ingrese el segundo valor"))

print("presiona 1 para sumar")
print("presione 2 para restar")
print("presiona 3 para mutliplcar")
operacion=0
comando=input("digite la opcion")
if comando == 1:
    print("la suma es:", operacion)
    operacion= n1+n2
elif comando == 2:
    print("la resta es:", operacion)
    operacion= n1-n2
elif comando == 3:
    print("la multiplicacion es:", operacion)
    operacion= n1*n2
else:
    print("comando no encotrado", operacion)
