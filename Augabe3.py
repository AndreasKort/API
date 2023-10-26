# es sieht nicht nur leichter aus wie javascript man versteht es drieckt XD
import random

zielzahl = random.randint(1, 20)

versuche = 0
while True:
    geratene_zahl = int(input("Rate eine Zahl zwischen 1 und 20: "))
    versuche += 1

    if geratene_zahl == zielzahl:
        print(f"Glückwunsch! Du hast die richtige Zahl ({zielzahl}) erraten. Du hast {versuche} Versuche gebraucht.")
        break
    elif geratene_zahl < zielzahl:
        print("Die geratene Zahl ist zu niedrig. Versuche es erneut.")
    else:
        print("Die geratene Zahl ist zu hoch. Versuche es erneut.")
