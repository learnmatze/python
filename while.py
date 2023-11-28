# zahl = 1
# while zahl <= 5:
#     print(zahl)
#     zahl = zahl - 1
# print("While Schleife fertig.")

# secret_number = 12
# number = 0
# while number != secret_number:
#     number = int(input("Erraten Sie die secrete number:"))

# liste = [1, 2, 3, 4, 5]
# for item in liste:
#     print(f"For: {item}")

# index = 0
# user_input = ""
# while index < len(liste) and user_input != 'y':
#     print(f"While: {liste[index]}")
#     user_input = input("Wollen sie abbrechen? (y/n):")
#     index = index + 1

# password = "geheim"
# user_eingabe = ""
# versuche = 0
# while user_eingabe != password and versuche < 5:
#     user_eingabe = input("Bitte geben sie das geheime passwort ein:")
#     versuche = versuche + 1
# if versuche == 5:
#     print("Sie haben nach 5 versuchen das password nicht erraten.")
# else:
#     print(f"Sie haben {versuche} versuche gebraucht um das password zu erraten!")

# import random

# zufallszahl = int(random.random() * 100)
# print(zufallszahl)
# print("Zahlen erraten!")
# benutzerzahl = 0
# while benutzerzahl != zufallszahl:
#     benutzerzahl = int(input("Geben sei eine Zahl ein:"))
#     if benutzerzahl > zufallszahl:
#         print(f"Ihre Zahl {benutzerzahl} ist größer als die zufallszahl.")
#     elif benutzerzahl < zufallszahl:
#         print(f"Ihre Zahl {benutzerzahl} ist kleiner als die zufallszahl.")
#     else:
#         print(f"Sie haben die Zahl erraten! {benutzerzahl} - {zufallszahl}")

# zahl = int(input("Bitte geben sie eine Zahl ein:"))
# summe = 0
# value = 1
# while value <= zahl:    
#     value = value + 1
#     summe = summe + value    
# print(f"Die summe von 1 bis {zahl} = {summe}")

# zahl = 1
# while zahl <= 5: #and zahl % 2 == 0:
#     print(zahl)
#     zahl += 1

#for zahl in range(10):
# zahl = 1
# while zahl <= 10:    
#     if zahl == 5:
#         break
#     print(zahl)
#     zahl += 1

zahl = 1
while zahl <= 10:     
    if zahl % 2 == 0:
        zahl += 1
        continue
    print(zahl)
    zahl += 1
