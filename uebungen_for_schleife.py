
# zahl = int(input("Geben sie eine Zahl ein:"))
# summe = 0
# print(f"Schleife läuft von 1 bis {zahl}")
# for count in range(1, zahl):    
#     alte_summe = summe
#     summe = summe + count
#     print(f"neue summe = {alte_summe} + {count} = {summe}")
# print(f"Summe von 1 bis {zahl} ist {summe}")

# for zahl in range(1,11):
#     quadart_zahl = zahl ** 2
#     print(f"Von der zahl {zahl} das quadart ist {quadart_zahl}")    

# for char in "ABCDEFGHIJKL":
#     print(char)

# liste = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L"]
# for item in liste:
#     print(item)

# for ascii_value in range(65, 91):
#     print(chr(ascii_value))

# for zahl in range(1, 21):
#     print(zahl)

# liste =[4, 9, 16, 25, 36, 56, 72, 78, 89, 93, 99]
# for zahl in liste:
#     print(zahl)

# import time

# def logging_start():
#     logfile = "C:\Temp\logging.txt"    
#     with open(logfile, 'a') as file:
#         file.write(f"*** Logging start at {time.ctime(time.time())} ***\n")        

# def logging(logmessage):
#     logfile = "C:\Temp\logging.txt"    
#     with open(logfile, 'a') as file:        
#         file.write(logmessage)

# import time

# def logging_start():
#     logfile = "C:\Windows\Temp\logging.log"
#     with open(logfile, 'a') as file:
#         file.write(f"******* Logging start at {time.ctime(time.time())} *********\n")

# def logging(logmessage):
#     logfile = "C:\Windows\Temp\logging.log"    
#     with open(logfile, 'a') as file:
#         file.write(logmessage)

# zahl = int(input("Bitte geben sie eine zahl ein!"))
# fakultät = 1
# logging_start()
# for value in range(1, zahl + 1):
#     alte_fakultät = fakultät
#     fakultät = fakultät * value
#     logmessage = f"Die fakultät von {value} ({value}!) = {alte_fakultät} * {value} = {fakultät} \n"
#     print(logmessage)
#     logging(logmessage)    
# print(f"Die Fakultät von {zahl} ({zahl}!) = {fakultät}")

# dezimal = int(input("Geben sie eine dezimalzahl ein:"))
# binär_zahl = bin(dezimal)
# print(f"Die Binärdarstellung von {dezimal} ist {binär_zahl}")

# mögliche_primzahl = int(input("Geben sie eine Zahl ein:"))
# for zahl in range(2, 101):
#     is_primzahl = True
#     for teiler in range(2, zahl):
#         if zahl % teiler == 0:
#             is_primzahl = False
#     if is_primzahl == True:
#         print(f"Die Zahl {zahl} ist eine primzahl.")    
        
# for außen in range(1,3):
#     for innen in range(1,5):
#         print(f"Äußere Schleife {außen} - Innere Schleife {innen} durchlauf {außen}-{innen}")

# zahl = int(input("Bitte eine zahl eingeben:"))
# for multiblikations_zahl in range(1,11):   
#     produkt = zahl * multiblikations_zahl
#     print(f"{zahl} * {multiblikations_zahl} = {produkt}")

# satz = "Hallo das ist ein ganz ein neuer python satz."
# wörter = satz.split(' ')
# wörter_count = len(wörter)
# print(f"Der Satz: {satz} hat {wörter_count} wörter")

# wort_count = 0
# for char in satz:
#     if char == " ":
#         wort_count = wort_count + 1
# wort_count = wort_count + 1
# print(f"Der Satz: {satz} hat {wort_count} wörter")

# string = "python"
# string_umgekehrt = string[::-1]
# print(string_umgekehrt)

# umgekehrt_buchstaben = ""
# for buchstabe in string:    
#     umgekehrt_buchstaben = buchstabe + umgekehrt_buchstaben
# print(umgekehrt_buchstaben)

# def generate_liste_python_style(zahl):
#     return list(range(1, zahl + 1))

# def generate_liste_python_for(zahl):
#     liste = []
#     for value in range(1, zahl + 1):
#         liste.append(value)
#     return liste

# zahl = 8
# liste = generate_liste_python_style(zahl)
# print(liste)
# liste = generate_liste_python_for(zahl)
# print(liste)

#string_umgekehrt = string[::-1]

# def is_palindrom_complicated(text):
#     return text.lower().replace(" ", "") == text.lower().replace(" ", "")[::-1]

# def is_palindrom(text):
#     text = text.lower()
#     text = text.replace(" ","")
#     # text_umgekehrt = text[::-1]
#     text_umgekehrt = ""
#     for buchstabe in text:    
#         text_umgekehrt = buchstabe + text_umgekehrt
#     if text == text_umgekehrt:
#         return True
#     return False

# text = "Dreh mal am Herd"
# # text = "Eine Horde bedrohe nie Hunde nein Eule nie oder Debaten reden Edelweine der Boden ehret Debatten nie oder rede nie Debatten über eine Horde"
# print(is_palindrom(text))
# print(is_palindrom_complicated(text))

# def buchstaben_zählen(text, buchstaben):    
#     anzahl = 0
#     for char in text.lower():
#         if char == buchstaben:
#             anzahl = anzahl + 1
#     return anzahl

# text = "Hallo alle Alben sind Albern."
# buchstabe = "l"
# anzahl = buchstaben_zählen(text, buchstabe)
# print(f"Der text '{text}' enhält {anzahl} mal den buchstaben {buchstabe}")


def tisch_des_einmaleins(zahl, bis_wo=10):
    richtig_counter = 0
    for number in range(1, bis_wo + 1):
        eingegebene_zahl = int(input(f"{zahl} * {number} = ?"))        
        result = number * zahl
        if eingegebene_zahl == result:
            print(f"Super richtig! {zahl} * {number} = {result}")
            richtig_counter = richtig_counter + 1
        else:
            print(f"Leider falsch deine Zahl {eingegebene_zahl} Richtig: {zahl} * {number} = {result}")
    if richtig_counter == bis_wo:
        print(f"Super du hast alle ({richtig_counter}/{bis_wo}) Ergebnisse richtig!")
    elif  richtig_counter > bis_wo / 2:
        print(f"Super du hast mehr als 50% ({richtig_counter}/{bis_wo}) Ergebnisse richtig!")            
    else:
        print(f"Üben! Du hast weniger als 50% ({richtig_counter}/{bis_wo}) Ergebnisse richtig!.")
zahl = 5
tisch_des_einmaleins(2)






