def write_dict(file_name):
    augen = {
        "Spinnen": 8,
        "Ameisen": 2,
        "Schmetterlinge": 2 * 100,
        "Grillen": 3,
        "Tausendfüssler": 2,
        "Skorpione": 4,
        "Krebse": 2,    
        "Quallen": 0
    }
    with open(file_name, 'w') as file:
        for key, value in augen.items():
            file.write(f"{key}: {value}\n")

# write_dict("augen.txt")


def augen_aus_file_lesen():
    file_name = "augen.txt"
    augen = {}
    with open(file_name, 'r') as file:
        for line in file:
            key, value = line.strip().split(": ")
            augen[key] = value
    # print(f"augen aus file {augen}")
    return augen

def insekten_eigenschaften(insekten_namen):
    # key : value -> "Spinnen" : 8 -> "Ameisen" : 6
    beine = {
        "Spinnen": 8,
        "Ameisen": 6,
        "Schmetterlinge": 6,
        "Grillen": 4,
        "Tausendfüssler": 1000,
        "Skorpione": 8,
        "Krebse": 10,
        "Quallen": 12       
    }
    augen = augen_aus_file_lesen()        
    anzahl_beine = beine.get(insekten_namen)
    anzahl_augen = augen.get(insekten_namen)
    insekten_string = f"{insekten_namen} haben {anzahl_beine} Beine und {anzahl_augen} Augen"
    return insekten_string

print('Spinnen haben 8 Beine')
print(insekten_eigenschaften('Spinnen'))
print('Ameisen haben 6 Beine')
print(insekten_eigenschaften('Ameisen'))
print('Schmetterlinge haben 6 Beine')
print(insekten_eigenschaften('Schmetterlinge'))
print('Grillen haben 4 Beine')
print(insekten_eigenschaften('Grillen'))
print('Tausendfüssler haben 1000 Beine')
print(insekten_eigenschaften('Tausendfüssler'))
print('Skorpione haben 8 Beine')
print(insekten_eigenschaften('Skorpione'))
print('Krebse haben 10 Beine')
print(insekten_eigenschaften('Krebse'))
print('Quallen haben 12 Beine')
print(insekten_eigenschaften('Quallen'))

# augen = {
    #     "Spinnen": 8,
    #     "Ameisen": 2,
    #     "Schmetterlinge": 2 * 100,
    #     "Grillen": 3,
    #     "Tausendfüssler": 2,
    #     "Skorpione": 4,
    #     "Krebse": 2,        
    #     "Quallen": 0
    # }

# print('Spinnen haben 8 Beine')
# print('Ameisen haben 6 Beine')
# print('Schmetterlinge haben 6 Beine')
# print('Grillen haben 4 Beine')
# print('Tausendfüssler haben 1000 Beine')
# print('Skorpione haben 8 Beine')
# print('Krebse haben 10 Beine')

# import random

# def gitarre_klang():
#     return random.choice(['D','E','F','G','A'])

# def trompete_klang():
#     return random.choice(['C','D', 'E', 'F', 'G'])

# def schlagzeug_klang():
#     return random.choice(['Kick', 'Hi-Hat', 'Bass'])

# print("Die Gitarre spielt den Ton: " + gitarre_klang())
# print("Die Trompete spielt den Ton: " + trompete_klang())
# print("Das Schlagzeug spielt den Ton: " + schlagzeug_klang())
# print("Die Trompete spielt den Ton: " + trompete_klang())
# print("Die Trompete spielt den Ton: " + trompete_klang())
# print("Das Schlagzeug spielt den Ton: " + schlagzeug_klang())
# print("Die Gitarre spielt den Ton: " + gitarre_klang())
# print("Die Gitarre spielt den Ton: " + gitarre_klang())
# print("Die Gitarre spielt den Ton: " + gitarre_klang())
# print("Die Trompete spielt den Ton: " + trompete_klang())
# print("Die Trompete spielt den Ton: " + trompete_klang())
# print("Das Schlagzeug spielt den Ton: " + schlagzeug_klang())
# print("Die Trompete spielt den Ton: " + trompete_klang())

# print("Die Gitarre spielt den Ton: " + random.choice(['C','D','E','F','G','A']))
# print("Die Trompete spielt den Ton: " + random.choice(['C','D', 'E', 'F', 'G']))
# print("Das Schlagzeug spielt den Ton: " + random.choice(['Kick', 'Snair', 'Hi-Hat', 'Bass']))
# print("Die Trompete spielt den Ton: " + random.choice(['C','D', 'E', 'F', 'G']))
# print("Die Trompete spielt den Ton: " + random.choice(['C','D', 'E', 'F', 'G']))
# print("Das Schlagzeug spielt den Ton: " + random.choice(['Kick', 'Snair', 'Hi-Hat', 'Bass']))
# print("Die Gitarre spielt den Ton: " + random.choice(['C','D','E','F','G','A']))
# print("Die Gitarre spielt den Ton: " + random.choice(['C','D','E','F','G','A']))
# print("Die Gitarre spielt den Ton: " + random.choice(['C','D','E','F','G','A']))
# print("Die Trompete spielt den Ton: " + random.choice(['C','D', 'E', 'F', 'G']))
# print("Die Trompete spielt den Ton: " + random.choice(['C','D', 'E', 'F', 'G']))
# print("Das Schlagzeug spielt den Ton: " + random.choice(['Kick', 'Snair', 'Hi-Hat', 'Bass']))
# print("Die Trompete spielt den Ton: " + random.choice(['C','D', 'E', 'F', 'G']))



# def anzahl_beine_frosch():
#     return "4"

# def anzahl_beine_tintenfisch():
#     return "0"

# def anzahl_beine_schildkröte():
#     return "4"

# print('Ausgabe mit Funktionen')
# print('Bein informationen:')
# print(f'Ein Frosch hat {anzahl_beine_frosch()} Beine')
# print(f'Ein Tintenfisch {anzahl_beine_tintenfisch()} Beine')
# print(f'Ein Schildkröte {anzahl_beine_schildkröte()} Beine')

# print('Bein informationen:')
# print(f'Ein Frosch hat {anzahl_beine_frosch()} Beine')
# print(f'Ein Tintenfisch {anzahl_beine_tintenfisch()} Beine')
# print(f'Ein Schildkröte {anzahl_beine_schildkröte()} Beine')

# print('Bein informationen:')
# print(f'Ein Frosch hat {anzahl_beine_frosch()} Beine')
# print(f'Ein Tintenfisch {anzahl_beine_tintenfisch()} Beine')
# print(f'Ein Schildkröte {anzahl_beine_schildkröte()} Beine')

# print('Bein informationen:')
# print(f'Ein Frosch hat {anzahl_beine_frosch()} Beine')
# print(f'Ein Tintenfisch {anzahl_beine_tintenfisch()} Beine')
# print(f'Ein Schildkröte {anzahl_beine_schildkröte()} Beine')

# print('Original ausgabe')
# print('Bein informationen:')
# print('Ein Frosch hat zwischen 3 und 5 Beine')
# print('Ein Tintenfisch hat zwischen 0 und 8 Beine')
# print('Ein Schildkröte hat zwischen 4 und 5 Beine')

# print('Bein informationen:')
# print('Ein Frosch hat zwischen 3 und 5 Beine')
# print('Ein Tintenfisch hat zwischen 0 und 8 Beine')
# print('Ein Schildkröte hat zwischen 4 und 5 Beine')

# print('Bein informationen:')
# print('Ein Frosch hat zwischen 3 und 5 Beine')
# print('Ein Tintenfisch hat zwischen 0 und 8 Beine')
# print('Ein Schildkröte hat zwischen 4 und 5 Beine')

# print('Bein informationen:')
# print('Ein Frosch hat zwischen 3 und 5 Beine')
# print('Ein Tintenfisch hat zwischen 0 und 8 Beine')
# print('Ein Schildkröte hat zwischen 4 und 5 Beine')



# def auto_gestartet(marke):
#     print(f"{marke} Auto wurde schnell gestartet")

# def auto_hupt(marke):
#     print(f"{marke} Auto hat laut gehupt")

# def auto_gefahren(marke):
#     print(f"{marke} Auto hat ist weit gefahren")

# def auto_gestoppt(marke):
#     print(f"{marke} Auto wurde apprupt gestoppt")

# auto_gestartet('Mercedes')
# auto_hupt('Mercedes')
# auto_gefahren('Mercedes')
# auto_gestoppt('Mercedes')

# auto_gestartet('BMW')
# auto_hupt('BMW')
# auto_gefahren('BMW')
# auto_gestoppt('BMW')

# auto_gestartet('Lada')
# auto_hupt('Lada')
# auto_gefahren('Lada')
# auto_gestoppt('Lada')

# auto_gestartet('VW')
# auto_hupt('VW')
# auto_gefahren('VW')
# auto_gestoppt('VW')

# print('Mercedes Auto wurde schnell gestartet')
# print('Mercedes Auto hat laut gehupt')
# print('Mercedes Auto ist weit gefahren')
# print('Mercedes Auto wurde apprupt gestoppt')

# print('BMW Auto wurde gestartet')
# print('BMW Auto hat gehupt')
# print('BMW Auto ist gefahren')
# print('BMW Auto wurde gestoppt')

# print('Lada Auto wurde gestartet')
# print('Lada Auto hat gehupt')
# print('Lada Auto ist gefahren')
# print('Lada Auto wurde gestoppt')

# print('VW Auto wurde gestartet')
# print('VW Auto hat gehupt')
# print('VW Auto ist gefahren')
# print('VW Auto wurde gestoppt')

print('Programmende')


# def addieren_plus_drei(zahl1, zahl2):
#     result = zahl1 + zahl2 + 8
#     return result

# print('Programmanfang')
# a = 3
# b = 5
# # result = a + b + 8
# result = addieren_plus_drei(a, b)
# print(result)
# c = 11
# d = 15
# # result = c + d + 8
# result = addieren_plus_drei(a, b)
# print(result)
# e = 22
# f = 33
# # result = c + d + 8
# result = addieren_plus_drei(a, b)
# print(result)
# print('Programmende')
