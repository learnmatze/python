import unittest

# def gruss():
#     print('Hallo!')
#     print('Wie geht es ihnen?')

# def grussbenutzer(user):
#     print(f'Hallo {user}')
#     print('Wie geht es dir?')

# def potenzieren(x, y):
#     if x == 0:
#         return "0 geht nicht"
#     return x**y

def grundrechnungsarten(a, b):
    summe = a + b
    differenz = a - b
    produkt = a * b
    quotient = a / b
    # print(f"Summe: {summe}, Differenz: {differenz}, Produkt: {produkt}, Quotient: {quotient}")
    return summe, differenz, produkt, quotient

print('Programmanfang')
result1 = grundrechnungsarten(2, 2)
result2 = grundrechnungsarten(2, 4)
result3 = grundrechnungsarten(3, 3)
print('Programmende')

# def erstellegrussformel(grussformel, user):
#     formel = f'Grussformel: {grussformel} {user}'
#     return formel

# def potenzieren(x, y=2):
#     return x**y

# def grundrechnungsarten(a, b):
#     summe = a + b
#     differenz = a - b
#     produkt = a * b
#     quotient = a / b
#     return summe, differenz, produkt, quotient

# print('Programmanfang')


# s,d,p,q = grundrechnungsarten(2,3)
# print(f"Summe: {s}, Differenz: {d}, Produkt: {p}, Quotient: {q}")

# ergebnis = potenzieren(2,3)
# print(ergebnis)

# benutzer = "Mathias"
# formel = "Hallo"
# # grussformel(formel, benutzer)
# grussformel = erstellegrussformel(formel, benutzer)
# print(grussformel)
# formel = "Servus"
# benutzer = "Karl"
# # grussformel(formel, benutzer)
# grussformel = erstellegrussformel(formel, benutzer)
# print(grussformel)
# print('Programmende')