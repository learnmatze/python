# obstsorten = ["Apfel","Banane","Orange", "Traube", "Kiwi"]
# print(f"Liste von Obstsorten: {obstsorten}")
# obstsorten.append("Mango")
# print(f"Liste von aktuallisierten Obstsorten: {obstsorten}")

# liste = [1, 2, 3, 4, 5]
# print(f"Das dritte Element der Liste ist {liste[2]}")
# liste[1] = 10
# print(f"Liste ist {liste}")

# tiere = ["Hund", "Katze", "Vogel"]
# print(f"Anzahl der Tiere in der Liste {len(tiere)}")

# farben =["rot", "blau", "grün", "gelb"]
# staedte = ["Berlin", "Paris", "Graz"]
# farben_staedte = farben + staedte
# print(f"Farben und Stadte: {farben_staedte}")

# combinierte_liste = []
# for stadt in staedte:
#     for farbe in farben:    
#         combinierte_liste.append(farbe + stadt)
# print(f"Combinierte Liste: {combinierte_liste}")       

# laender = ["Österreich", "Deutschland", "Frankreich", "Vatikan", "Andora"]
# laender.remove("Österreich")
# print(laender)

# wochentag = "Dienstag"
# wochentage = ["Montag", "Dienstag", "Mittwoch"]
# montag_counter = wochentage.count(wochentag)
# if montag_counter > 0:
#     print(f"Der {wochentag} ist in der Liste")
# else:
#     print(f"Der {wochentag} ist nicht in der Liste")
# if wochentag in wochentage:
#     print(f"Der {wochentag} ist in der Liste")
# else:
#     print(f"Der {wochentag} ist nicht in der Liste")

# zahlen = [1, 2, 3]
# faktor = 3
# # zahlen = zahlen * faktor
# print(zahlen)

# neue_zahlen = []
# for zahl in zahlen:
#     neu_zahl = zahl * faktor
#     neue_zahlen.append(neu_zahl)
# print(neue_zahlen)

# neue_zahlen = [zahl * faktor for zahl in zahlen]
# print(neue_zahlen)

# liste = []
# for zahl in range(1,6):
#     liste.append(zahl)
# print(liste)

# liste = [zahl for zahl in range(1,6)]
# print(liste)

# tiere = ["Affen", "Giraffe", "Nilpferd"]
# fruechte = ["Traube", "Orange", "Banane", "Kokusnuss"]
# kombinierte_liste = tiere + fruechte
# kombinierte_liste.sort()
# print(kombinierte_liste)
# tiere.sort()
# fruechte.sort()
# sort_kombinierte_liste = tiere + fruechte
# print(sort_kombinierte_liste)

# zahlen = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# gerade_zahlen = []
# ungerade_zahlen = []
# for zahl in zahlen:
#     if zahl % 2 == 0:
#         # zahlen.remove(zahl)
#         gerade_zahlen.append(zahl)
#     else:
#         ungerade_zahlen.append(zahl)
# print(f"Die Liste der geraden zahlen {gerade_zahlen} besteht aus {len(gerade_zahlen)} elementen.")
# print(f"Die Liste der ungeraden zahlen {ungerade_zahlen} besteht aus {len(ungerade_zahlen)} elementen.")

# gerade_zahlen = [zahl for zahl in zahlen if zahl % 2 == 0]
# ungerade_zahlen = [zahl for zahl in zahlen if zahl % 2 != 0]
# print(f"Die Liste gerade zahlen {gerade_zahlen} besteht aus {len(gerade_zahlen)} elementen.")
# print(f"Die Liste ungeraden zahlen {ungerade_zahlen} besteht aus {len(ungerade_zahlen)} elementen.")


wochentage = ["Montag", "Dienstag", "Mittwoch", "Donnerstag", "Freitag"]
umgekehrte_wochetage = wochentage[::-1]
wochentage.reverse()
index = 0
for wochentag in wochentage:
    umgekehrte_wochetage.insert(index, wochentag)   
    index -= 1
print(wochentage)


