# erste aufgabe 
def print_number_triangle(row): #definieren eine Funktion    
    number = ""# eine leere Zeichenkette namens "number".  
    for i in range(1, row + 1):# eine Schleife von 1 bis zur übergebenen Zeilenanzahl "row".
        
        number += str(i) # hinzfügen die aktuelle Zahl zu unserer Zeichenkette
        print(number)

# Zeilenanzahlen werden ausgegeben bis 5
print_number_triangle(5)

# 2 aufgabe 
# Wir definieren eine Funktion namens "print_number_triangle", die Zahlen untereinander ausgibt.
def print_number_triangle(row):
    # Wir starten mit der Zahl 1.
    number = 1
    # Wir beginnen eine Schleife von 1 bis zur übergebenen Zeilenanzahl "row".
    for i in range(1, row + 1):
        # Innerhalb dieser Schleife starten wir eine weitere Schleife.
        for j in range(i):
            # Wir geben die aktuelle Zahl "number" aus, gefolgt von einem Leerzeichen, damit die Zahlen getrennt sind.
            print(number, end=" ")
            # Dann erhöhen wir die Zahl "number" um 1, damit wir zur nächsten Zahl gehen.
            number += 1
        # Nachdem wir alle Zahlen in dieser Zeile ausgegeben haben, machen wir einen Zeilenumbruch.
        print()

# Hier rufen wir unsere Funktion auf und übergeben die Zeilenanzahl 4.
print_number_triangle(4)
