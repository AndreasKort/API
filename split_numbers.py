# zum ausführen in der powerchell "python .\ip_validation.py 128.80.86.125" 128.80.86.125 da kann man jede ip adresse eingeben die überprüft werden soll.
# Python Datei: ip_validation.py
# Autor: Andreas Kort
# Split-Validierung in Python hinzugefügt überprüfen ob 4 Elemente sind und Ip adresse im Terminal eingeben Version 3

import sys  # Importiere das sys-Modul, um die Argumente aus der Bash-Umgebung zu erhalten wenn nicht vorhanden. 

# Beschriebene Funktion
# In den () können Parameter eingesetzt werden, in diesem Fall nicht nötig.
def split_numbers(ip_string):
    numbers = ip_string.split(".")
    return [int(number) for number in numbers]
# .split splittet den ip_string an den Stellen "." und löst so die Strings auf.
# Mit int(number) for number in numbers und int() überarbeiten wir die Strings in Ganzzahlen, die dann mit , geteilt werden.
# Danach werden die Strings "" entfernt und in der IP-Variable 128, 80, 86, 125 gespeichert und ausgegeben.
# Neue Funktion check_numbers einbauen
def check_numbers(numbers_list):
    # Überprüfe, ob genau 4 Elemente vorhanden sind, wenn ja gut, wenn nein, falsch
    if len(numbers_list) != 4:
        return False

    # Überprüfe, ob jedes Element zwischen 0 und 255 ist
    for number in numbers_list:
        if not (0 <= number <= 255):
            return False

    return True

if __name__ == "__main__":
    # Erhalte das Argument von der Bash-Umgebung mit sys.argv[1]
    ip_string = sys.argv[1]
    
    # Rufe die Funktion split_numbers mit dem übergebenen Argument auf
    ip_numbers = split_numbers(ip_string)
    print(ip_numbers)

    # Rufe die Funktion check_numbers mit dem Ergebnis von split_numbers auf
    result = check_numbers(ip_numbers)
    print(result)

