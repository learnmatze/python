# zahlen = [1, 2, 3, 4, 5]
# namen = ["Alice", "Bob", "Charlie"]
# gemischt = [1, "Hallo", True, [4,3,2,1]]
# leer = []
# print(f"{zahlen} - {namen} - {gemischt} - {leer}")
# zahlen = [1, 2, 3, 4, 5]
# erster_wert = zahlen[0:2]  # Erstes Element (Index 0)
# dritter_wert = zahlen[2:4]  # Drittes Element (Index 2)
# print(f"{zahlen} - {erster_wert} - {dritter_wert}")

# zahlen = [1, 2, 3, 4, 5]
# zahlen.append(6)  # Hinzufügen eines Elements ans Ende der Liste
# zahlen.append(7) 
# zahlen.append("Osterhase") 
# zahlen[0] = 20
# print(f"{zahlen}")
# zahlen.remove(2)  # Entfernen eines Elements (nach Wert)
# zahlen.remove(3)  # Entfernen eines Elements (nach Wert)
# zahlen.pop(len(zahlen) - 1)
# zahlen.insert(0, 12)
# zahlen.insert(1, 12)
# counter = zahlen.count(12)
# verkehrte_liste = zahlen.reverse()
# print(f"{zahlen}")
# print(f"{verkehrte_liste}")

# zahlen[0] = 10  # Ändern eines Elements

# text = "hallo python"
# teil = text[::2]
# print(teil)
# print(type(text))

# liste = [1, 2, 3, 4, 5]
# teil_liste = liste[::2]
# print(teil_liste)
# print(type(liste))
# print(len(liste))

# boolean = True
# print(len(boolean))

# empty_liste = ["Meine Liste"]
# for index in range(1,11):
#     empty_liste.append(index)
# print(empty_liste)

# bits = [1, 0]
# print(bits)
# print(bits * 10)

# liste = [2, 4, 1, 8, 7, 12]
liste = ['b', 'g', 'a', 'x', 'z', 'c']
# print(type(liste))
# print(liste)

# liste.sort(reverse=True)
# print(liste)
tier_liste = ['bär', 'schwein', 'kuh', 'tiger', 'esel', 'tiger']
# print(tier_liste)
# tier_liste.insert(0, 'biene')
# tier_liste.insert(len(tier_liste), 'biene')
# print(tier_liste)
# index = tier_liste.index('kuh')
# print(f"Die Kuh ist an index {index} / position {index + 1} der Liste {tier_liste}")
# kuh = tier_liste.pop(index)
# print(kuh)
# print(tier_liste)
# tier_liste.clear()
# print(tier_liste)

# tier_liste.remove('biene')
# del(tier_liste[0:4])
# print(tier_liste)
# for index in range(0,len(tier_liste)):
# while len(tier_liste) > 0:
#     # print(index)
#     # pop_item = tier_liste.pop(0)
#     pop_item = tier_liste[0]
#     if tier_liste != []:
#         tier_liste.remove(pop_item)
#     print(tier_liste)
#     print(pop_item)


# tier_liste.append(['bär','tiger'])
# print(tier_liste)
# for tier in tier_liste:
#     print(tier)
# tier_liste = tier_liste + ['schwein','kuh']
# print(tier_liste)
# for tier in tier_liste:
#     print(tier)



# tiger_count = tier_liste.count('tiger')
# while tiger_count > 1:
#     tier_liste.remove('tiger')
#     tiger_count = tier_liste.count('tiger')
# print(tier_liste)
# print(tier_liste)

# esel_count = tier_liste.count('esel')
# bär_count = tier_liste.count('bär')
# tiger_count = tier_liste.count('tiger')
# hahn_count = tier_liste.count('hahn')
# print(f"Der Hahn kommt {hahn_count}, Esel kommt {esel_count}, der Bär kommt {bär_count} und der Tiger kommt {tiger_count} in der Liste vor.")

# tier_liste = ['bär', 'schwein', 'kuh', 'tiger', 'esel', 'tiger']
# lotto_liste = [12,25,31,33,38,41]
# # print(tier_liste)
# tier_string = '/'.join(tier_liste)
# # print(tier_string)
# lotto_string = ""
# lotto_string_liste = []
# for zahl in lotto_liste:    
#     zahl_string = str(zahl)
#     print(zahl_string)
#     lotto_string_liste.append(zahl_string)
# print(lotto_string_liste)
# lotto_string = ','.join(lotto_string_liste)
# print(lotto_string)

matrix = [
    'kuh',
    [[1,2,3],[3,4,5],[6,7,8]],
    [4,5,6],
    [7,8,9]
    ]

erste_liste = matrix[1]
# print(erste_liste)
eins_aus_liste = erste_liste[2]
eins_aus_matrix = matrix[1][2]
# print(eins_aus_liste)
# print(eins_aus_matrix)
for item in matrix:
    print(item)
    if isinstance(item, list):
        for inneritem in item:
            print(inneritem)
            # if isinstance(inneritem, list):
            # for inner_inner_item in inneritem:
            #     print(inner_inner_item)