"""
einfach

Über eine Usereingabe sind zwei Kreise k1 und k2 einzugeben. Diese Kreise sind
definiert durch Radius und Position im kart. Koordinatensystem.

Eingabe:
Position und Radius der beiden Kreise

Aufgabe:
Schneiden/Überlagern sich die Kreise?
"""
import math as m

x_1 = float(input("Kreis 1 Mittelpunkt an der X-Achse: "))
y_1 = float(input("Kreis 1 Mittelpunkt an der Y-Achse: "))
r_1 = float(input("Kreis 1 Radius: "))

x_2 = float(input("Kreis 2 Mittelpunkt an der X-Achse: "))
y_2 = float(input("Kreis 2 Mittelpunkt an der Y-Achse: "))
r_2 = float(input("Kreis 2 Radius: "))

distance = m.sqrt((pow((x_1 - x_2), 2)) + (pow((y_1 - y_2), 2))) 

# z Achse für 3D 

#geradengleichungschnittpunkte = ((r_1)**2 == ((x - x_1)**2) + ((y - y_1)**2)) - ((r_2)**2 == ((x - x_2)**2) + ((y - y_2)**2))
#

if r_2 > (r_1 + distance):
    print("Der Kreis 1 liegt in Kreis 2")
elif r_1 > (r_2 + distance):
    print("Der Kreis 2 liegt in Kreis 1")
elif (r_1 - r_2) < distance < (r_1 + r_2):
    print("Die Kreise haben Schnittpunktean den Punkten")
elif (r_1 + r_2) < distance:
    print("Die Kreise haben keine Schnittpunkte und liegen außerhalb von einander")
