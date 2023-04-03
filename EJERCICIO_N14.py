print("CURSO DE PYTHON")
print("NOMBRE: SANDRO SANCHEZ")
print("FECHA: 31/03/2023")
#14. Programa para determinar si un número es divisible por 4 y 6:
numero=input("ingrese un numero del 1 al 9: ")

if len(numero) != 1:
    print("ERROR")
elif numero in "0123456789":
    print(f" EL NUMERO {numero} ES CORRECTO")
else:
    print(f"EL NUMERO {numero} ES INCORRECTO")