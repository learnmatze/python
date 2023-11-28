# alter = int(input("Alter eingeben:"))
# if alter >= 18:
#     print("Sie sind volljährig")
# else:
#     print("Sie sind minderjährig")

# zahl1 = int(input("Erste Zahl:"))
# zahl2 = int(input("Zweite Zahl:"))

# def zahl_ist_gleich_kleiner_größer(zahl1, zahl2):
#     if zahl1 == zahl2:
#         print("Zahlen sind gleich")
#         return "gleich"
#     elif zahl1 > zahl2:
#         print("Die erste Zahl ist größer als die zweite Zahl")
#         return "zahl1"
#     #elif zahl1 < zahl2:
#     else:
#         print("Die erste Zahl ist kleiner als die zweite Zahl")
#         return "zahl2"

# #Test
# result = zahl_ist_gleich_kleiner_größer(5,5)
# if result == "gleich":
#     print("Grün")
# else:
#     print("Rot")
# zahl_ist_gleich_kleiner_größer(5,10)
# zahl_ist_gleich_kleiner_größer(10,5)

# deutsch = float(input("Deutsch note eigeben:"))
# englisch = float(input("Englisch note eigeben:"))
# mathematik = float(input("Mathematik note eigeben:"))

# durchschnitt = (deutsch + englisch + mathematik) / 3
# print(f"Der Notendurchschnitt ist {durchschnitt:.2f}")
# print(f"Der Notendurchschnitt ist {durchschnitt:.2e}")

# tag = input("Tag eingeben:").lower()

# arbeitstage = ["montag", "dienstag", "mittwoch", "donnerstag", "freitag"]
# wocheende = ["samstag", "sonntag"]

# if tag == "montag" or tag == "dienstag" or tag == "mittwoch" or tag == "donnerstag" or tag == "freitag":
#     print(f"{tag} ist ein Wochentag.")
# elif tag == "samstag" or tag == "sonntag":
#     print(f"{tag} ist ein Wochenende Tag.")
# else:
#     print(f"{tag} is kein gültiger Wochentag.")

# eingabe = input("Geben sie eine Zeichefolge ein:")
# zeichenlänge = 10
# länge_zeichenfolge = len(eingabe)
# if länge_zeichenfolge > zeichenlänge:
#     print(f"Die Zeichenfolge ist länger als {zeichenlänge} Zeichen. Sie hat {länge_zeichenfolge} Zeichen.")
# elif länge_zeichenfolge < zeichenlänge:
#     print(f"Die Zeichenfolge ist kürzer als {zeichenlänge} Zeichen. Sie hat {länge_zeichenfolge} Zeichen.")
# else:
#     print(f"Die Zeichenfolge ist genau {zeichenlänge} Zeichen lang. Sie hat {länge_zeichenfolge} Zeichen.")

# alter = int(input("Geben sie ihr Alter ein:"))

# if alter >= 16:
#     print("Sie dürfen Alkohol kaufen")
# else:
#     print("Sie dürfen keinen Alkohol kaufen!")
# if alter >= 18:
#     print("Sie dürfen den Führerschein beantragen.")
#     print("Sie dürfen Zigaretten kaufen")        
# else:
#     print("Sie dürfen den Führerschein nicht beantragen.")
#     print("Sie dürfen keine Zigaretten kaufen")
# if alter >= 21:
#     print("Sie dürfen in den Nachtklub gehen")
# else:
#     print("Sie dürfen nicht in den Nachtklub gehen!")

# zahl1 = float(input("Geben sie die erste Zahl1:"))
# operator = input("Geben sie einen Operator (+,-,*,/) an:")
# zahl2 = float(input("Geben sie die erste Zahl1:"))

# if operator == "+":
#     ergebnis = zahl1 + zahl2
# elif operator == "-":
#     ergebnis = zahl1 - zahl2
# elif operator == "*":
#     ergebnis = zahl1 * zahl2
# elif operator == "/":
#     ergebnis = zahl1 / zahl2
# else:
#     print("Falscher Operator")
# print(f"Das Ergebnis von {zahl1} {operator} {zahl2} = {ergebnis}")

# jahr = int(input("Geben sie ein Jahr ein:"))
# if jahr % 4 == 0 and jahr % 100 != 0 or jahr % 400 == 0:
#     print("Das Jahr {jahr} ist ein Schaltjahr")
# else:
#     print("Das Jahr {jahr} ist kein Schaltjahr")

# notedurchschnitt = float(input("Geben sie ihren Notendurchschnitt ein:"))

# if notedurchschnitt >= 1.0 and notedurchschnitt < 1.5:
#     print("Sehr Gut")
# elif notedurchschnitt >= 1.5 and notedurchschnitt < 2.5:
#     print("Gut")
# elif notedurchschnitt >= 2.5 and notedurchschnitt < 3.5:
#     print("Befriedigend")
# elif notedurchschnitt >= 3.5:
#     print("Nicht richtausreichend")
# else:
#     print("Notendurchschnitt ungültig")

# note = input("Gib note ein:")

# match note:
#     case "1":
#         print("Sehr gut")
#     case "2": 
#         print("gut")
#     case "3": 
#         print("befriedigend")
#     case "4": 
#         print("genügend")
#     case "5": 
#         print("nicht genügend")

# if note == "1":
#     print("Sehr gut")
# elif note == "2":
#     print("gut")
# elif note == "3":
#     print("befriedigend")
# elif note == "4":
#     print("genügend")
# elif note == "5":
#     print("nicht genügend")
# else:
#     print("Keine gültige Note")

# buchstabe = input("Bitte einen Buchstaben eingeben:")
# kleinbuchstaben = buchstabe.lower()
# if kleinbuchstaben.isalpha() and len(kleinbuchstaben) == 1:
#     if kleinbuchstaben == "a" or kleinbuchstaben == "e" or kleinbuchstaben == "i" or kleinbuchstaben == "o" or kleinbuchstaben == "u":
#     # if kleinbuchstaben in "aeiou":
#         print("Es ist ein Selbstlaut (Vokal)!")
#     else:
#         print("Es ist ein Mitlaut (Konsunant)!")
# else:
#     print("Bitte geben sie einen BUCHSTABEN ein!")    

# monat = input("Geben Sie den Namen eines Monats ein:")
# monat_lower = monat.lower()

# monate_mit_31_tagen = ["januar","märz","mai","juli","august","oktober","dezember"]
# monate_mit_30_tagen = ["april", "juni", "september", "november"]

# if monat_lower in monate_mit_31_tagen:
#     print(f"Der Monat: {monat_lower.capitalize()} hat 31 Tage")
# elif monat_lower in monate_mit_30_tagen:
#     print(f"Der Monat: {monat_lower.capitalize()} hat 30 Tage")
# elif monat_lower == "februar":
#     print(f"Das Monat: {monat_lower.capitalize()} hat 28 Tage oder 29 Tage")
# else:
#     print("Das ist ein ungültiges Monat")

# zahl = int(input("Geben sie eine Zahl ein."))
# alter = int(input("Gebe sie ihr Alter ein"))

# if zahl < 10:
#     print(f"Die zahl {zahl} is kleiner als 10")
# elif zahl > 10:
#     print(f"Die zahl {zahl} is größer als 10")
# else:
#     print(f"Die zahl {zahl} ist gleich 10")

# if alter < 2:
#     print("Sie sind ein Kind.")
# elif alter < 18:
#     print("Sie sind ein Jugendlicher")
# elif alter < 65:
#     print("Sie sind ein Erwachsener")
# else:    
#     print("Sie sind ein Senior")

# temperatur = float(input("Geben sie eine Temperatur ein:"))
# umwandeln = input("Möchten Sie von Celsius nach Fahrenheit (C) oder von Fahrenheit nach Celsius (F) umwandeln?")
# umwandeln_groß = umwandeln.upper()

# if umwandeln == "C":
#     fahrenheit = (temperatur * 9 / 5) + 32
#     print(f"{temperatur} Grad Celsius entspricht {fahrenheit} Fahrenheit.")
# elif umwandeln == "F":
#     celsius = (temperatur - 32) / 9 / 5
#     print(f"{temperatur} Fahrenheit entspricht {celsius} grad celsius")
# else:
#     print("Ungültige Eingabe")

# benutzername = input("Benutzername:")
# password = input("Password:")
# if benutzername == "admin" and password == "12345":
#     print("Anmeldung erfolgreich")
# else:
#     print("Anmeldung nicht erfolgreich")

# wochentag = int(input("Bitte eine Zahle von 1 bis 7 eingeben (Wochetag):"))

# match wochentag:
#     case 1:
#         print("Montag")
#     case 2:
#         print("Dienstag")
#     case 3:
#         print("Mittwoch")
#     case 4:
#         print("Donnerstag")
#     case 5: 
#         print("Freitag")
#     case 6: 
#         print("Samstag")
#     case 7:
#         print("Sonntag")
#     case _:
#         print("Kein Tag")
    
# a = float(input("Länge der ersten Seite (a):"))
# b = float(input("Länge der zweiten Seite (b):"))
# c = float(input("Länge der dritten Seite (c):"))

# if a == b == c:
#     print("Es ist ein gleichseitiges Dreieck!")
# elif a == b or a == c or b == c:
#     print("Es ist ein gleichschenkeliges Dreieck")
# else:
#     print("Es ist ein ungleichschenkeliges Dreieck")    

# def maskiere_email(email):
#     parts = email.split('@')
#     replacepart = "ddd"
#     replacedomainpart = "ttt"
#     if len(parts) == 2:
#         name, domain = parts
#         len_name = len(name)
#         replace_name = "x" * len_name
#         print(name)
#         print(domain)
#         # example.com
#         domainpart = domain.split('.')[-1]
#         print(domainpart)        
#         maskierte_email = f"{replace_name}@{replacepart}.{replacedomainpart}"
#         print(maskierte_email)
#         return maskierte_email
#     else:
#         return email

# email = "schober@example.com"
# maskierte_mail = maskiere_email(email)
# print(maskierte_mail)

# def create_initialen(vorname, nachname):
#     vorname = vorname.strip()
#     nachname = nachname.strip()
#     initialen = vorname[0].upper() + nachname[0].upper()
#     return initialen

# vorname = input("Geben sie ihren Vornamen ein:")
# nachname = input("Geben sie ihren Nachnamen ein:")

# initialen = create_initialen(vorname, nachname)
# print(f"Die initialen für ihren namen {vorname} {nachname} sind {initialen}")

# def entferne_leerzeichen_vorne_und_hinten(satz):
#     satz_ohne_vorne_und_hinten_leerzeichen = satz.strip()
#     return satz_ohne_vorne_und_hinten_leerzeichen

# satz = """                                     Hallo es sind viele leerzeichen!      
#   - ist eh gut --                      
# """
# satz_ohne_vorne_und_hinten_leerzeichen = entferne_leerzeichen_vorne_und_hinten(satz)
# print(satz)
# print(satz_ohne_vorne_und_hinten_leerzeichen)

# def bereinige_schwein_text(text):
#     bereinigter_text = text.replace('Sau','Schwein')
#     return bereinigter_text

# def bereinige_huhn_text(text):
#     bereinigter_text = text.replace('Hendl','Huhn')
#     return bereinigter_text

# def bereinige_text(text, unerwünschtes_wort, ersetzt_durch_wort):
#     bereinigter_text = text.replace(unerwünschtes_wort, ersetzt_durch_wort)
#     return bereinigter_text

# text = "Die Sau hat 150kg"
# bereinigter_schweine_text = bereinige_text(text, "Sau", "Schwein")
# print(text)
# print(bereinigter_schweine_text)
# text = "Das Hendl hat 5kg"
# print(text)
# print(bereinige_text(text, "Hendl", "Huhn"))

# def zaehle_wörter(text):
#     wörter = text.split(' ')
#     print(wörter)
#     anzahl_wörter = len(wörter)
#     return anzahl_wörter

# text = input("Bitte geben sie einen Text ein:")
# # text = "Dieser Text hat einige wörter!"
# anzahl_wörter = zaehle_wörter(text)
# print(f"Der Text: {text} hat {anzahl_wörter} Wörter")

# def vergleiche_zeichenketten(zeichenkette1, zeichenkette2):
#     zeichenkette1_lower = zeichenkette1.lower()
#     zeichenkette2_lower =  zeichenkette2.lower()
#     print(f"{zeichenkette1_lower} == {zeichenkette2_lower}")
#     return zeichenkette1_lower == zeichenkette2_lower
#     # if zeichenkette1_lower == zeichenkette2_lower:
#     #     return True
#     # else:
#     #     return False

# text_klein = "es ist alles klein geschrieben nur KLEIN nicht"
# text_nicht_klein = "Es ist alles klein geschrieben nur klein nicht"
# print(f"{text_klein} | {text_nicht_klein}")
# sind_zeichenketten_gleich = vergleiche_zeichenketten(text_klein, text_nicht_klein)
# print(sind_zeichenketten_gleich)

# def finde_größere_zahl(zahl1, zahl2):
#     if zahl1 >= zahl2:
#         return zahl1
#     else:
#         return zahl2    
    
# zahl1 = 5
# zahl2 = 5
# größere_zahl = finde_größere_zahl(zahl1, zahl2)
# print(größere_zahl)

# def berechne_operation(zahl1, zahl2, operation):
#     if operation.lower() == "add":
#         return zahl1 + zahl2
#     elif operation.lower() == "subtract":
#         return zahl1 - zahl2
#     elif operation.lower() == "multiply":
#         return zahl1 * zahl2
#     # else:
#     #     return zahl1 * zahl2

# zahl1 = 10
# zahl2 = 5
# add_result = berechne_operation(zahl1, zahl2, "add")
# subtract_result = berechne_operation(zahl1, zahl2, "subtract")
# mulitply_result = berechne_operation(zahl1, zahl2, "multiply")
# sqrt_result = berechne_operation(zahl1, zahl2, "sqrt")
# divide_result = berechne_operation(zahl1, zahl2, "divide")
# print(f"{zahl1} + {zahl2} = {add_result}")
# print(f"{zahl1} - {zahl2} = {subtract_result}")
# print(f"{zahl1} * {zahl2} = {mulitply_result}")
# if divide_result == None:
#     print("Operation wird nicht unterstützt")
# if sqrt_result == None:
#     print("Operation wird nicht unterstützt")

# def größter_wert_in_liste(liste):
#     if len(liste) == 0:
#         return 0
#     else:
#         return max(liste)

# def kleinster_wert_in_liste(liste):
#     if len(liste) == 0:
#         return 0
#     else:
#         return min(liste)

# def größter_oder_kleinster_wert_in_liste(liste, größter_oder_kleinster):
#     if len(liste) == 0:
#         return 0
#     if größter_oder_kleinster == "größter":
#         return max(liste)
#     if größter_oder_kleinster == "kleinster":
#         return min(liste)
    
# liste = [5, 8, 12, 3]
# größter_wert = größter_wert_in_liste(liste)
# print(f"In der Liste {liste} ist {größter_wert} der größte Wert")
# kleinster_wert = kleinster_wert_in_liste(liste)
# print(f"In der Liste {liste} ist {kleinster_wert} der kleinste Wert")
# größter_wert = größter_oder_kleinster_wert_in_liste(liste, "größter")
# print(f"In der Liste {liste} ist {größter_wert} der größte Wert")
# kleinster_wert = größter_oder_kleinster_wert_in_liste(liste, "kleinster")
# print(f"In der Liste {liste} ist {kleinster_wert} der kleinste Wert")

# 0 - 100 Punkte
def notengebung(punktanzahl):
    if punktanzahl >= 90:
        return 1
    elif punktanzahl >= 80:
        return 2
    elif punktanzahl >= 70:
        return 3
    elif punktanzahl >= 50:
        return 4
    else:
        return 5
    
punkte = 70
note = notengebung(punkte)
print(f"Mit {punkte} punkten bekommen sie eine {note}")




