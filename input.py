# print("Wie geht es ihnen?")
# laune = input("Wie ist ihre Laune heute?")
# print(f"Ich sehe ihre Laune ist {laune}")

# a = float(input("Zahl a eingeben:"))
# b = float(input("Zahl b eingeben:"))
# print(type(a))
# print(type(b))
# summe = a + b
# print(f"Die summe von a {a} + b {b} = {summe}")

def getlength(string):
    return len(string)

# input = input("Bitte gib eine Zeichenkette ein:")
# lenght = getlength(input)
# print(f"Die länge der Zeichenkette {input} ist {lenght}")

def celsius_to_fahrenheit(celsius):
    return (celsius * 9 / 5) + 32

input = float(input("Temperatur in Celsius eingeben"))
fahrenheit = celsius_to_fahrenheit(input)
print(f"{input} grad celsius sind {fahrenheit} fahrenheit")




