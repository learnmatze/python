# x = 4
# if x == 4:
#     print("x ist gleich 4")
#     print("x ist gleich 4")
# elif x == 5:
#     print("x ist gleich 5")
#     print("x ist gleich 5")
# elif x == 6:
#     print("x ist gleich 6")
#     print("x ist gleich 6")
# elif x > 0:
#     print("x ist größer als 0")
#     print("x ist größer als 0")
# else:
#     print("Keine Bedingung war true")
# print("Nach der if bedingung.")

# input = int(input("Wie alt bist du?"))
# if input >= 18:
#     print("Du bist volljährig")
# else:
#     print("Du bist nicht volljährig")
# print("Programm ist zu ende")

# is_true = False
# if is_true:
#     print(f"Die variable is_true ist {is_true}")
# else:
#     print(f"Die variable is_true ist {is_true}")
# print('Nach dem If')

def weinsorte():
    wein_sorte = input("Mögen sie roten (r) oder weißen (w) Wein?")
    if wein_sorte == "r":
        print("Sie sind ein Rotweinliebhaber!")
    elif wein_sorte == "w":
        print("Sie sind ein Weißweinliebhaber!")
    else:
        print("Sie mögen anscheinend jeden Wein!")

def biersorte():
    zweite_antwort = input("Mögen sie denn Bier?")
    if zweite_antwort == "j":
        print(f"Sie sind ein Bierliebhaber!")
    elif zweite_antwort == "n":
        print(f"Sie sind kein Bierliebhaber!")
    else:
        dritte_antwort = input("Was mögen sie sonst?")
        print(f"Sie mögen {dritte_antwort}")

antwort = input("Mögen sie guten Wein?")
if (antwort == "j"):
    print("Sie sind ein Weinliebhaber!")
    weinsorte()  
elif (antwort == "n"):
    print("Sie sind kein Weinliebhaber!")
else:
   biersorte()
print("Programm ist zu ende")

