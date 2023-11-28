def bmi(gewicht, groesse):
    bmi = gewicht / groesse ** 2
    return bmi

def abnehmen(gewicht, abnahme):
    return gewicht - abnahme

def zunehmen(gewicht, zunahme):
    return gewicht + zunahme

def sag_gewicht(name):
    print(f"Hallo {name} zu bist zu dick!")
