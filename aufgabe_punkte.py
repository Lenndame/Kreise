"""
Berechne die Distanz zweier Punkte p1(x1, y1) p2(x2, y2)
die Koordinaten sollen über Userinput eingegeben werden
nutze dazu zum Beispiel das math-Modul (zb. für die Squareroot-Methode) 
runde das Ergebnis auf 3 Nachkommastellen

die Punkte werden über input eingegeben
"""

import math

print("die Wurzel von 4 ist: ", math.sqrt(4))

p1x1 = float(input("wie lautet x1 von p1? "))
p1y1 = float(input("wie lautet y1 von p1? "))
p2x1 = float(input("wie lautet x1 von p2? "))
p2y1 = float(input("wie lautet y1 von p2? "))

distance =  math.sqrt((pow((p1x1 - p2x1), 2)) + (pow((p1y1 - p2y1), 2))) 

print ("Die Distance beträgt: ", round(distance, 3))
