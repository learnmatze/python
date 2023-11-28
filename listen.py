zahlen = [1, 2, 3, 4, 5]
namen = ["Alice", "Bob", "Charlie"]
gemischt = [1, "Hallo", True, [4,3,2,1]]
leer = []
print(f"{zahlen} - {namen} - {gemischt} - {leer}")
zahlen = [1, 2, 3, 4, 5]
erster_wert = zahlen[0:2]  # Erstes Element (Index 0)
dritter_wert = zahlen[2:4]  # Drittes Element (Index 2)
print(f"{zahlen} - {erster_wert} - {dritter_wert}")

zahlen = [1, 2, 3, 4, 5]
zahlen.append(6)  # Hinzufügen eines Elements ans Ende der Liste
zahlen.append(7) 
zahlen.append("Osterhase") 
zahlen[0] = 20
print(f"{zahlen}")
# zahlen.remove(2)  # Entfernen eines Elements (nach Wert)
# zahlen.remove(3)  # Entfernen eines Elements (nach Wert)
# zahlen.pop(len(zahlen) - 1)
# zahlen.insert(0, 12)
# zahlen.insert(1, 12)
counter = zahlen.count(12)
verkehrte_liste = zahlen.reverse()
print(f"{zahlen}")
print(f"{verkehrte_liste}")

# zahlen[0] = 10  # Ändern eines Elements
