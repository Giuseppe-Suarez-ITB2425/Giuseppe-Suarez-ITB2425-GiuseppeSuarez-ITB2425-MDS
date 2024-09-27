"""
Javier Amaya Boira

12/09/2023

ASIXc M03 UF1 A1

Descripció: Exemple dels apunts
"""

# Programa que demana l'edat i diu si ets major d'edat.

edat = int(input("Quina edat tens? "))
año_actual = int(input("En quin any estem?"))
if edat >= 18:
    print("Ets major d'edat")
elif 13<= edat <18:
    print("Ets un adolescent")
else:
    print("No ets major d'edat")
año_nacimiento = año_actual - edat
print(f"Vas neixer al any: {año_nacimiento} ")
print("Programa Finalitzat")
