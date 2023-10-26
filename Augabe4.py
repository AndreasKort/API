ursprüngliche_liste = [1, 2, 3, 4, 5]

def umkehren_liste(liste):
    umgekehrte_liste = liste[::-1]
    return umgekehrte_liste

def duplizieren_liste(liste):
    duplizierte_liste = [element for element in liste for _ in range(2)]
    return duplizierte_liste

# Die umgekehrte Liste erstellen
umgekehrte = umkehren_liste(ursprüngliche_liste)

# Die umgekehrte Liste duplizieren
duplizierte = duplizieren_liste(umgekehrte)

print("Ursprüngliche Liste:", ursprüngliche_liste)
print("Umgekehrte Liste:", umgekehrte)
print("Duplizierte, umgekehrte Liste:", duplizierte)
