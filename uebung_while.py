# zahl = int(input("Geben sie eine Zahl ein:"))
# summe = 0
# index = 1
# while index <= zahl:
#     summe = summe + index
#     index += 1
# print(f"Die summe von 1 bis {zahl} ist {summe}")

# import random
# zufallszahl = random.randint(1, 10)
# versuche = 0

# # ist_erraten = False
# while True:
#     user_zahl = int(input("Bitte raten sie eine Zahl (1-100):"))
#     if user_zahl < zufallszahl:       
#         print("Sie haben zu nieder geraten!")
#     elif user_zahl > zufallszahl:        
#         print("Sie haben zu hoch geraten!")
#     else:
#         print(f"Richtig geraten die Zahl ist {zufallszahl}. Sie haben {versuche} Versuche gebraucht.")
#         # ist_erraten = True
#         break
#     versuche += 1

# max_zahl = int(input("Geben sie die maximale Zahl:"))
# print(f"Primzahlen von 1 bis {max_zahl} suchen.")
# zahl = 2
# while zahl <= max_zahl:
#     is_primzahl = True
#     for innere_zahl in range(2, max_zahl - 1):
#         if zahl == innere_zahl:
#             break
#         if zahl % innere_zahl == 0:
#             is_primzahl = False
#             break
#     if is_primzahl == True:
#         print(f"Die Zahl {zahl} ist eine Primzahl")
#     zahl += 1

# primzahl_zahl = int(input("Geben sie bitte eine Zahl ein:"))
# print(f"Ist {primzahl_zahl} eine Primzahl?.")
# is_primzahl = True
# zahl = 2
# # for innere_zahl in range(2, primzahl_zahl - 1):
# while zahl < primzahl_zahl:
#     if primzahl_zahl % zahl == 0:
#         is_primzahl = False
#         break
#     zahl += 1
# if is_primzahl == True:
#     print(f"Die Zahl {primzahl_zahl} ist eine Primzahl")
# else:
#     print(f"Die Zahl {primzahl_zahl} ist keine Primzahl")

# zahl = int(input("Geben sie eine Zahl ein:"))
# fakultaet = 1
# index = 1
# while index <= zahl:
#     fakultaet = fakultaet * index
#     index += 1
# print(f"Die Fakultät von {zahl} ist {fakultaet} => {zahl}! = {fakultaet}")

# text = input("Bitte Text eingeben:")
# index = 1
# while index < len(text):
#     index = index + 1
# print(f"Die länge des textes {text} ist {len(text)}")

# basis = int(input("Geben sie die basis ein:"))
# exponent = int(input("Geben sie den Exponenten ein:"))
# produkt = 1
# index = 1
# while index <= exponent:
#     produkt = produkt * basis
#     index = index + 1
# print(f"Die basis {basis} hoch {exponent} ist {produkt} => {basis}^{exponent} = {produkt}")

# text = input("Bitte Text eingeben:")
# umgedrehter_text = text[::-1]
# print(f"Der Text {text} ungedreht ist {umgedrehter_text}")

# umgedrehter_text = ""
# index = len(text) - 1
# while index >= 0:
#     umgedrehter_text = umgedrehter_text + text[index]
#     index = index - 1
# print(f"Der Text {text} ungedreht ist {umgedrehter_text}")

index = 1
# while index <= 100:
#     if index % 3 == 0 and index % 5 == 0:
#         print("FizzBuzz")
#     elif index % 3 == 0:
#         print("Fizz")
#     elif index % 5 == 0:
#         print("Buzz")
#     else:
#         print(index)
#     index = index + 1

