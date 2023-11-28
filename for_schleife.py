# obstkorb = ["Apfel","Birne","Banane","Pfirsich","Erdbeere"]

# for obst in obstkorb:
#     if obst == "Birne":
#         print("Birnen sind nicht lecker")
#     else:
#         print(f"Das obst {obst} ist sehr lecker")
# print("For schleife beendet")

# for value in range(3):
#     print(f"Hallo python - {value}. Wiederholung")



# liste = list(range(2,10))
# print(liste)

# def berechne_listen_wert(index, zahl):
#     return index + zahl

# for index in [0, 1, 2, 3, 4]:
#     print(f"Für den Index {index} berechnete zahl {berechne_listen_wert(index,5)}")
#     # print(f"Hallo python - {index}. Wiederholung")

# hunde = ['Dackel','Pudel','Boxer','Schäferhund']
# kosten = [5, 6, 10, 8]
# counter = 0
# for hund in hunde:
#     print(f"Counter: {counter}")
#     hund_kosten = kosten[counter]
#     print(f"hundkosten: {hund_kosten}")
#     print(f"Der hund: {hund} kostet {hund_kosten} Euro.")
#     counter = counter + 1

# text = "Hallo"
# neuentext = ""
# counter = 0
# for zeichen in text:
#     # print(counter)
#     if counter % 2 == 0:
#         neuentext = neuentext + "-" + zeichen
#     else:
#         neuentext = neuentext + "*" + zeichen
#     print(neuentext)  
#     counter = counter + 1  
# print(neuentext)

katzen = ["Mencoon", "Nacktkatze", "Löwe", "Gepard", "Leopard", "Tiger", "Luchs", "Puma"]

# counter = 0
# for katze in katzen:
#     print(f"Die Katze {katze} ist an der position {counter} in der Liste Katzen")
#     counter = counter + 1

# enumerate_katzen = list(enumerate(katzen))
# print(katzen)
# print(enumerate_katzen)

for index, katze in enumerate(katzen):
    print(f"Die Katze {katze} ist an der position {index} in der Liste Katzen")

# liste = [2, 3, 4, 5]
# print(liste)
# liste = [x for x in range(2,12) if x % 2 == 0]
# print(liste)

# liste = []
# for x in range(2,12):
#     if x % 2 == 0:
#         liste.append(x)
# print(liste)

# for index in [1, 2, 3, 4, 5]:
# zahl = int(input("Bitte zahl eingeben:"))
# operator = input("Bitte operator eingeben:")
# range_zahl = 5
# if operator == "-":
#     range_zahl = 5 - zahl
# if operator == "+":
#     range_zahl = 5 + zahl
# for index in range(range_zahl):
#     print(index)
#     print(katzen[index])    


# for index in [0, 2, 4, 8]:
#     print(f"Hallo python - {index}. Wiederholung")

zahlen = [10, 8, 3, 7, 9, 6]

range_liste = list(range(len(zahlen)))
print(zahlen)
print(range_liste)
for index in range_liste:    
    print(f"An der Position {index} steht die Zahl {zahlen[index]}")

