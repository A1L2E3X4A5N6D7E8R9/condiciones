print("CURSO DE PYTHON")
print("NOMBRE: SANDRO SANCHEZ")
print("FECHA: 31/03/2023")

#Escribir un programa que pida al usuario una nota del 0 al 10 y muestre por pantalla la calificación según la siguiente tabla:
#- 0-2: Muy deficiente
#- 3-4: Insuficiente
#- 5-6: Suficiente
#- 7: Bien
#- 8-9: Notable
#- 10: Sobresaliente
nota=float(input("Ingrese la nota: "))
if nota >= 0 and nota <= 2:
    print(f"La nota de {nota} es muy deficiente")
elif nota >= 3 and nota <= 4:
    print(f"La nota de {nota} es insuficiente")
elif nota >= 5 and nota <= 6:
    print(f"La nota de {nota} es suficiente")
elif nota == 7:
    print(f"La nota de {nota} esta bien")
elif nota >= 8 and nota <= 9:
    print(f"La nota de {nota} es notable")
elif nota == 10:
    print(f"La nota de {nota} es sobresaliente")
else:
    print(f"La nota de {nota} no existe")
