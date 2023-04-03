print("CURSO DE PYTHON")
print("NOMBRE: SANDRO SANCHEZ")
print("FECHA: 31/03/2023")

calificacion= float(input("ingrese su calificacion"))
if calificacion >=0.00 and calificacion <4.00:
    print("su equivalencia es DEFICIENTE")
elif calificacion >=4.00 and calificacion <7.00:
    print("su equivalencia es REGULAR")
elif calificacion >=7.00 and calificacion <8.50:
    print("su equivalencia es BUENO")
elif calificacion >=8.50 and calificacion <9.50:
    print("su equivalencia es MUY BUENO")
elif calificacion >=9.50 and calificacion <=10.00:
    print("su equivalencia es EXCELENTE")
else:
    print("la nota introducida no es esta en el rango establecido")