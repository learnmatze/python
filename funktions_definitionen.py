# def f(a, b, **c):
#     print(f"a: {a}, b:{b}, c:{c}")    

# f(1, 2, vorname = 'Mathias', nachname = 'Schober', alter=47)

def dividieren(x,y):
    print(f"x: {x}, y:{y} = {x / y}")

# dividieren(4,2)

def sag_hallo(vorname="Tim", nachname="Johns"):
    print(f"Hallo {vorname}, {nachname}")

# def verkehrsstrafen(number=None):
#     print(f"Meine Verkehrsstrafen sind {number}")

# verkehrsstrafen()

# sag_hallo("Mathias", "Schober")

def einkaufen(**produkte):
    for key in produkte:
        print(f"{key}")

# einkaufen(sellerie=2.5, bananen=3.8, trauben=5.6)

# def f(x=3):
#     print(f"{x}")

# def f(x,y):
#     print(f"{y}")

# f(10)
# f(5,6)
# f(1, 2, vorname = 'Mathias', nachname = 'Schober', alter=47)

def ueberweisen(sender, *mehrere_empfaenger):
    print(f"sender: {sender} to {mehrere_empfaenger}")

# ueberweisen("Schober", "Karl", "Hubert", "Franz")

def email_senden(sender, empfaenger="test@schober.com", subject="Test", body="Das ist ein Textmail"):
    print(f"Sender {sender} schickt Email an {empfaenger} - {subject} - {body}")

# email_senden("Mathias")
# email_senden("Mathias","karl@example.com","Lieber Karl","Danke für die Einladung!")

def f(x=1, y=2, z=3, *params1, **params2):
    print(f"{x}, {y}, {z}, {params1}, {params2}")

f("Test1","Test2",vorname="Mathias", nachname="Schober")









