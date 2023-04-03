print("CURSO DE PYTHON")
print("NOMBRE: SANDRO SANCHEZ")
print("FECHA: 30/03/2023")

#Los tramos impositivos para la declaración de la renta en un determinado país son los siguientes:
#Realizar un programa que pueda decir el % de impuestos que una persona deba pagar según su sueldo

salario=float(input("INGRESE SU SUELDO: "))
impuesto=0
if salario < 10000:
    impuesto=0.05
elif salario >=10000 and impuesto < 20000:
    impuesto=0.15
elif salario >= 20000 and salario < 35000:
    impuesto=0.20
elif salario >= 35000 and salario < 60000:
    impuesto=0.30
elif salario >= 60000:
    impuesto=0.45
else:
    print ("EL SALARIO INGRESADO ES INCORRECTO")
total= salario*impuesto
print("El valor del impuesto ha pagar es ",total)
print("El salario ha resivir es ",salario - total)