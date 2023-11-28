# def teilnehmer(schiedsrichter, linienrichter, *liste_von_teilnehmern):
#     print(f"Der Schiedsrichter ist {schiedsrichter}")
#     print(f"Der Linienrichter ist {linienrichter}")
#     print(type(liste_von_teilnehmern))
#     print(f"Teilnehmer {liste_von_teilnehmern}")

# teilnehmer("Schiri","Linie","Karl","Hans","Franz")

def datenabfrage_args(*daten):
    print(f'Daten: {daten}')
    vorname = daten[0]
    nachname = daten[1]
    alter = daten[2]

def datenabfrage_kwargs(**daten):
    print(f'Daten: {daten}')
    vorname = daten.get('vorname')
    nachname = daten.get('nachname')
    alter = daten.get('alter')

datenabfrage_args('Mathias', 'Schober', 47)
datenabfrage_kwargs(vorname = 'Mathias', nachname = 'Schober', alter=47)
