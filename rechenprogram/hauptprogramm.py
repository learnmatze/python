import taschenrechner as tr
# from utils.person import *
import utils.person

result = tr.addieren(2,5)
print(f"Die addition von 2,5 ist {result}")

result = tr.subtrahieren(4,2)
print(f"Die subtraktion von 4,2 ist {result}")

vorname_string = utils.person.format_vorname('Mathias')
print(vorname_string)
nachname_string = utils.person.format_nachname('Schober')
print(nachname_string)