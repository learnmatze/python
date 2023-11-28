def hallowelt():
    print('Hallo, Welt')

def addieren(zahl1, zahl2):
    summe = zahl1 + zahl2
    return summe

def multiblizieren(zahl1, zahl2):
    produkt = zahl1 * zahl2
    return produkt

def check_ist_zahl_gerade(zahl):
    is_gerade = (zahl % 2 == 0) # True or False
    return is_gerade

def durchmesser_berechnung(radius):
    durchmesser = radius * 2
    return durchmesser

fix_string = "sdlfjsdöalfjsaödlfjsödfjaösdfj"

def sind_zeichenfolgen_gleich(string1):
    return string1 == fix_string

def greet(name):
    return f"Hallo, {name}"

def word_length(word):
    return len(word)

def to_upper(text):
    return text.upper()

def to_lower(text):
    return text.lower()

def is_even(zahl):
    return zahl % 2 == 0

def reverse_string(string):
    reversstring = string[::-1]
    return reversstring

def repeat_char(char, zahl):
    return char * zahl

import math

def volumen_kugel(radius):
    volumen = 4/3 * math.pi * radius**3
    return round(volumen,2)

def temperatur_umrechnung(celsius):
    fahrenheit = (celsius * 9 / 5) + 32
    kelvin = celsius + 273.15
    return fahrenheit, kelvin

def rechteck_fläche_umfang(länge, breite):
    fläche = länge * breite
    umfang = 2 * (länge + breite)
    return fläche, umfang

def teilnehmer()

länge = 10
breite = 5
fläche, umfang = rechteck_fläche_umfang(länge, breite)
print(f"Ein Rechteck mit der Länge {länge} und der Breite {breite} hat eine Fläche von {fläche} und einen Umfang von {umfang}")

# celsius = 10
# result = temperatur_umrechnung(celsius)
# print(result)
# fahrenheit, kelvin = temperatur_umrechnung(celsius)
# print(f"Die Temperatur in Celsius({celsius}) ist {fahrenheit} in Fahrenheit und {kelvin} in Kelvin")
# print(f"Die Temperatur in Celsius({celsius}) ist {result[0]} in Fahrenheit und {result[1]} in Kelvin")




# radius = 2
# volumen = volumen_kugel(radius)
# print(f"Das Volumen einer Kugel mit dem Radius {radius} ist {volumen}")

# radius = 4
# volumen = volumen_kugel(radius)
# print(f"Das Volumen einer Kugel mit dem Radius {radius} ist {volumen}")

# char = 'a'
# n = 10
# result = repeat_char('a', n)
# print(f"Das Zeichen {char} {n} mal wiederholt gibt: {result}")

# string = "python"
# result = reverse_string(string)
# print(f"Der string {string} von hinten nach vorne {result}")

# string = "hallo python world"
# result = reverse_string(string)
# print(f"Der string {string} von hinten nach vorne {result}")


# zahl = 4
# result = is_even(zahl)
# print(f"Zahl {zahl} ist gerade: {result}")

# zahl = 7
# result = is_even(zahl)
# print(f"Zahl {zahl} ist gerade: {result}")

# string = "Python"
# result = to_lower(string)
# print(f"Der text {string} tolower ist {result}")


# string = "python"
# result = word_length(string)
# print(f"Der string {string} hat {result} Buchstaben")

# greeting = greet('Mathias')
# print(greeting)

# string1 = "Python"
# string2 = "Python"
# result = sind_zeichenfolgen_gleich(string1, string2)
# print(f"sind: {string1} und {string2} gleich? {result}")
# string1 = "Python"
# string2 = "python"
# result = sind_zeichenfolgen_gleich(string1, string2)
# print(f"sind: {string1} und {string2} gleich? {result}")


# radius = 2
# durchmesser = durchmesser_berechnung(radius)
# print(f"Für einen Kreis mit dem Radius: {radius} ist der Durchmesser: {durchmesser}")


# zahl = 4
# result = check_ist_zahl_gerade(zahl)
# print(f"Die Zahl: {zahl} is Gerade: {result}")
# zahl = 7
# result = check_ist_zahl_gerade(zahl)
# print(f"Die Zahl: {zahl} is Gerade: {result}")

# result = multiblizieren(3, 5)
# print(result)

# result = addieren(3, 5)
# print(result)

# hallowelt()